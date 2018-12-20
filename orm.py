#!/usr/bin/python2
# -*- coding: utf-8 -*-

import MySQLdb as mdb


class Field(object):
    pass


class Expr(object):
    def __init__(self, model, kwargs):
        pass

    def update(self, **kwargs):
        pass

    def limit(self, rows, offset=None):
        pass

    def select(self):
        pass

    def count(self):
        pass


class ModelMetaclass(type):
    table = None
    fields = dict()

    def __init__(self, name, bases, attrs):
        super(ModelMetaclass, self).__init__(name, bases, attrs)
        for key, val in self.__dict__.iteritems():
            if isinstance(val, Field):
                self.fields[key] = val


class Model(object):
    __metaclass__ = ModelMetaclass

    def save(self):
        sql = 'insert ignore into %s(%s) values (%s);' % (
            self.table,
            ', '.join(self.__dict__.keys()),
            ', '.join(['%s'] * len(self.__dict__))
        )
        return Database.execute(sql, self.__dict__.values())

    @classmethod
    def where(cls, **kwargs):
        return Expr(cls, kwargs)


class Database(object):
    autocommit = True
    connection = None
    db_config = dict()

    @classmethod
    def connect(cls, **db_config):
        cls.connection = mdb.connect(
            host=db_config.get('host', 'localhost'),
            port=int(db_config.get('port', 2222)),
            user=db_config.get('user', 'root'),
            passwd=db_config.get('password', ''),
            db=db_config.get('database', 'test'),
            charset=db_config.get('charset', 'utf-8')
        )
        cls.connection.autocommit(cls.autocommit)
        cls.db_config.update(db_config)

    @classmethod
    def get_connection(cls):
        if not cls.connection or not cls.connection.open:
            cls.connect(**cls.db_config)
        try:
            cls.connection.ping()
        except mdb.OperationalError:
            cls.connect(**cls.db_config)
        return cls.connection

    @classmethod
    def execute(cls, *args):
        cursor = cls.get_connection().cursor()
        cursor.execute(*args)
        return cursor

    def __del__(self):
        if self.connection and self.conn.open:
            self.connection.close()


def execute_raw_sql(sql, params=None):
    pass