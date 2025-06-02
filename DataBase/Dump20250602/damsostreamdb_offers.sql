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
-- Table structure for table `offers`
--

DROP TABLE IF EXISTS `offers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `offers` (
  `idOffer` int NOT NULL AUTO_INCREMENT,
  `description` text,
  `image_Name` varchar(255) DEFAULT 'default-product-image.png',
  `Offer_price` decimal(10,2) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `duration` int DEFAULT NULL,
  PRIMARY KEY (`idOffer`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `offers`
--

LOCK TABLES `offers` WRITE;
/*!40000 ALTER TABLE `offers` DISABLE KEYS */;
INSERT INTO `offers` VALUES (14,'Netflix account. \n\nWatch on Smart TVs, Playstation, Xbox, Chromecast, Apple TV, Blu-ray players, and more.\n\n\n\n Download your shows to watch offline\n\nSave your favorites easily and always have something to watch. Watch everywhere\n\n\n\nStream unlimited movies and TV shows on your phone, tablet, laptop, and TV.\n\n\n\n','Netflix accounts.jpg',40.00,'Netflix accounts',30),(15,'Spotify, audio streaming service that offers users access to music tracks, podcasts, and other media through a subscription model. It is a publicly traded company that was founded by Swedish entrepreneurs Daniel Ek and Martin Lorentzon in 2006. Spotify is headquartered in Stockholm and has more than a dozen other office locations worldwide.','Spotify Premium.png',70.00,'Spotify Premium',90),(16,'Prime Video offers a massive library of movies, series, and sports. Prime Video is home to more content than you might realize.  The membership gives access to all the perks of Amazon Prime (including free Two-Day Delivery on eligible items, and other benefits) plus the full library of content available through Prime Video. ','Amazon Prime.jpg',40.00,'Amazon Prime',30),(17,'Hulu is the leading and most comprehensive all-in-one premium streaming service that offers an expansive slate of live and on-demand entertainment, both in and outside the home, through a wide array of subscription options that give consumers ultimate control over their viewing experience.','Hulu Subscription.jpg',50.00,'Hulu Subscription',30),(18,'Crunchyroll, LLC, d/b/a Crunchyroll, formerly known as Funimation, is an American entertainment company owned by Tokyo-based Sony Group Corporation based in Coppell, a suburb of Dallas, Texas, focused on the distribution and licensing of anime, films, and television series.','Crunchyroll.jpg',40.00,'Crunchyroll',30),(19,'What is Snapchat+? As a Snapchat+ subscriber, you can get exclusive, experimental, and pre-release features! These features enhance and customize your Snapchat experience, enabling you to dive deeper into the parts of the app you use the most ? Plus, you can peep cool new features before anyone else!','Snapchat+.jpg',250.00,'Snapchat+',365),(20,'Adobe Creative Cloud refers to a bundle of more than 20 software applications that creators use to produce visual content for personal or professional use, including: Flyers, brochures, business cards, and infographics. Books of any length. Websites and apps.','Adobe Creative Cloud.png',500.00,'Adobe Creative Cloud',365),(21,'In Office 2021, you\'ll find new co-authoring features, inking tools, data types, functions, translation and editing tools, motion graphics, ease-of-use features, and so much more! Check out what\'s available to you today. Note: Some features listed below are not included in Office LTSC 2021 for commercial customers.','Office 2021.png',250.00,'Office 2021',365),(22,'Microsoft 365 is our cloud-powered productivity platform. With a subscription to Microsoft 365, you can get:\r\n\r\n\r\n\r\nThe latest productivity apps, such as Microsoft Teams, Word, Excel, PowerPoint, Outlook, OneDrive, and so much more.\r\n\r\n\r\n\r\nThe ability to install on PCs, Macs, tablets, and phones.\r\n\r\n\r\n\r\n1 TB of OneDrive cloud storage.\r\n\r\n\r\n\r\nFeature updates and upgrades not available anywhere else.','Office 365.png',200.00,'Office 365',365),(23,'The Duolingo language learning app is the world\'s most popular way to learn languages. The company\'s mission is to develop the best education in the world and make it universally available. Learning with Duolingo is fun, and research shows that it works!','duolingo plus.jpg',100.00,'duolingo plus',365),(24,'At Grammarly, we democratize great writing in English. We believe anyone can communicate effectively, efficiently, and persuasively with the right tools. Grammarly is the AI writing partner that helps people at every stage of the writing process, from blank page to final draft.','grammarly.png',100.00,'grammarly',365),(25,'NordVPN is the gateway to a secure and private access to the internet. It works by enveloping all of your online activities in a layer of encryption, while also hiding information about your virtual location.','NordVpn.jpg',40.00,'NordVpn',30),(26,'STARZPLAY allows you to watch anytime, anywhere on an iOS or Android device, supports Mac and Windows devices, and streams via Apple TV, Chromecast, a PS4 console or directly to most smart TVs.','StarzPlay.jpg',40.00,'StarzPlay',30),(27,'Orbit Showtime Network (OSN), branded as OSN Group is a multinational premium entertainment content company based in Dubai, serving the Middle East and North Africa (MENA).','oSn+.jpg',40.00,'oSn+',30),(28,'IPTV works by transmitting television content over an internet connection using the IP protocol. Content is delivered to users via broadband or internet connection, allowing them to stream TV shows, movies, and live events on various devices such as smart TVs, computers, smartphones, and set-top boxes.','Iptv.jpg',250.00,'Iptv',365),(29,'Apple One bundles up to six Apple subscriptions for one lower monthly price, including up to 2TB of iCloud+ storage. And with the Family plan or Premier plan, you can invite up to five other people to join — with private access on all of their devices. It\'s never been easier to get more.','Apple one Premier.png',300.00,'Apple one Premier',365),(30,'Apple One is a subscription which bundles a number of premium services provided by Apple Inc. into tiered packages, first offered in late 2020. The three tiers offered are Individual, Family, and Premier, with all three providing access to Apple Music, Apple TV+, Apple Arcade, and iCloud storage','Apple one.png',100.00,'Apple one',90),(31,'What is Disney+? Disney+ is the streaming home for entertainment from Disney, Pixar, Marvel, Star Wars, and National Geographic. From exclusive original content to the classic stories you know and love, Disney+ gives you access to thousands of titles for a high-quality viewing experience.','Disney+.jpg',40.00,'Disney+',1),(32,'NBA TV is an American sports-oriented pay television network owned by the National Basketball Association and operated by Warner Bros. Discovery through TNT Sports','NBA TV.jpg',40.00,'NBA TV',30),(33,'Canva is an online template editor app for creating social media graphics and presentations and merch and websites','Canva Pro.jpg',70.00,'Canva Pro',365),(34,'HBO Max is a streaming experience that brings together new and iconic series and films from HBO, Warner Bros., DC, Cartoon Network, and Max Originals. With over 13,000 hours of groundbreaking entertainment, there\'s something for everyone.','HBOmax.jpg',40.00,'HBOmax',30);
/*!40000 ALTER TABLE `offers` ENABLE KEYS */;
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

-- Dump completed on 2025-06-02 11:21:26
