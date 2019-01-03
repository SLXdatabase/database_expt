#!/usr/bin/python2
# -*- coding: utf-8 -*-

from orm import execute_raw_sql
from model import *
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

def create_editor_instance(
        ediid,
        ediname,
        edisex,
        ediage,
        edicountry,
        ediheight,
        edibirthplace,
        edination,
        ediconstellation
    ):
    editor = EditorModel()

    editor.ediid = ediid
    editor.ediname = ediname
    editor.edisex = edisex
    editor.ediage = ediage
    editor.edicountry = edicountry
    editor.ediheight = ediheight
    editor.edibirthplace = edibirthplace
    editor.edination = edination
    editor.ediconstellation = ediconstellation

    editor.save()
    return editor

def create_actor_instance(
        actorid,
        actorname,
        sex,
        age,
        country,
        height,
        birthplace,
        nation,
        constellation
    ):
    actor = ActorModel()

    actor.actorid = actorid
    actor.actorname = actorname
    actor.sex = sex
    actor.age = age
    actor.country = country
    actor.height = height
    actor.birthplace = birthplace
    actor.nation = nation
    actor.constellation = constellation

    actor.save()
    return actor

def create_director_instance(
        dirtorid,
        dirorname,
        dirsex,
        dirage,
        dircountry,
        dirheight,
        dirbirthplace,
        dirnation,
        dirconstellation
    ):
    director = DirectorModel()

    director.dirtorid = dirtorid
    director.dirorname = dirorname
    director.dirsex = dirsex
    director.dirage = dirage
    director.dircountry = dircountry
    director.dirheight = dirheight
    director.dirbirthplace = dirbirthplace
    director.dirnation = dirnation
    director.dirconstellation = dirconstellation

    director.save()
    return director

def create_movact_instance(
        movieid,
        actorid,
        character
    ):
    movact = MovActModel()

    movact.movieid = movieid
    movact.actorid = actorid
    movact.character = character

    movact.save()
    return movact

def create_md_instance(
        movieid,
        dirtorid
    ):
    md = MDModel()

    md.movieid = movieid
    md.dirtorid = dirtorid

    md.save()
    return md

def create_me_instance(
        movieid,
        ediid
    ):
    me = MEModel()

    me.movieid = movieid
    me.ediid = ediid

    me.save()
    return me


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

    def rm_tearDown(self):
        execute_raw_sql("truncate table User;")

    def test_main(self):
        user = UserModel.where(userid="1998080911").select().next()

        self.assertEquals(user.userid, "1998080911")
        self.assertEquals(user.username, "strawberry")
        self.assertEquals(user.password, "Leo980809")
        self.assertEquals(user.record, u"来电狂想/云南虫谷/无敌破坏王")


        users = UserModel.where().select()

        for user in users:
            if user.userid == "1999080611": pass
            elif user.userid == "1999022511": pass
            else:
                self.assertEquals(user.userid, "1998080911")
                self.assertEquals(user.username, "strawberry")
                self.assertEquals(user.password, "Leo980809")
                self.assertEquals(user.record, u"来电狂想/云南虫谷/无敌破坏王")


        UserModel.where(userid="1998080911").update(record=u"来电狂想/云南虫谷/无敌破坏王")
        user = UserModel.where(userid="1998080911").select().next()

        self.assertEquals(user.userid, "1998080911")
        self.assertEquals(user.username, "strawberry")
        self.assertEquals(user.password, "Leo980809")
        self.assertEquals(user.record, u"来电狂想/云南虫谷/无敌破坏王")


        users = UserModel.where(username="strawberry").limit(2).select()

        cnt = 0
        for user in users: cnt += 1
        self.assertEquals(1, cnt)


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
        if list(ScoreModel.where(userid="1999080611").select()) == []:
            create_score_instance(
                "1999080611",
                "0000000003",
                "2018-12-4",
                60,
                u"龙猫太可爱了",
                1,
                5
            )

    def rm_tearDown(self):
        execute_raw_sql("truncate table Score;")

    def test_main(self):
        score = ScoreModel.where(userid="1998080911").select().next()

        self.assertEquals(score.userid, "1998080911")
        self.assertEquals(score.movieid, "0000000001")
        self.assertEquals(score.comDate, "2018-12-1")
        self.assertEquals(score.value, 5)
        self.assertEquals(score.content, u"电影肥肠好看哈哈哈哈哈哈")
        self.assertEquals(score.watched, 1)
        self.assertEquals(score.star, 4)


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



        ScoreModel.where(userid="1999080611").update(star=2)
        score = ScoreModel.where(userid="1999080611").select().next()

        self.assertEquals(score.userid, "1999080611")
        self.assertEquals(score.movieid, "0000000003")
        self.assertEquals(score.comDate, "2018-12-4")
        self.assertEquals(score.value, 60)
        self.assertEquals(score.content, u"龙猫太可爱了")
        self.assertEquals(score.watched, 1)
        self.assertEquals(score.star, 2)


        scores = ScoreModel.where(content=u"电影肥肠好看哈哈哈哈哈哈").limit(2).select()

        cnt = 0
        for score in scores: cnt += 1
        self.assertEquals(1, cnt)


        cnt = ScoreModel.where(content=u"电影肥肠好看哈哈哈哈哈哈").count()

        self.assertEquals(1, cnt)


