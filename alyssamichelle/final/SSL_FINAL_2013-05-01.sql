# ************************************************************
# Sequel Pro SQL dump
# Version 4004
#
# http://www.sequelpro.com/
# http://code.google.com/p/sequel-pro/
#
# Host: 127.0.0.1 (MySQL 5.5.29)
# Database: SSL_FINAL
# Generation Time: 2013-05-02 03:16:39 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table Dictionary
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Dictionary`;

CREATE TABLE `Dictionary` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `word` varchar(255) DEFAULT NULL,
  `definition` text,
  `trans_word` varchar(255) DEFAULT NULL,
  `trans_definition` text,
  `trans_language` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `Dictionary` WRITE;
/*!40000 ALTER TABLE `Dictionary` DISABLE KEYS */;

INSERT INTO `Dictionary` (`id`, `word`, `definition`, `trans_word`, `trans_definition`, `trans_language`)
VALUES
	(1,'hell','hell','hell','hell','hell'),
	(2,'text','definition','trans_word','trans_definition','toLang'),
	(3,'text','','','',NULL),
	(4,'text','','','',NULL),
	(5,'text','','','',''),
	(6,'text','','','',''),
	(7,'text','','','','deu'),
	(8,'text','','','','deu'),
	(9,'text','','','','deu'),
	(10,'coffee','value is not being set by search def in WordService class','value is not being set by search def in WordService class','value is not being set by search def in WordService class','deu');

/*!40000 ALTER TABLE `Dictionary` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
