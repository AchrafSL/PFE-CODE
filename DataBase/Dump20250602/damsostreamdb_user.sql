-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: damsostreamdb
-- ------------------------------------------------------
-- Server version	8.0.36

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

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `idCli` int NOT NULL AUTO_INCREMENT,
  `Email` char(60) DEFAULT NULL,
  `Password` char(60) DEFAULT NULL,
  `FirstName` char(32) DEFAULT NULL,
  `LastName` char(32) DEFAULT NULL,
  `status` char(30) DEFAULT 'unverified',
  `role` char(30) DEFAULT 'client',
  `Date_Joined` datetime DEFAULT NULL,
  `whatsapp` char(30) DEFAULT NULL,
  `pfpName` char(255) DEFAULT 'user583abc_1649114257.png',
  PRIMARY KEY (`idCli`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (2,'achraf.salimi@uit.ac.ma','Salimi@01','Salimi','UIT','verified','admin','2024-04-25 14:32:16','+212611223344','achraf.salimi@uit.ac.ma_Salimi.png'),(3,'lilnavincisa2022@gmail.com','Salimi@01','Linanvinci','SL','unverified','employee','2024-04-28 16:33:40','','lilnavincisa2022@gmail.com_Linanvinci.png'),(8,'thenewachraf2020@gmail.com','dadadqdq01@A','Salimi','Salimiiiiii','unverified','client','2024-05-30 14:38:09','0676384393','thenewachraf2020@gmail.com_Salimi.png'),(9,'dkhadhak2022@gmail.com','2022@gmailA','dakdha','kalfkla','unverified','client','2024-05-30 14:46:11','0676384393','user583abc_1649114257.png'),(10,'dadagf@gmail.com','Aqqq22##@','dafa','gaga','unverified','client','2024-05-30 14:48:27','+212676384393','user583abc_1649114257.png'),(13,'iroh25fi@gmail.com','12345678aA!','iroh','Mekawi','unverified','client','2025-01-22 16:18:54','+12689814810414','user583abc_1649114257.png'),(14,'iroh25fire@gmail.com','Aa123~1!11kj','fafas','rwqreq','unverified','client','2025-01-22 16:19:49','','user583abc_1649114257.png');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-02  9:53:50