class TestMovieModel(unittest.TestCase):

    def setUp(self):
        if list(MovieModel.where(movieid="0000000001").select()) == []:
            create_movie_instance(
                "0000000001",
                u"海王",
                u"温子仁",
                u"编剧",
                u"师毓洁/智障",
                u"玄幻",
                u"中国",
                u"中文",
                u"2018-12-2",
                145,
                u"海的女儿",
                u"www.123.com",
                u"很好看的电影",
                u"罗钥轩/海王",
                3466,
                1531,
                245,
                456,
                1000,
                234
            )
        if list(MovieModel.where(movieid="0000000002").select()) == []:
            create_movie_instance(
                "0000000002",
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
        if list(MovieModel.where(movieid="0000000003").select()) == []:
            create_movie_instance(
                "0000000003",
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

    def rm_tearDown(self):
        execute_raw_sql("truncate table Movie;")

    def test_main(self):
        movie = MovieModel.where(movieid="0000000001").select().next()

        self.assertEquals(movie.movieid, "0000000001")
        self.assertEquals(movie.mname, u"海王")


        movies = MovieModel.where().select()

        for movie in movies:
            if movie.movieid == "0000000001": pass
            elif movie.movieid == "0000000002": pass
            else:
                self.assertEquals(movie.movieid, "0000000003")
                self.assertEquals(movie.mname, u"狗十三")


        MovieModel.where(movieid="0000000001").update(mname=u"海的女儿")
        movie = MovieModel.where(movieid="0000000001").select().next()

        self.assertEquals(movie.mname, u"海的女儿")


        movies = MovieModel.where(introduction=u"很好看的电影").limit(2).select()

        cnt = 0
        for movie in movies: cnt += 1
        self.assertEquals(1, cnt)


        cnt = MovieModel.where(introduction=u"很好看的电影").count()

        self.assertEquals(1, cnt)


class TestEditorModel(unittest.TestCase):

    def setUp(self):
        if list(EditorModel.where(ediid="1111100001").select()) == []:
            create_editor_instance(
                "1111100001",
                u"编剧",
                u"男",
                56,
                u"中国",
                178,
                u"沈阳市沈河区",
                u"汉族",
                u"处女座"
            )
       
    def rm_tearDown(self):
        execute_raw_sql("truncate table Editor;")

    def test_main(self):
        editor = EditorModel.where(ediid="1111100001").select().next()

        self.assertEquals(editor.ediname, u"编剧")


        editors = EditorModel.where().select()

        for editor in editors:
            if editor.ediid == "1111100002": pass
            elif editor.ediid == "1111100003": pass
            else:
                self.assertEquals(editor.ediname, u"编剧")


        EditorModel.where(ediid="1111100001").update(ediname=u"罗钥轩")
        editor = EditorModel.where(ediid="1111100001").select().next()

        self.assertEquals(editor.ediid, "1111100001")
        self.assertEquals(editor.ediname, u"罗钥轩")


        editors = EditorModel.where(edicountry=u"中国").limit(2).select()

        cnt = len(list(editors))
        self.assertEquals(1, cnt)


        cnt = EditorModel.where(edicountry=u"中国").count()

        self.assertEquals(1, cnt)


class TestActorModel(unittest.TestCase):

    def setUp(self):
        if list(ActorModel.where(actorid="2222200001").select()) == []:
            create_actor_instance(
                "2222200001",
                u"师毓洁",
                u"女",
                19,
                u"中国",
                169,
                u"陕西省",
                u"汉族",
                u"双子座"
            )

    def rm_tearDown(self):
        execute_raw_sql("truncate table Actor;")

    def test_main(self):
        actor = ActorModel.where(actorid="2222200001").select().next()

        self.assertEquals(actor.actorname, u"师毓洁")


        actors = ActorModel.where().select()

        for actor in actors:
            if actor.actorid == "2222200002": pass
            elif actor.actorid == "2222200003": pass
            else:
                self.assertEquals(actor.actorname, u"师毓洁")


        ActorModel.where(actorid="2222200001").update(actorname=u"罗钥轩")
        actor = ActorModel.where(actorid="2222200001").select().next()

        self.assertEquals(actor.actorid, "2222200001")
        self.assertEquals(actor.actorname, u"罗钥轩")


        actors = ActorModel.where(constellation=u"双子座").limit(2).select()

        cnt = 0
        for actor in actors: cnt += 1
        self.assertEquals(1, cnt)


        cnt = ActorModel.where(constellation=u"双子座").count()

        self.assertEquals(1, cnt)


class TestDirectorModel(unittest.TestCase):

    def setUp(self):
        if list(DirectorModel.where(dirtorid="3333300001").select()) == []:
            create_director_instance(
                "3333300001",
                u"温子仁",
                u"男",
                42,
                u"马来西亚",
                168,
                u"马来西亚-砂拉越州-古晋",
                u"汉族",
                u"双鱼座"
            )
       
    def rm_tearDown(self):
        execute_raw_sql("truncate table Director;")

    def test_main(self):
        director = DirectorModel.where(dirtorid="3333300001").select().next()

        self.assertEquals(director.dirorname, u"温子仁")


        directors = DirectorModel.where().select()

        for director in directors:
            if director.dirtorid == "3333300002": pass
            elif director.dirtorid == "3333300003": pass
            else:
                self.assertEquals(director.dirorname, u"温子仁")


        DirectorModel.where(dirtorid="3333300001").update(dirorname=u"罗钥轩")
        director = DirectorModel.where(dirtorid="3333300001").select().next()

        self.assertEquals(director.dirtorid, "3333300001")
        self.assertEquals(director.dirorname, u"罗钥轩")


        directors = DirectorModel.where(dirage=42).select()

        cnt = len(list(directors))
        self.assertEquals(1, cnt)


        cnt = DirectorModel.where(dirage=42).count()

        self.assertEquals(1, cnt)


"""
class TestMovActModel(unittest.TestCase):
    
    def setUp(self):
        if list(MovActModel.where(movieid="0000000001").select()) == []:
            create_movact_instance(
                "0000000001",
                "2222200001",
                 u"智障"
            )
       
    def rm_tearDown(self):
        execute_raw_sql("truncate table MovAct;")

    def test_main(self):
        movact = MovActModel.where(actorid="2222200001").select().next()

        self.assertEquals(movact.character, u"智障")

 
        movacts = MovActModel.where().select()

        for movact in movacts:
            if movact.actorid == "2222200002": pass
            elif movact.actorid == "2222200003": pass
            else:
                self.assertEquals(movact.character, u"智障")


        MovActModel.where(actorid="2222200001").update(character=u"海王")
        movacts = MovActModel.where(actorid="2222200001").select().next()

        self.assertEquals(movact.actorid, "2222200001")
        self.assertEquals(movact.character, u"海王")


        movacts = MovActModel.where(character=u"智障").limit(2).select()

        cnt = 0
        for movact in movacts: cnt += 1
        self.assertEquals(1, cnt)


        cnt = MovActModel.where(character=u"智障").count()

        self.assertEquals(1, cnt)
"""


class TestMEModel(unittest.TestCase):
    
    def setUp(self):
        if list(MEModel.where(movieid="0000000001").select()) == []:
            create_me_instance(
                "0000000001",
                "1111100001"
            )
       
    def rm_tearDown(self):
        execute_raw_sql("truncate table ME;")

    def test_main(self):
        me = MEModel.where(movieid="0000000001").select().next()

        self.assertEquals(me.ediid, "1111100001")

    
        mes = MEModel.where().select()

        for me in mes:
            if me.movieid == "0000000002": pass
            elif me.movieid == "0000000003": pass
            else:
                self.assertEquals(me.ediid, "1111100001")

        """
        MEModel.where(movieid="0000000001").update(ediid="1111100011")
        mes = MEModel.where(movieid="0000000001").select().next()

        self.assertEquals(me.movieid, "0000000001")
        self.assertEquals(me.ediid, "1111100001")
        """

        mes = MEModel.where(movieid="0000000001").limit(2).select()

        cnt = 0
        for me in mes: cnt += 1
        self.assertEquals(1, cnt)


        cnt = MEModel.where(movieid="0000000001").count()

        self.assertEquals(1, cnt)


class TestMDModel(unittest.TestCase):
    
    def setUp(self):
        if list(MDModel.where(movieid="0000000001").select()) == []:
            create_md_instance(
                "0000000001",
                "3333300001"
            )
       
    def rm_tearDown(self):
        execute_raw_sql("truncate table MD;")

    def test_main(self):
        md = MDModel.where(movieid="0000000001").select().next()

        self.assertEquals(md.dirtorid, "3333300001")

   
        mds = MDModel.where().select()

        for md in mds:
            if md.movieid == "0000000002": pass
            elif md.movieid == "0000000003": pass
            else:
                self.assertEquals(md.dirtorid, "3333300001")

        """
        MDModel.where(movieid="0000000001").update(dirtorid="1111100011")
        mds = MDModel.where(movieid="0000000001").select().next()

        self.assertEquals(md.movieid, "0000000001")
        self.assertEquals(md.dirtorid, "3333300001")
        """
   
        mds = MDModel.where(movieid="0000000001").limit(2).select()

        cnt = 0
        for md in mds: cnt += 1
        self.assertEquals(1, cnt)

    
        cnt = MDModel.where(movieid="0000000001").count()

        self.assertEquals(1, cnt)


if __name__ == "__main__":
    for table in ['User', 'Movie', 'Score', 'Editor', 'Director', 'Actor', 'MovAct', 'MD', 'ME']:
        execute_raw_sql("truncate table " + table + ";")
    unittest.main()
