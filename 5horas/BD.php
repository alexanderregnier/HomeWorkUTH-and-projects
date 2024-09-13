<?php

$servidor="localhost";//127.0.0.1
$BD="app";
$usuario="root";    
$contraseña="";

try{
    $conexion= new PDO("mysql:host=$servidor;dbname=$BD",$usuario,$contraseña);
}catch(exception $ex){
    echo $ex->getMessage();
}


?>