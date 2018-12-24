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

    userid = Field()
    username = Field()
    password = Field()
    record = Field()
    permission = Field()


class ScoreModel(Model):
    table = 'Score'

    userid = Field()
    movieid = Field()
    comDate = Field()
    value = Field()
    content = Field()
    watched = Field()
    star = Field()


class MovieModel(Model):
    table = 'Movie'

    movieid = Field()
    mname = Field()
    director = Field()
    editor = Field()
    actor = Field()
    mtype = Field()
    countryOrLocation = Field()
    language = Field()
    date = Field()
    duration = Field()
    othername = Field()
    IMDb = Field()
    introduction = Field()
    allActors = Field()
    numOfEvaluator = Field()
    star5 = Field()
    star4 = Field()
    star3 = Field()
    star2 = Field()
    star1 = Field()