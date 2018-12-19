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
   `language`           varchar(20)                    not null,
   `date`               varchar(15)                    not null,
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
   constraint AK_MOVIE_MOVIE unique (movieid)
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
   `value`              integer                        not null,
   content              varchar(200)                   not null,
   watched              smallint                       not null,
   star                 integer                        not null,
   constraint PK_SCORE primary key (movieid, userid)
);

/*==============================================================*/
/* Table: "User"                                                */
/*==============================================================*/
create table `User` 
(
   userid               char(10)                       not null,
   username             varchar(30)                    not null,
   `password`           varchar(30)                    not null,
   record               varchar(300)                   null,
   permission           smallint                       not null,
   constraint PK_USER primary key (userid)
);
