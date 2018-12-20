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
        pass

    @classmethod
    def get_connection(cls):
        pass

    @classmethod
    def execute(cls, *args):
        pass

    def __del__(self):
        pass


def execute_raw_sql(sql, params=None):
    pass