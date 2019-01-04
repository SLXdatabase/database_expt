-- MySQL dump 10.16  Distrib 10.1.37-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: dodo
-- ------------------------------------------------------
-- Server version	10.1.37-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Actor`
--

DROP TABLE IF EXISTS `Actor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Actor` (
  `actorid` char(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `actorname` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `sex` char(1) COLLATE utf8mb4_unicode_ci NOT NULL,
  `age` int(11) NOT NULL,
  `country` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `height` int(11) NOT NULL,
  `birthplace` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `nation` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `constellation` char(3) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`actorid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Actor`
--

LOCK TABLES `Actor` WRITE;
/*!40000 ALTER TABLE `Actor` DISABLE KEYS */;
/*!40000 ALTER TABLE `Actor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Director`
--

DROP TABLE IF EXISTS `Director`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Director` (
  `dirtorid` char(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `dirorname` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `dirsex` char(1) COLLATE utf8mb4_unicode_ci NOT NULL,
  `dirage` int(11) NOT NULL,
  `dircountry` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `dirheight` int(11) NOT NULL,
  `dirbirthplace` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `dirnation` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `dirconstellation` char(3) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`dirtorid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Director`
--

LOCK TABLES `Director` WRITE;
/*!40000 ALTER TABLE `Director` DISABLE KEYS */;
/*!40000 ALTER TABLE `Director` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Editor`
--

DROP TABLE IF EXISTS `Editor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Editor` (
  `ediid` char(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ediname` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `edisex` char(1) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ediage` int(11) NOT NULL,
  `edicountry` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ediheight` int(11) NOT NULL,
  `edibirthplace` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `edination` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ediconstellation` varchar(3) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`ediid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Editor`
--

LOCK TABLES `Editor` WRITE;
/*!40000 ALTER TABLE `Editor` DISABLE KEYS */;
/*!40000 ALTER TABLE `Editor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MD`
--

DROP TABLE IF EXISTS `MD`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MD` (
  `movieid` char(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `dirtorid` char(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`movieid`,`dirtorid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MD`
--

LOCK TABLES `MD` WRITE;
/*!40000 ALTER TABLE `MD` DISABLE KEYS */;
/*!40000 ALTER TABLE `MD` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ME`
--

DROP TABLE IF EXISTS `ME`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ME` (
  `movieid` char(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ediid` char(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`movieid`,`ediid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ME`
--

LOCK TABLES `ME` WRITE;
/*!40000 ALTER TABLE `ME` DISABLE KEYS */;
/*!40000 ALTER TABLE `ME` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MovAct`
--

DROP TABLE IF EXISTS `MovAct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MovAct` (
  `movieid` char(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `actorid` char(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `character` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MovAct`
--

LOCK TABLES `MovAct` WRITE;
/*!40000 ALTER TABLE `MovAct` DISABLE KEYS */;
/*!40000 ALTER TABLE `MovAct` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Movie`
--

DROP TABLE IF EXISTS `Movie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Movie` (
  `movieid` char(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `mname` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `director` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `editor` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `actor` varchar(300) COLLATE utf8mb4_unicode_ci NOT NULL,
  `mtype` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `countryOrLocation` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `language` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  `duration` int(11) NOT NULL,
  `othername` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `IMDb` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `introduction` varchar(300) COLLATE utf8mb4_unicode_ci NOT NULL,
  `allActors` varchar(1000) COLLATE utf8mb4_unicode_ci NOT NULL,
  `numOfEvaluator` int(11) NOT NULL,
  `star5` int(11) NOT NULL,
  `star4` int(11) NOT NULL,
  `star3` int(11) NOT NULL,
  `star2` int(11) NOT NULL,
  `star1` int(11) NOT NULL,
  PRIMARY KEY (`movieid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Movie`
--

LOCK TABLES `Movie` WRITE;
/*!40000 ALTER TABLE `Movie` DISABLE KEYS */;
/*!40000 ALTER TABLE `Movie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Score`
--

DROP TABLE IF EXISTS `Score`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Score` (
  `userid` char(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `movieid` char(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Mov_movieid` char(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Use_userid` char(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `comDate` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  `value` int(11) NOT NULL,
  `content` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `watched` smallint(6) NOT NULL,
  `star` int(11) NOT NULL,
  PRIMARY KEY (`movieid`,`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Score`
--

LOCK TABLES `Score` WRITE;
/*!40000 ALTER TABLE `Score` DISABLE KEYS */;
/*!40000 ALTER TABLE `Score` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User` (
  `userid` char(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `username` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `record` varchar(300) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `permission` smallint(6) NOT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-01-08  8:35:32
