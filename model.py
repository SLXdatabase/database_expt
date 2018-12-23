#!/usr/bin/python2
# -*- coding: utf-8 -*-

from orm import *


Database.connect(
    host='localhost',
    port=3306,
    user='mysql',
    password='mysql',
    database='dodo'
)


class UserModel(Model):
    table = 'User'


class ScoreModel(Model):
    table = 'Score'


class MovieModel(Model):
    table = 'Movie'
