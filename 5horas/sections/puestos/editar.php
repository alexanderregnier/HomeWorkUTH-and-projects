<?php
include("../../BD.php");    

if(isset($_GET['txtID'])){

    $txtID=(isset($_GET['txtID']))?$_GET['txtID']:"";

    $sentencia=$conexion->prepare("SELECT * FROM tbl_puestos WHERE id=:id");
    $sentencia->bindParam(":id", $txtID);
    $sentencia->execute();

    $registro=$sentencia->fetch(PDO::FETCH_LAZY);
    $nombredepuesto=$registro["nombredepuesto"];
}

if($_POST){
    // Recolectamos los datos del método POST
    $nombredepuesto = isset($_POST["nombredepuesto"]) ? $_POST["nombredepuesto"] : "";
    $txtID = isset($_POST["txtID"]) ? $_POST["txtID"] : "";

    // Actualización
    $sentencia = $conexion->prepare("UPDATE tbl_puestos SET nombredepuesto = :nombredepuesto WHERE id = :id");

    // Asignando los valores que vienen del método POST
    $sentencia->bindParam(":nombredepuesto", $nombredepuesto);
    $sentencia->bindParam(":id", $txtID);
    $sentencia->execute();
    $mensaje = "Registro Editado";
    header("Location: index.php?mensaje=" . urlencode($mensaje));
    exit;
}

?>   
<?php include("../../templates/header.php"); ?>
<?php if(isset($_GET['mensaje'])) { ?>
    <script>
        Swal.fire({
            icon: "success",
            title: "<?php echo htmlspecialchars($_GET['mensaje'], ENT_QUOTES, 'UTF-8'); ?>"
        });
    </script>
<?php } ?>
<div class="card">
    <div class="card-header">Puestos</div>
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
                <label for="nombredepuesto" class="form-label">Nombre del puesto:</label>
                <input
                    value="<?php echo $nombredepuesto;?>"
                    type="text" 
                    class="form-control" name="nombredepuesto" id="nombredepuesto" aria-describedby="helpId" placeholder="Nombre del puesto" />
            </div>
            
            <button type="submit" class="btn btn-primary">Actualizar</button>
            |
            <a name="" id="" class="btn btn-primary" href="index.php" role="button">Cancelar</a>
        </form>
    </div>
    <div class="card-footer text-muted"></div>
</div>

<?php include("../../templates/footer.php"); ?>
