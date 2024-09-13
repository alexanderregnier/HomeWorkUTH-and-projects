<?php
include("../../BD.php");    
if($_POST){
    // Recolectamos los datos del método POST
    $nombres = isset($_POST["nombres"])?$_POST["nombres"] : "";
    $apellidoPA = isset($_POST["apellidoPA"])?$_POST["apellidoPA"] : "";
    $apellidoMA = isset($_POST["apellidoMA"])?$_POST["apellidoMA"] : "";

    $foto = isset($_FILES["foto"]['name'])?$_FILES["foto"]['name'] : "";
    $cv = isset($_FILES["cv"]['name'])?$_FILES["cv"]['name'] : "";

    $idpuesto = isset($_POST["idpuesto"])?$_POST["idpuesto"] : "";
    $fechadeingreso = isset($_POST["fechadeingreso"]) ? $_POST["fechadeingreso"] : "";

    // Inserción
    $sentencia = $conexion->prepare("INSERT INTO tbl_empleados(id,nombres,apellidoPA,apellidoMA,foto,cv,idpuesto,fechadeingreso)
    VALUES(NULL,:nombres,:apellidoPA,:apellidoMA,:foto,:cv,:idpuesto,:fechadeingreso);");
    
    // Asignando los valores que vienen del método POST
    $sentencia->bindParam(":nombres", $nombres);
    $sentencia->bindParam(":apellidoPA", $apellidoPA);
    $sentencia->bindParam(":apellidoMA", $apellidoMA);

    $fecha = new DateTime();

    $Nombre_Archivo_foto=($foto!='')?$fecha->getTimestamp()."_".$_FILES["foto"]['name']:"";
    $tmpfoto=$_FILES["foto"]['tmp_name'];
    if ($tmpfoto!='') {
        move_uploaded_file($tmpfoto,"./".$Nombre_Archivo_foto);
    }
    $sentencia->bindParam(":foto",$Nombre_Archivo_foto);

    $Nombre_Archivo_cv=($cv!='')?$fecha->getTimestamp()."_".$_FILES["cv"]['name']:"";
    $tmpcv = $_FILES["cv"]['tmp_name'];
    if($tmpcv!=''){
        move_uploaded_file($tmpcv,"./".$Nombre_Archivo_cv);
    }
    $sentencia->bindParam(":cv",$Nombre_Archivo_cv);

    $sentencia->bindParam(":idpuesto", $idpuesto);
    $sentencia->bindParam(":fechadeingreso", $fechadeingreso);
    $sentencia->execute();
    $mensaje = "Registro Creado";
    header("Location: index.php?mensaje=" . urlencode($mensaje));
    exit;
    
}
$sentencia = $conexion->prepare("SELECT * FROM tbl_puestos");
$sentencia->execute(); 
$lista_tbl_Puestos = $sentencia->fetchAll(PDO::FETCH_ASSOC);
?>
<?php include("../../templates/header.php"); ?>
<div class="card">
    <div class="card-header">Agregar datos del empleado</div>
    <div class="card-body">
    
        <form action="" method="post" enctype="multipart/form-data">
            <div class="mb-3">
                <label for="nombres" class="form-label">nombres</label>
                <input type="text" class="form-control" name="nombres" id="nombres" aria-describedby="helpId" placeholder="Nombre(s)"/>
            </div>
            
            <div class="mb-3">
                <label for="apellidoPA" class="form-label">Apellido Paterno</label>
                <input type="text" class="form-control" name="apellidoPA" id="apellidoPA" aria-describedby="helpId" placeholder="Apellido Paterno"/>
            </div>

            <div class="mb-3">
                <label for="apellidoMA" class="form-label">Apellido Materno</label>
                <input type="text" class="form-control" name="apellidoMA" id="apellidoMA" aria-describedby="helpId" placeholder="Apellido Materno"/>
            </div>
            
            <div class="mb-3">
                <label for="foto" class="form-label">foto:</label>
                <input type="file" class="form-control" name="foto" id="foto" aria-describedby="HelpId" placeholder="foto"/> 
            </div>

            <div class="mb-3">
                <label for="cv" class="form-label">CV(PDF):</label>
                <input type="file" class="form-control" name="cv" id="cv" aria-describedby="HelpId" placeholder="cv"/> 
            </div>
            
            <div class="mb-3">
                <label for="idpuesto" class="form-label">Puesto:</label>
                <select class="form-select form-select-sm" name="idpuesto" id="idpuesto">
                    <?php foreach ($lista_tbl_Puestos as $registro) { ?>
                    <option value="<?php echo $registro['id']; ?>">
                    <?php echo $registro['nombredepuesto']; ?></option>
                    <?php } ?>
                </select>
            </div>

            <div class="mb-3">
                <label for="fechadeingreso" class="form-label">Fecha de ingreso</label>
                <input type="date" class="form-control" name="fechadeingreso" id="fechadeingreso" aria-describedby="emailHelpId" placeholder="fecha de ingreso"/> 
            </div>
            <button type="submit" class="btn btn-success">Agregar registro</button>
            <a class="btn btn-primary" href="index.php" role="button">Cancelar</a>
        </form>
    </div>
    <div class="card-footer text-muted"></div>
</div>
<?php include("../../templates/footer.php"); ?>
