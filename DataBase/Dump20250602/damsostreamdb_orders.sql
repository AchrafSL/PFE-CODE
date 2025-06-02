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
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `idOrder` int NOT NULL AUTO_INCREMENT,
  `idCli` int DEFAULT NULL,
  `StatOfTreatment` varchar(50) DEFAULT 'Pending Treatment',
  `PaymentStat` varchar(50) DEFAULT 'Pending Payment',
  `TotalPrice` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`idOrder`),
  KEY `idCli` (`idCli`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`idCli`) REFERENCES `user` (`idCli`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (6,2,'treated','Payed',250.00),(7,2,'treated','Payed',150.00),(8,2,'treated','Pending Payment',200.00),(9,2,'treated','Pending Payment',120.00),(22,2,'treated','Payed',301.00),(23,NULL,'treated','Payed',201.00),(24,NULL,'treated','Payed',120.00),(25,NULL,'treated','Payed',120.00),(26,2,'treated','Payed',120.00),(27,NULL,'treated','Payed',201.00),(28,NULL,'treated','Payed',120.00),(29,2,'treated','Payed',100.00),(30,2,'treated','Payed',110.00),(31,2,'treated','Pending Payment',150.00),(32,2,'treated','Pending Payment',150.00),(33,2,'treated','Payed',70.00),(34,8,'treated','Payed',110.00),(35,8,'treated','Pending Payment',40.00),(36,2,'treated','Pending Payment',40.00),(37,8,'treated','Payed',40.00),(38,2,'Pending Treatment','Pending Payment',110.00),(39,2,'Pending Treatment','Pending Payment',70.00),(40,2,'Pending Treatment','Pending Payment',80.00),(41,2,'Pending Treatment','Pending Payment',110.00),(42,8,'Pending Treatment','Pending Payment',70.00),(43,8,'Pending Treatment','Pending Payment',40.00),(44,2,'Pending Treatment','Pending Payment',40.00);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
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

-- Dump completed on 2025-06-02 11:21:20
