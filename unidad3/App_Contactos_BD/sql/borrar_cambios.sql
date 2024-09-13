-- --------------------------------------------------------
-- Este script BORRA los cambios hechos por el script "info_db.sql".
-- --------------------------------------------------------

USE `info_db`;
DROP DATABASE `info_db`;

DROP USER 'contactos_user'@'localhost';
FLUSH PRIVILEGES;
SHOW DATABASES;
