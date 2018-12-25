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
        if list(UserModel.where(userid="1998080911").select()) == []:
            create_user_instance(
                "1998080911",
                "strawberry",
                "Leo980809",
                u"来电狂想/云南虫谷/无敌破坏王",
                0
            )
        if list(UserModel.where(userid="1999022511").select()) == []:
            create_user_instance(
                "1999022511",
                "mu001999",
                "woaini18",
                u"海王/蜘蛛侠",
                0
            )
        if list(UserModel.where(userid="1999080611").select()) == []:
            create_user_instance(
                "1999080611",
                "likemilk",
                "woaihemilk",
                u"龙猫/狗十三",
                0
            )

    def tearDown(self):
        execute_raw_sql("truncate table User;")

    def test_instance(self):
        user = UserModel.where(userid="1998080911").select().next()

        self.assertEquals(user.userid, "1998080911")
        self.assertEquals(user.username, "strawberry")
        self.assertEquals(user.password, "Leo980809")
        self.assertEquals(user.record, u"来电狂想/云南虫谷/无敌破坏王")

    def test_select(self):
        users = UserModel.where().select()

        for user in users:
            if user.userid == "1998080911": pass
            elif user.userid == "1999022511": pass
            else:
                self.assertEquals(user.userid, "1999080611")
                self.assertEquals(user.username, "likemilk")
                self.assertEquals(user.password, "woaihemilk")
                self.assertEquals(user.record, u"龙猫/狗十三")

    def test_update(self):
        UserModel.where(userid="1998080911").update(record=u"来电狂想/云南虫谷/无敌破坏王")
        user = UserModel.where(userid="1998080911").select().next()

        self.assertEquals(user.userid, "1998080911")
        self.assertEquals(user.username, "strawberry")
        self.assertEquals(user.password, "Leo980809")
        self.assertEquals(user.record, u"来电狂想/云南虫谷/无敌破坏王")

    def test_limit(self):
        users = UserModel.where(username="strawberry").limit(2).select()

        cnt = 0
        for user in users: cnt += 1
        self.assertEquals(1, cnt)

    def test_count(self):
        cnt = UserModel.where(username="strawberry").count()

        self.assertEquals(1, cnt)


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
