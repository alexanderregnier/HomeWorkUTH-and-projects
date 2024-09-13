<?php
include("../../BD.php");    

if(isset($_GET['txtID'])){
    $txtID = (isset($_GET['txtID'])) ? $_GET['txtID'] : "";

    $sentencia = $conexion->prepare("SELECT * FROM tbl_empleados WHERE id = :id");
    $sentencia->bindParam(":id", $txtID);
    $sentencia->execute();
    $registro = $sentencia->fetch(PDO::FETCH_LAZY);

    $nombres = $registro["nombres"];
    $apellidoPA = $registro["apellidoPA"];
    $apellidoMA = $registro["apellidoMA"];
    $foto = $registro["foto"];
    $cv = $registro["cv"];
    $idpuesto = $registro["idpuesto"];
    $fechadeingreso = $registro["fechadeingreso"];
}

if($_POST){
    $txtID = (isset($_POST['txtID'])) ? $_POST['txtID'] : "";

    // Recolectamos los datos del método POST
    $nombres = isset($_POST["nombres"]) ? $_POST["nombres"] : "";
    $apellidoPA = isset($_POST["apellidoPA"]) ? $_POST["apellidoPA"] : "";
    $apellidoMA = isset($_POST["apellidoMA"]) ? $_POST["apellidoMA"] : "";
    $idpuesto = isset($_POST["idpuesto"]) ? $_POST["idpuesto"] : "";
    $fechadeingreso = isset($_POST["fechadeingreso"]) ? $_POST["fechadeingreso"] : "";

    // Actualización
    $sentencia = $conexion->prepare("
    UPDATE tbl_empleados
    SET 
        nombres = :nombres,
        apellidoPA = :apellidoPA,
        apellidoMA = :apellidoMA,
        idpuesto = :idpuesto,
        fechadeingreso = :fechadeingreso 
    WHERE id = :id");

    $sentencia->bindParam(":nombres", $nombres);
    $sentencia->bindParam(":apellidoPA", $apellidoPA);
    $sentencia->bindParam(":apellidoMA", $apellidoMA);
    $sentencia->bindParam(":idpuesto", $idpuesto);
    $sentencia->bindParam(":fechadeingreso", $fechadeingreso);
    $sentencia->bindParam(":id", $txtID);
    $sentencia->execute();

    $fecha = new DateTime();

    // Procesar la foto
    $Foto = isset($_FILES["foto"]['name']) ? $_FILES["foto"]['name'] : "";
    $Nombre_Archivo_Foto = ($Foto != '') ? $fecha->getTimestamp()."_".$_FILES["foto"]['name'] : "";
    $tmpFoto = $_FILES["foto"]['tmp_name'];
    if ($tmpFoto != '') {
        move_uploaded_file($tmpFoto, "./" . $Nombre_Archivo_Foto);

        $sentencia = $conexion->prepare("SELECT foto FROM tbl_empleados WHERE id = :id");
        $sentencia->bindParam(":id", $txtID);
        $sentencia->execute();
        $RegistroRecuperado = $sentencia->fetch(PDO::FETCH_LAZY);

        if(isset($RegistroRecuperado["foto"]) && $RegistroRecuperado["foto"] != "") {
            $foto_path = "./" . $RegistroRecuperado["foto"];
            if(file_exists($foto_path)) {
                unlink($foto_path);
            }
        }

        $sentencia = $conexion->prepare("UPDATE tbl_empleados SET foto = :foto WHERE id = :id");
        $sentencia->bindParam(":foto", $Nombre_Archivo_Foto);
        $sentencia->bindParam(":id", $txtID);
        $sentencia->execute();
    }

    // Procesar el CV
    $CV = isset($_FILES["cv"]['name'])?$_FILES["cv"]['name'] : "";
    $Nombre_Archivo_cv = ($CV != '')?$fecha->getTimestamp()."_".$_FILES["cv"]['name'] : "";
    $tmp_CV = $_FILES["cv"]['tmp_name'];
    if ($tmp_CV != ''){
        move_uploaded_file($tmp_CV,"./".$Nombre_Archivo_cv);

        $sentencia = $conexion->prepare("SELECT cv FROM tbl_empleados WHERE id = :id");
        $sentencia->bindParam(":id", $txtID);
        $sentencia->execute();
        $RegistroRecuperado = $sentencia->fetch(PDO::FETCH_LAZY);

        if(isset($RegistroRecuperado["cv"]) && $RegistroRecuperado["cv"] != "") {
            $cv_path="./".$RegistroRecuperado["cv"];
            if(file_exists($cv_path)) {
                unlink($cv_path);
            }
        }

        $sentencia = $conexion->prepare("UPDATE tbl_empleados SET cv = :cv WHERE id = :id");
        $sentencia->bindParam(":cv", $Nombre_Archivo_cv);
        $sentencia->bindParam(":id", $txtID);
        $sentencia->execute();
    }
    $mensaje = "Registro Actualizado";
    header("Location: index.php?mensaje=" . urlencode($mensaje));
    exit;       
}
$sentencia = $conexion->prepare("SELECT * FROM tbl_puestos");
$sentencia->execute(); 
$lista_tbl_Puestos = $sentencia->fetchAll(PDO::FETCH_ASSOC);
?>
<?php include("../../templates/header.php"); ?>
<div class="card">
    <div class="card-header">Editar Empleado</div>
    <div class="card-body">
        <form action="" method="post" enctype="multipart/form-data">
            <input type="hidden" name="txtID" value="<?php echo $txtID; ?>">

            <div class="mb-3">
                <label for="txtID" class="form-label">ID:</label>
                <input value="<?php echo $txtID; ?>" type="text" class="form-control" name="txtID" id="txtID" readonly aria-describedby="helpId" placeholder="id" />
            </div>

            <div class="mb-3">
                <label for="nombres" class="form-label">Nombres:</label>
                <input value="<?php echo $nombres; ?>" type="text" class="form-control" name="nombres" id="nombres" placeholder="Nombres">
            </div>

            <div class="mb-3">
                <label for="apellidoPA" class="form-label">Apellido Paterno:</label>
                <input value="<?php echo $apellidoPA; ?>" type="text" class="form-control" name="apellidoPA" id="apellidoPA" placeholder="Apellido Paterno">
            </div>

            <div class="mb-3">
                <label for="apellidoMA" class="form-label">Apellido Materno:</label>
                <input value="<?php echo $apellidoMA; ?>" type="text" class="form-control" name="apellidoMA" id="apellidoMA" placeholder="Apellido Materno">
            </div>

            <div class="mb-3">
                <label for="foto" class="form-label">Foto:</label>
                <img width="100" src="<?php echo $foto; ?>" class="rounded" alt="" />
                <input type="file" class="form-control" name="foto" id="foto">
            </div>

            <div class="mb-3">
                <label for="cv" class="form-label">CV (PDF):</label>
                <a href="<?php echo $cv; ?>"><?php echo $cv; ?></a>
                <input type="file" class="form-control" name="cv" id="cv">
            </div>

            <div class="mb-3">
                <label for="idpuesto" class="form-label">Puesto:</label>
                <select class="form-select" name="idpuesto" id="idpuesto">
                    <option value="">Selecciona un puesto:</option>
                    <?php foreach ($lista_tbl_Puestos as $registro) { ?>
                        <option <?php echo ($idpuesto == $registro['id']) ? "Selected" : ""; ?> value="<?php echo $registro['id']; ?>">
                            <?php echo $registro['nombredepuesto']; ?>
                        </option>
                    <?php } ?>
                </select>
            </div>

            <div class="mb-3">
                <label for="fechadeingreso" class="form-label">Fecha de ingreso:</label>
                <input type="date" class="form-control" name="fechadeingreso" id="fechadeingreso" value="<?php echo $fechadeingreso; ?>">
            </div>

            <button type="submit" class="btn btn-primary">Actualizar</button>
            <a class="btn btn-secondary" href="index.php">Cancelar</a>
        </form>
    </div>
</div>
<?php include("../../templates/footer.php"); ?>