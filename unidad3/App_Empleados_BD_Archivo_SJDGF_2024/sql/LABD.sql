-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.28-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.2.0.6213
-- --------------------------------------------------------






/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para labd
DROP DATABASE IF EXISTS `labd`;
CREATE DATABASE IF NOT EXISTS `labd` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `labd`;

-- Volcando estructura para tabla labd.empleados
DROP TABLE IF EXISTS `empleados`;
CREATE TABLE IF NOT EXISTS `empleados` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `apellido_pat` varchar(50) NOT NULL,
  `apellido_mat` varchar(50) NOT NULL,
  `correo` varchar(50) DEFAULT NULL,
  `puesto` varchar(50) DEFAULT NULL,
  `fecha_ingreso` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_empleados_puestos` (`puesto`),
  CONSTRAINT `FK_empleados_puestos` FOREIGN KEY (`puesto`) REFERENCES `puestos` (`nombre_puesto`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla labd.empleados: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `empleados` DISABLE KEYS */;
INSERT INTO `empleados` (`id`, `nombre`, `apellido_pat`, `apellido_mat`, `correo`, `puesto`, `fecha_ingreso`) VALUES
	(1, 'José', 'Padilla', 'Duarte', 'jopadu@gmail.com', 'Programador Jr', '2002-09-02'),
	(2, 'Tony', 'Stark', '', 'tony@starkindustries.com', 'Administrador de la BD', '2024-03-08');
/*!40000 ALTER TABLE `empleados` ENABLE KEYS */;

-- Volcando estructura para tabla labd.puestos
DROP TABLE IF EXISTS `puestos`;
CREATE TABLE IF NOT EXISTS `puestos` (
  `nombre_puesto` varchar(50) NOT NULL,
  PRIMARY KEY (`nombre_puesto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla labd.puestos: ~6 rows (aproximadamente)
/*!40000 ALTER TABLE `puestos` DISABLE KEYS */;
INSERT INTO `puestos` (`nombre_puesto`) VALUES
	('Administrador de la BD'),
	('Guardia de Seguridad'),
	('Ingeniero de Pruebas'),
	('Lider de proyectos'),
	('Programador Jr'),
	('Programador Sr');
/*!40000 ALTER TABLE `puestos` ENABLE KEYS */;

-- Volcando estructura para tabla labd.usuarios
DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE IF NOT EXISTS `usuarios` (
  `nombre` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `correo` varchar(50) NOT NULL,
  PRIMARY KEY (`nombre`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla labd.usuarios: ~3 rows (aproximadamente)
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` (`nombre`, `password`, `correo`) VALUES
	('irma', '0c12278389532e91c601af4c8adef7fc', 'irmabarens@gmail.com'),
	('jopadu', 'a709909b1ea5c2bee24248203b1728a5', 'jopadu@gmail.com'),
	('tic', 'e10adc3949ba59abbe56e057f20f883e', 'tic@uthermosillo.edu.mx');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;

SHOW DATABASES;
SELECT * FROM labd.usuarios;