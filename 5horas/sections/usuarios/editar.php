<?php
include("../../BD.php");    

if(isset($_GET['txtID'])){

    $txtID=(isset($_GET['txtID']))?$_GET['txtID']:"";

    $sentencia=$conexion->prepare("SELECT * FROM tbl_usuarios WHERE id=:id");
    $sentencia->bindParam(":id", $txtID);
    $sentencia->execute();

    $registro=$sentencia->fetch(PDO::FETCH_LAZY);
    $usuario=$registro["usuario"];
    $contrasena=$registro["contrasena"];
    $correo=$registro["correo"];
}

if($_POST){
    // Recolectamos los datos del método POST
    $usuario = isset($_POST["usuario"]) ? $_POST["usuario"] : "";
    $txtID = isset($_POST["txtID"]) ? $_POST["txtID"] : "";

    // Actualización
    $sentencia = $conexion->prepare("UPDATE tbl_usuarios SET usuario = :usuario, contrasena = :contrasena, correo = :correo WHERE id = :id");

    // Asignando los valores que vienen del método POST
    $sentencia->bindParam(":usuario", $usuario);
    $sentencia->bindParam(":contrasena", $contrasena);
    $sentencia->bindParam(":correo", $correo);
    $sentencia->bindParam(":id", $txtID);
    $sentencia->execute();
    $mensaje = "Registro Actualizado";
    header("Location: index.php?mensaje=" . urlencode($mensaje));
    exit;
}

?>   
<?php include("../../templates/header.php"); ?>

<div class="card">
    <div class="card-header">Datos del usuario</div>
    <div class="card-body">
        <form action="" method="post" enctype="multipart/form-data">

            <div class="mb-3">
                <label for="txtID" class="form-label">id:</label>
                <input
                    value="<?php echo $txtID;?>"
                    type="text"
                    class="form-control"
                    name="txtID"
                    id="txtID"
                    readonly
                    aria-describedby="helpId"
                    placeholder="id"
                />
            </div>
            
            <div class="mb-3">
                <label for="usuario" class="form-label">Nombre del usuario:</label>
                <input
                    value="<?php echo $usuario;?>"
                    type="text" 
                    class="form-control" name="usuario" id="usuario" aria-describedby="helpId" placeholder="Nombre del puesto" />
            </div>

            <div class="mb-3">
                <label for="contrasena" class="form-label">contraseña:</label>
                <input
                    value="<?php echo $contrasena;?>"
                    type="password" 
                    class="form-control" name="contrasena" id="contrasena" placeholder="contraseña" />
            </div>

            <div class="mb-3">
                <label for="correo" class="form-label">correo:</label>
                <input
                    value="<?php echo $correo;?>"
                    type="email" 
                    class="form-control" name="correo" id="correo" aria-describedby="helpId" placeholder="Nombre del puesto" />
            </div>
            
            <button type="submit" class="btn btn-primary">Actualizar</button>
            |
            <a name="" id="" class="btn btn-primary" href="index.php" role="button">Cancelar</a>
        </form>
    </div>
    <div class="card-footer text-muted"></div>
</div>

<?php include("../../templates/footer.php"); ?>
