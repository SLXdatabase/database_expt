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

        cnt = len(list(users))
        self.assertEquals(1, cnt)

    def test_count(self):
        cnt = UserModel.where(username="strawberry").count()

        self.assertEquals(1, cnt)


class TestScoreModel(unittest.TestCase):
    
    def setUp(self):
        if list(ScoreModel.where(userid="1998080911").select()) == []:
            create_score_instance(
                "1998080911",
                "0000000001",
                "2018-12-1",
                5,
                u"电影肥肠好看哈哈哈哈哈哈",
                1,
                4
            )
        if list(ScoreModel.where(userid="1999022511").select()) == []:
            create_score_instance(
                "1999022511",
                "0000000002",
                "2018-12-7",
                14,
                u"还阔以，嘻嘻",
                1,
                3
            )
        if list(UserModel.where(userid="1999080611").select()) == []:
            create_score_instance(
                "1999080611",
                "0000000003",
                "2018-12-4",
                60,
                u"龙猫太可爱了",
                1,
                5
            )

    def tearDown(self):
        execute_raw_sql("truncate table Score;")

    def test_instance(self):
        score = ScoreModel.where(userid="1998080911").select().next()

        self.assertEquals(score.userid, "1998080911")
        self.assertEquals(score.movieid, "0000000001")
        self.assertEquals(score.comDate, "2018-12-1")
        self.assertEquals(score.value, 5)
        self.assertEquals(score.content, u"电影肥肠好看哈哈哈哈哈哈")
        self.assertEquals(score.watched, 1)
        self.assertEquals(score.star, 4)

    def test_select(self):
        scores = ScoreModel.where().select()

        for score in scores:
            if score.userid == "1998080911": pass
            elif score.userid == "1999022511": pass
            else:
                self.assertEquals(score.userid, "1999080611")
                self.assertEquals(score.movieid, "0000000003")
                self.assertEquals(score.comDate, "2018-12-4")
                self.assertEquals(score.value, 60)
                self.assertEquals(score.content, u"龙猫太可爱了")
                self.assertEquals(score.watched, 1)
                self.assertEquals(score.star, 5)


    def test_update(self):
        ScoreModel.where(userid="1999080611").update(star=2)
        score = ScoreModel.where(userid="1999080611").select().next()

        self.assertEquals(score.userid, "1999080611")
        self.assertEquals(score.movieid, "0000000003")
        self.assertEquals(score.comDate, "2018-12-4")
        self.assertEquals(score.value, 60)
        self.assertEquals(score.content, u"龙猫太可爱了")
        self.assertEquals(score.watched, 1)
        self.assertEquals(score.star, 2)

    def test_limit(self):
        scores = ScoreModel.where(content=u"电影肥肠好看哈哈哈哈哈哈").limit(2).select()

        cnt = len(list(scores))
        self.assertEquals(1, cnt)

    def test_count(self):
        cnt = ScoreModel.where(ScoreModel.value > 13).count()

        self.assertEquals(2, cnt)


class TestMovieModel(unittest.TestCase):
    
    def setUp(self):
        if list(MovieModel.where(movieid="9999999991").select()) == []:
            create_movie_instance(
                "9999999991",
                u"海王",
                u"温子仁",
                u"编剧",
                u"罗钥轩/海王",
                u"玄幻",
                u"中国",
                u"中文",
                u"2018-12-2",
                145,
                u"海的女儿",
                u"www.123.com",
                u"很好看的电影",
                u"师毓洁/智障",
                3466,
                1531,
                245,
                456,
                1000,
                234
            )
        if list(MovieModel.where(movieid="9999999992").select()) == []:
            create_movie_instance(
                "9999999992",
                u"龙猫",
                u"导演2",
                u"编剧2",
                u"罗钥轩/龙",
                u"动漫",
                u"日本",
                u"日语",
                u"2018-12-23",
                120,
                u"dragon",
                u"www.456.com",
                u"很不好看的电影",
                u"师毓洁/猫",
                5000,
                2300,
                40,
                60,
                1300,
                1300
            )
        if list(MovieModel.where(movieid="9999999993").select()) == []:
            create_movie_instance(
                "9999999993",
                u"狗十三",
                u"曹保平",
                u"编剧3",
                u"张雪迎/十三",
                u"爱情",
                u"中国",
                u"中文",
                u"2018-12-25",
                118,
                u"狗狗十三啦",
                u"www.789.com",
                u"冷冷冷冷了很好看的电影",
                u"师毓洁/狗子",
                1800,
                300,
                600,
                300,
                500,
                100
            )

    def tearDown(self):
        execute_raw_sql("truncate table Movie;")

    def test_instance(self):
        movie = MovieModel.where(movieid="9999999991").select().next()

        self.assertEquals(movie.movieid, "9999999991")
        self.assertEquals(movie.mname, u"海王")

    def test_select(self):
        movies = MovieModel.where().select()

        for movie in movies:
            if movie.movieid == "9999999991": pass
            elif movie.movieid == "9999999992": pass
            else:
                self.assertEquals(movie.movieid, "9999999993")
                self.assertEquals(movie.mname, u"狗十三")

    def test_update(self):
        MovieModel.where(movieid="9999999991").update(mname=u"海的女儿")
        movie = MovieModel.where(movieid="9999999991").select().next()

        self.assertEquals(movie.mname, u"海的女儿")

    def test_limit(self):
        movies = MovieModel.where(introduction=u"很好看的电影").limit(2).select()

        cnt = len(list(movies))
        self.assertEquals(1, cnt)

    def test_count(self):
        cnt = MovieModel.where(introduction=u"很好看的电影").count()

        self.assertEquals(1, cnt)


if __name__ == "__main__":
    unittest.main()
