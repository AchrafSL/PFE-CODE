-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: damsodb-thenewachraf2020-50c1.j.aivencloud.com    Database: damsostreamdb
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '1b2af18d-3f3e-11f0-89ef-862ccfb04933:1-94';

--
-- Table structure for table `orderoffers`
--

DROP TABLE IF EXISTS `orderoffers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orderoffers` (
  `OrderOffers_Id` int NOT NULL AUTO_INCREMENT,
  `idOrder` int DEFAULT NULL,
  `idOffer` int DEFAULT NULL,
  PRIMARY KEY (`OrderOffers_Id`),
  KEY `idOrder` (`idOrder`),
  KEY `idOffer` (`idOffer`),
  CONSTRAINT `orderoffers_ibfk_1` FOREIGN KEY (`idOrder`) REFERENCES `orders` (`idOrder`),
  CONSTRAINT `orderoffers_ibfk_2` FOREIGN KEY (`idOffer`) REFERENCES `offers` (`idOffer`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orderoffers`
--

LOCK TABLES `orderoffers` WRITE;
/*!40000 ALTER TABLE `orderoffers` DISABLE KEYS */;
INSERT INTO `orderoffers` VALUES (37,30,15),(38,30,14),(39,31,15),(40,31,14),(41,31,18),(42,32,15),(43,32,14),(44,32,18),(45,33,15),(46,34,15),(47,34,16),(48,35,14),(49,36,14),(50,37,14),(51,38,15),(52,38,16),(53,39,15),(54,40,16),(55,40,14),(56,41,14),(57,41,33),(58,42,15),(59,43,14),(60,44,14);
/*!40000 ALTER TABLE `orderoffers` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-02 11:21:23
