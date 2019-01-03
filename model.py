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


class DirectorModel(Model):
    table = 'Director'

    dirtorid = Field()
    dirorname = Field()
    dirsex = Field()
    dirage = Field()
    dircountry = Field()
    dirheight = Field()
    dirbirthplace = Field()
    dirnation = Field()
    dirconstellation = Field()


class EditorModel(Model):
    table = 'Editor'

    ediid = Field()
    ediname = Field()
    edisex = Field()
    ediage = Field()
    edicountry = Field()
    ediheight = Field()
    edibirthplace = Field()
    edination = Field()
    ediconstellation = Field()


class ActorModel(Model):
    table = 'Actor'

    actorid = Field()
    actorname = Field()
    sex = Field()
    age = Field()
    country = Field()
    height = Field()
    birthplace = Field()
    nation = Field()
    constellation = Field()


class MovActModel(Model):
    table = 'MovAct'

    movieid = Field()
    actorid = Field()
    character = Field()


class MDModel(Model):
    table = 'MD'

    movieid = Field()
    dirtorid = Field()


class MEModel(Model):
    table = 'ME'

    movieid = Field()
    ediid = Field()
