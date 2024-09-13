-- --------------------------------------------------------
-- Este script crea la BD directorio, la tabla contactos y el usuario dir_user
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


CREATE DATABASE IF NOT EXISTS `info_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;


USE `info_db`;


CREATE TABLE IF NOT EXISTS `contactos` (
  `nombre` varchar(50) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


/*!40000 ALTER TABLE `contactos` DISABLE KEYS */;
INSERT INTO `contactos` (`nombre`, `telefono`, `email`) VALUES
	('Irma Barens', '6621777888', 'irmabarens@gmail.com'),
	('Jose Padilla', '6621999888', 'jopadu@gmail.com'),
	('Tony Stark', '5097846622', 'tony@starkindustries.com');
/*!40000 ALTER TABLE `contactos` ENABLE KEYS */;


CREATE USER 'contactos_user'@'localhost' IDENTIFIED BY 'user1234';
GRANT USAGE ON *.* TO 'contactos_user'@'localhost';
GRANT EXECUTE, SELECT, SHOW VIEW, ALTER, ALTER ROUTINE, CREATE, CREATE ROUTINE, CREATE TEMPORARY TABLES, CREATE VIEW, DELETE, DROP, EVENT, INDEX, INSERT, REFERENCES, TRIGGER, UPDATE, LOCK TABLES  ON `info_db`.* TO 'contactos_user'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;


/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;


SHOW DATABASES;

SELECT User, Host, Password FROM mysql.user WHERE USER = 'contactos_user';
