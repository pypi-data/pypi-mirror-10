# -*- coding: utf-8 -*-

__all__ = (
    'RawSqlMigrateException',
    'IncorrectDbBackendException',
    'InconsistentParamsException',
    'ParamRequiredException',
    'NoForwardMigrationsFound',
    'NoBackwardMigrationsFound',
    'IncorrectMigrationFile',
)


class RawSqlMigrateException(Exception):
    pass

class IncorrectDbBackendException(Exception):
    pass


class InconsistentParamsException(RawSqlMigrateException):
    pass


class ParamRequiredException(RawSqlMigrateException):
    pass


class NoForwardMigrationsFound(RawSqlMigrateException):
    pass


class NoBackwardMigrationsFound(RawSqlMigrateException):
    pass


class IncorrectMigrationFile(RawSqlMigrateException):
    pass


class IncorrectPackage(RawSqlMigrateException):
    pass

