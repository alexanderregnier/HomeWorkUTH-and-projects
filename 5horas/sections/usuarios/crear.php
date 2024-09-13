<?php
include("../../BD.php");    

if($_POST){
    // Recolectamos los datos del método POST
    $Usuario = isset($_POST["NombreUsuario"]) ? $_POST["NombreUsuario"] : "";
    $contrasena = isset($_POST["contrasena"]) ? $_POST["contrasena"] : "";
    $Correo = isset($_POST["Correo"]) ? $_POST["Correo"] : "";

    // Inserción
    $sentencia = $conexion->prepare("INSERT INTO tbl_usuarios (usuario, contrasena, correo) VALUES (:usuario, :contrasena, :correo)");

    // Asignando los valores que vienen del método POST
    $sentencia->bindParam(":usuario", $Usuario);
    $sentencia->bindParam(":contrasena", $contrasena);
    $sentencia->bindParam(":correo", $Correo);
    $sentencia->execute();
    $mensaje = "Registro Creado";
    header("Location: index.php?mensaje=" . urlencode($mensaje));
    exit;
}
?>
<?php include("../../templates/header.php"); ?>

<div class="card">
    <div class="card-header">Agregar datos del empleado</div>
    <div class="card-body">
    
        <form action="" method="post" enctype="multipart/form-data">
            <div class="mb-3">
                <label for="NombreUsuario" class="form-label">Nombre del Usuario</label>
                <input
                    type="text"
                    class="form-control"
                    name="NombreUsuario"
                    id="NombreUsuario"
                    aria-describedby="helpId"
                    placeholder="Nombre del usuario"
                />
            </div>

            <div class="mb-3">
                <label for="contrasena" class="form-label">Contraseña</label>
                <input
                    type="password"
                    class="form-control"
                    name="contrasena"
                    id="contrasena"
                    aria-describedby="helpId"
                    placeholder="Escriba su contraseña"
                />
            </div>

            <div class="mb-3">
                <label for="Correo" class="form-label">Correo</label>
                <input
                    type="email"
                    class="form-control"
                    name="Correo"
                    id="Correo"
                    aria-describedby="helpId"
                    placeholder="Escribe tu Correo"
                />
            </div>
            
            <button type="submit" class="btn btn-primary">Agregar registro</button>
            <a name="" id="" class="btn btn-primary" href="index.php" role="button">Cancelar</a>

        </form>
    </div>
    <div class="card-footer text-muted"></div>
</div>

<?php include("../../templates/footer.php"); ?>
