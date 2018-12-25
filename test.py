#!/usr/bin/python2
# -*- coding: utf-8 -*-

from orm import execute_raw_sql
from model import UserModel, ScoreModel, MovieModel
import unittest


def create_user_instance(
        userid,
        username,
        password,
        record,
        permission
    ):
    user = UserModel()

    user.userid = userid
    user.username = username
    user.password = password
    user.record = record
    user.permission = permission

    user.save()
    return user

def create_score_instance(
        userid,
        movieid,
        comDate,
        value,
        content,
        watched,
        star
    ):
    score = ScoreModel()

    score.userid = userid
    score.movieid = movieid
    score.comDate = comDate
    score.value = value
    score.content = content
    score.watched = watched
    score.star = star

    score.save()
    return score

def create_movie_instance(
        movieid,
        mname,
        director,
        editor,
        actor,
        mtype,
        countryOrLocation,
        language,
        date,
        duration,
        othername,
        IMDb,
        introduction,
        allActors,
        numOfEvaluator,
        star5,
        star4,
        star3,
        star2,
        star1
    ):
    movie = MovieModel()

    movie.movieid = movieid
    movie.mname = mname
    movie.director = director
    movie.editor = editor
    movie.actor = actor
    movie.mtype = mtype
    movie.countryOrLocation = countryOrLocation
    movie.language = language
    movie.date = date
    movie.duration = duration
    movie.othername = othername
    movie.IMDb = IMDb
    movie.introduction = introduction
    movie.allActors = allActors
    movie.numOfEvaluator = numOfEvaluator
    movie.star5 = star5
    movie.star4 = star4
    movie.star3 = star3
    movie.star2 = star2
    movie.star1 = star1

    movie.save()
    return movie


class TestUserModel(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_instance(self):
        pass

    def test_select(self):
        pass

    def test_update(self):
        pass

    def test_limit(self):
        pass

    def test_count(self):
        pass


class TestScoreModel(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_instance(self):
        pass

    def test_select(self):
        pass

    def test_update(self):
        pass

    def test_limit(self):
        pass

    def test_count(self):
        pass


class TestMovieModel(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_instance(self):
        pass

    def test_select(self):
        pass

    def test_update(self):
        pass

    def test_limit(self):
        pass

    def test_count(self):
        pass


if __name__ == "__main__":
    unittest.main()
