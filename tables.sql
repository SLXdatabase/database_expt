if exists(select 1 from sys.sysforeignkey where role='FK_SCORE_SM_MOVIE') then
    alter table Score
       delete foreign key FK_SCORE_SM_MOVIE
end if;

if exists(select 1 from sys.sysforeignkey where role='FK_SCORE_US_USER') then
    alter table Score
       delete foreign key FK_SCORE_US_USER
end if;

if exists(select 1 from sys.sysforeignkey where role='FK_UM_UM_USER') then
    alter table UM
       delete foreign key FK_UM_UM_USER
end if;

if exists(select 1 from sys.sysforeignkey where role='FK_UM_UM2_MOVIE') then
    alter table UM
       delete foreign key FK_UM_UM2_MOVIE
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='Movie_AK'
     and t.table_name='Movie'
) then
   drop index Movie.Movie_AK
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='Movie_PK'
     and t.table_name='Movie'
) then
   drop index Movie.Movie_PK
end if;

if exists(
   select 1 from sys.systable 
   where table_name='Movie'
     and table_type in ('BASE', 'GBL TEMP')
) then
    drop table Movie
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='SM_FK'
     and t.table_name='Score'
) then
   drop index Score.SM_FK
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='US_FK'
     and t.table_name='Score'
) then
   drop index Score.US_FK
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='Score_PK'
     and t.table_name='Score'
) then
   drop index Score.Score_PK
end if;

if exists(
   select 1 from sys.systable 
   where table_name='Score'
     and table_type in ('BASE', 'GBL TEMP')
) then
    drop table Score
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='UM2_FK'
     and t.table_name='UM'
) then
   drop index UM.UM2_FK
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='UM_FK'
     and t.table_name='UM'
) then
   drop index UM.UM_FK
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='UM_PK'
     and t.table_name='UM'
) then
   drop index UM.UM_PK
end if;

if exists(
   select 1 from sys.systable 
   where table_name='UM'
     and table_type in ('BASE', 'GBL TEMP')
) then
    drop table UM
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='User_PK'
     and t.table_name='User'
) then
   drop index "User".User_PK
end if;

if exists(
   select 1 from sys.systable 
   where table_name='User'
     and table_type in ('BASE', 'GBL TEMP')
) then
    drop table "User"
end if;

/*==============================================================*/
/* Table: Movie                                                 */
/*==============================================================*/
create table Movie 
(
   movieid              char(10)                       not null,
   mname                varchar(30)                    not null,
   director             varchar(100)                   not null,
   editor               varchar(100)                   not null,
   actor                varchar(300)                   not null,
   mtype                varchar(50)                    not null,
   countryOrLocation    varchar(100)                   not null,
   language             varchar(20)                    not null,
   "date"               varchar(15)                    not null,
   duration             integer                        not null,
   othername            varchar(200)                   null,
   IMDb                 varchar(30)                    not null,
   introduction         varchar(300)                   not null,
   allActors            varchar(1000)                  not null,
   numOfEvaluator       integer                        not null,
   5star                integer                        not null,
   4star                integer                        not null,
   3star                integer                        not null,
   2star                integer                        not null,
   1star                integer                        not null,
   constraint PK_MOVIE primary key (movieid),
   constraint AK_MOVIE_MOVIE unique ()
);

/*==============================================================*/
/* Index: Movie_PK                                              */
/*==============================================================*/
create unique index Movie_PK on Movie (
movieid ASC
);

/*==============================================================*/
/* Index: Movie_AK                                              */
/*==============================================================*/
create unique index Movie_AK on Movie (

);

/*==============================================================*/
/* Table: Score                                                 */
/*==============================================================*/
create table Score 
(
   userid               char(10)                       not null,
   movieid              char(10)                       not null,
   Mov_movieid          char(10)                       null,
   Use_userid           char(10)                       null,
   comDate              varchar(15)                    not null,
   value                integer                        not null,
   content              varchar(200)                   not null,
   watched              smallint                       not null,
   star                 integer                        not null,
   constraint PK_SCORE primary key (movieid, userid)
);

/*==============================================================*/
/* Index: Score_PK                                              */
/*==============================================================*/
create unique index Score_PK on Score (
movieid ASC,
userid ASC
);

/*==============================================================*/
/* Index: US_FK                                                 */
/*==============================================================*/
create index US_FK on Score (
Use_userid ASC
);

/*==============================================================*/
/* Index: SM_FK                                                 */
/*==============================================================*/
create index SM_FK on Score (
Mov_movieid ASC
);

/*==============================================================*/
/* Table: UM                                                    */
/*==============================================================*/
create table UM 
(
   userid               char(10)                       not null,
   movieid              char(10)                       not null,
   constraint PK_UM primary key clustered (userid, movieid)
);

/*==============================================================*/
/* Index: UM_PK                                                 */
/*==============================================================*/
create unique clustered index UM_PK on UM (
userid ASC,
movieid ASC
);

/*==============================================================*/
/* Index: UM_FK                                                 */
/*==============================================================*/
create index UM_FK on UM (
userid ASC
);

/*==============================================================*/
/* Index: UM2_FK                                                */
/*==============================================================*/
create index UM2_FK on UM (
movieid ASC
);

/*==============================================================*/
/* Table: "User"                                                */
/*==============================================================*/
create table "User" 
(
   userid               char(10)                       not null,
   username             varchar(30)                    not null,
   password             varchar(30)                    not null,
   record               varchar(300)                   null,
   permission           smallint                       not null,
   constraint PK_USER primary key (userid)
);

/*==============================================================*/
/* Index: User_PK                                               */
/*==============================================================*/
create unique index User_PK on "User" (
userid ASC
);

alter table Score
   add constraint FK_SCORE_SM_MOVIE foreign key (Mov_movieid)
      references Movie (movieid)
      on update restrict
      on delete restrict;

alter table Score
   add constraint FK_SCORE_US_USER foreign key (Use_userid)
      references "User" (userid)
      on update restrict
      on delete restrict;

alter table UM
   add constraint FK_UM_UM_USER foreign key (userid)
      references "User" (userid)
      on update restrict
      on delete restrict;

alter table UM
   add constraint FK_UM_UM2_MOVIE foreign key (movieid)
      references Movie (movieid)
      on update restrict
      on delete restrict;
