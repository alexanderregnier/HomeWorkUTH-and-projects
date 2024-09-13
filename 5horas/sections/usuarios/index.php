<?php
include("../../BD.php");    

if(isset($_GET['txtID'])){
    $txtID=(isset($_GET['txtID']))?$_GET['txtID']:"";

    $sentencia=$conexion->prepare("DELETE FROM tbl_usuarios WHERE id=:id");
    $sentencia->bindParam(":id", $txtID);
    $sentencia->execute();
    $mensaje = "Registro eliminado";
    header("Location: index.php?mensaje=" . urlencode($mensaje));
    exit;
}

// Seleccionamos todos los usuarios
$sentencia=$conexion->prepare("SELECT * FROM tbl_usuarios");
$sentencia->execute();
$lista_tbl_Usuarios=$sentencia->fetchAll(PDO::FETCH_ASSOC);

?>   
<?php include("../../templates/header.php"); ?>
<br>
<h4>Usuarios</h4>
<div class="card">
    <div class="card-header">
        <a name="" id="" class="btn btn-primary" href="crear.php" role="button">Agregar registro</a>
    </div>
    <div class="card-body">
        <div class="table-responsive-sm">
            <table class="table" id="tabla_id">
                <thead>
                    <tr>
                        <th scope="cool">Id</th>
                        <th scope="cool">Nombre del Usuario</th>
                        <th scope="cool">contrasena</th>
                        <th scope="cool">Correo</th>
                        <th scope="cool">Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    <?php foreach ($lista_tbl_Usuarios as $registro) { ?>
                        <tr class="">
                            <td scope="row"><?php echo $registro['id'];?></td>
                            <td><?php echo $registro['usuario'];?></td>
                            <td>********</td>
                            <td><?php echo $registro['correo'];?></td>
                            <td>
                                <a href="editar.php?txtID=<?php echo $registro['id']; ?>" class="btn btn-info">Editar</a>
                                |
                                <a href="javascript:borrar(<?php echo $registro['id']; ?>);" class="btn btn-danger">Eliminar</a>
                            </td>
                        </tr>
                    <?php } ?>
                </tbody>
            </table>
        </div>
    </div>
</div>
    
<?php include("../../templates/footer.php"); ?>
