# -*- coding: utf-8 -*-

from os import rename, path
from sys import stdout

from importlib import import_module

from raw_sql_migrate import config as file_config
from raw_sql_migrate.exceptions import (
    InconsistentParamsException, NoForwardMigrationsFound, NoBackwardMigrationsFound,
    IncorrectMigrationFile, ParamRequiredException, IncorrectDbBackendException,
)
from raw_sql_migrate.helpers import (
    generate_migration_name, get_package_migrations_directory,
    create_migration_file, get_migrations_list, get_migration_python_path_and_name,
    get_migration_file_content, create_squashed_migration_file, get_file_system_latest_migration_number,
    DatabaseHelper,
)

__all__ = (
    'Api',
)


class Api(object):

    config = None
    database_api = None
    database_helper = None

    def __init__(self, config=None):

        if config is not None:
            self.config = config
        else:
            self.config = file_config

        try:
            database_api_module = import_module(self.config.engine)
            self.database_api = database_api_module.DatabaseApi(
                self.config.host,
                self.config.port,
                self.config.name,
                self.config.user,
                self.config.password,
                self.config.additional_connection_params
            )
        except (ImportError, AttributeError, ):
            raise IncorrectDbBackendException(u'Failed to import given database engine: %s' % self.config.engine)

        self.database_helper = DatabaseHelper(self.database_api, self.config.history_table_name)

    def create(self, package, name):
        """
        Creates a new migration in given package. Command makes next things:
        1. creates migration structure if package does not have one
        2. creates migration history table if it does not exist
        3. makes new migration file with given name in migration folder
        :param package: path to package where migration should be created
        :param name: human readable name of migration
        :return: migration name
        :raises ParamRequiredException: raises if 'package' or 'name' are not given.
        """
        if not package:
            raise ParamRequiredException(u'Provide correct package where to store migrations')

        if not name:
            raise ParamRequiredException(u'Provide correct migration name')

        if not self.database_helper.migration_history_exists():
            self.database_helper.create_history_table()

        current_migration_number = get_file_system_latest_migration_number(package)
        path_to_migrations = get_package_migrations_directory(package)
        migration_name = generate_migration_name(name, current_migration_number + 1)
        create_migration_file(path_to_migrations, migration_name)

    def forward(self, package=None, migration_number=None):
        """
        Searches for not applied migrations and applies them. If migration number is left None
        applies all new migrations.
        :param package: path to package which migrations should be applied, omit to migrate all packages in config.
        :param migration_number: number of migration to migrate to.
        :return: None
        :raises InconsistentParamsException: raises if migration number is less than current migration number or
        package or packages list in config are not specified.
        :raises NoForwardMigrationsFound: raises if no new migrations found
        :raises IncorrectMigrationFile: raises if no forward function is found in migration file
        """
        if package is not None:
            packages = (package, )
        else:
            if self.config.packages:
                packages = self.config.packages
            else:
                raise InconsistentParamsException(
                    u'Inconsistent params: specify package or packages list in config'
                )

        for package_for_migrate in packages:
            current_migration_number = self.database_helper.get_latest_migration_number(package_for_migrate)

            if migration_number is not None and migration_number < current_migration_number:
                raise InconsistentParamsException(
                    u'Inconsistent params given: migration number cant\'t be less than current'
                )

            if not migration_number:
                lambda_for_filter = lambda number: number > current_migration_number
            elif migration_number:
                lambda_for_filter = lambda number: current_migration_number < number <= migration_number
            else:
                lambda_for_filter = lambda number: number == current_migration_number + 1

            migration_data = get_migrations_list(package_for_migrate)
            new_migrations_numbers = filter(lambda_for_filter, migration_data.keys())

            if not new_migrations_numbers:
                if package is not None:
                    raise NoForwardMigrationsFound(u'No new migrations found in package %s' % package_for_migrate)
                else:
                    stdout.write('No new migrations found in package %s. Skipping.\n' % package_for_migrate)
                    continue

            for new_migration_number in new_migrations_numbers:
                migration_python_path, name = get_migration_python_path_and_name(
                    migration_data[new_migration_number]['file_name'], package_for_migrate
                )
                module = import_module(migration_python_path)
                if not hasattr(module, 'forward'):
                    raise IncorrectMigrationFile(u'File %s has no forward function' % migration_python_path)
                stdout.write('Migrating forward to migration %s in package %s\n' % (name, package_for_migrate, ))
                module.forward(self.database_api)
                self.database_helper.write_migration_history(name, package_for_migrate)

    def backward(self, package, migration_number=None):
        """
        Searches for applied migrations and rollbacks changes made. If migration number is left None
        downgrades to first migration.
        :param package: path to package which migrations should be rolled back
        :param migration_number: number of migration to rollback to. If not given rollbacks until first migration.
        :return: None
        :raises InconsistentParamsException: raises if migration number is greater than current migration number.
        :raises NoBackwardMigrationsFound: raises if no applied migrations found
        :raises IncorrectMigrationFile: raises if no backward function is found in migration file
        """
        current_migration_number = self.database_helper.get_latest_migration_number(package)

        if migration_number and migration_number > current_migration_number:
            raise InconsistentParamsException(
                u'Inconsistent params given: migration number cant\'t be greater then current.'
            )

        if not migration_number:
            lambda_for_filter = lambda number: number <= current_migration_number
        elif migration_number:
            lambda_for_filter = lambda number: current_migration_number > number >= migration_number
        else:
            lambda_for_filter = lambda number: number == current_migration_number - 1

        migration_data = get_migrations_list(package)
        previous_migrations_numbers = filter(lambda_for_filter, migration_data.keys())

        if not previous_migrations_numbers:
            raise NoBackwardMigrationsFound(
                u'No backward migrations found in to downgrade from %s' % current_migration_number
            )

        for previous_migration_number in sorted(previous_migrations_numbers, reverse=True):
            migration_python_path, name = get_migration_python_path_and_name(
                migration_data[previous_migration_number]['file_name'], package
            )
            module = import_module(migration_python_path)
            if not hasattr(module, 'backward'):
                raise IncorrectMigrationFile(u'File %s has no backward function' % migration_python_path)
            stdout.write('Downgrading from migration %s\n' % name)
            module.backward(self.database_api)
            self.database_helper.delete_migration_history(name, package)

    def status(self, package=None):
        """
        Returns status dictionary for given package or all packages in migration history
        if 'package' is left None. Dictionary has next structure:
        {
            package:
            {
                name: migration name,
                processed_at: datetime of migration apply
            }
        }
        :param package: given status of the given package
        """
        if not self.database_helper.migration_history_exists():
            self.database_helper.create_history_table()

        return self.database_helper.status(package)

    def squash(self, package, begin_from=1, name=None):
        """
        Squashes several migrations into one. Command reads all not applied migrations
        in package migration directory and appends content of forward and backward
        function into result functions. Squash also renames squashed migration with
        'squashed_' prefix.
        :param package: path to package which migrations should be squashed
        :param begin_from: migration number to begin squash from. Should be not less than 1
        :param name: squashed migration name
        """
        result_forward_content = ''
        result_backward_content = ''
        current_migration_number = self.database_helper.get_latest_migration_number(package)
        last_file_system_migration_number = get_file_system_latest_migration_number(package)

        if begin_from <= current_migration_number or current_migration_number > last_file_system_migration_number:
            raise InconsistentParamsException(
                u'Can squash only applied migrations. Current applied migration number is %s' % current_migration_number
            )

        if begin_from < 1:
            raise InconsistentParamsException(
                u'begin_from should be not less than 1'
            )

        migration_data = get_migrations_list(package)
        ordered_keys = sorted(migration_data.keys())

        for key in ordered_keys[begin_from:]:
            file_name = migration_data[key]['file_name']
            file_path = migration_data[key]['file_path']
            stdout.write('Squashing migration %s...' % file_name)
            file_forward_content, file_backward_content = get_migration_file_content(file_path)
            result_forward_content += file_forward_content
            result_backward_content += file_backward_content
            new_file_name = 'squashed_%s' % file_name
            new_file_path = path.join(migration_data[key]['file_directory'], new_file_name)
            rename(migration_data[key]['file_path'], new_file_path)
        last_number = ordered_keys[-1]
        if name is None:
            name = '%04d_squashed_%04d_to_%04d.py' % (begin_from, begin_from, last_number, )
        else:
            name = generate_migration_name(name, begin_from)
        path_to_package_migrations = get_package_migrations_directory(package)
        create_squashed_migration_file(
            path_to_package_migrations, name, result_forward_content, result_backward_content
        )
