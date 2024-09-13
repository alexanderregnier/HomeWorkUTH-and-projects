<?php
include("../../BD.php"); 

if(isset($_GET['txtID'])) {
    $txtID = $_GET['txtID'] ?? "";

    // Buscar archivos asociados al empleado
    $sentencia = $conexion->prepare("SELECT foto, cv FROM tbl_empleados WHERE id=:id");
    $sentencia->bindParam(":id", $txtID);
    $sentencia->execute();
    $RegistroRecuperado = $sentencia->fetch(PDO::FETCH_LAZY);

    // Eliminar archivos si existen
    if(isset($RegistroRecuperado["foto"]) && !empty($RegistroRecuperado["foto"])) {
        $foto_path = "./" . $RegistroRecuperado["foto"];
        if(file_exists($foto_path)) {
            unlink($foto_path);
        }
    }
    if(isset($RegistroRecuperado["cv"]) && !empty($RegistroRecuperado["cv"])) {
        $cv_path = "./" . $RegistroRecuperado["cv"];
        if(file_exists($cv_path)) {
            unlink($cv_path);
        }
    }

    // Eliminar empleado de la base de datos
    $sentencia = $conexion->prepare("DELETE FROM tbl_empleados WHERE id=:id");
    $sentencia->bindParam(":id", $txtID);
    $sentencia->execute();
    $mensaje = "Registro eliminado";
    header("Location: index.php?mensaje=" . urlencode($mensaje));
    exit;
}

// Obtener lista de empleados
$sentencia = $conexion->prepare("SELECT *, (
    SELECT nombredepuesto FROM tbl_puestos WHERE tbl_puestos.id = tbl_empleados.idpuesto LIMIT 1
) AS puesto FROM tbl_empleados");
$sentencia->execute();
$lista_tbl_empleados = $sentencia->fetchAll(PDO::FETCH_ASSOC);
?>

<?php include("../../templates/header.php"); ?>
<br>
<h4>Empleados</h4>
<div class="card">
    <div class="card-header">
        <a name="" id="" class="btn btn-primary" href="crear.php" role="button">Agregar registro</a>
    </div>
    <div class="card-body">
        <div class="table-responsive-sm">
            <table class="table" id="tabla_id">
                <thead>
                    <tr>
                        <th scope="col">ID</th>
                        <th scope="col">Nombre</th>
                        <th scope="col">Foto</th>
                        <th scope="col">CV</th>
                        <th scope="col">Puesto</th>
                        <th scope="col">Fecha de ingreso</th>
                        <th scope="col">Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    <?php foreach ($lista_tbl_empleados as $registro) { ?>
                        <tr>
                            <td><?php echo $registro['id']; ?></td>
                            <td><?php echo $registro['nombres'] . ' ' . $registro['apellidoPA'] . ' ' . $registro['apellidoMA']; ?></td>
                            <td><img width="50" src="<?php echo $registro['foto']; ?>" class="img-fluid rounded" alt="" /></td>
                            <td><a href=<?php echo $registro['cv']; ?>><?php echo $registro['cv']; ?></a></td>
                            <td><?php echo $registro['puesto']; ?></td>
                            <td><?php echo $registro['fechadeingreso']; ?></td>
                            <td>
                                <a class="btn btn-primary" href="CartadeRecomendacion.php?txtID=<?php echo $registro['id']; ?>" role="button">carta</a>
                                |
                                <a class="btn btn-info" href="editar.php?txtID=<?php echo $registro['id']; ?>" role="button">Editar</a>
                                |
                                <a class="btn btn-danger" href="javascript:borrar(<?php echo $registro['id']; ?>);" role="button">Eliminar</a>
                            </td>
                        </tr>
                    <?php } ?>
                </tbody>
            </table>
        </div>
    </div>
</div>
<?php include("../../templates/footer.php"); ?>
