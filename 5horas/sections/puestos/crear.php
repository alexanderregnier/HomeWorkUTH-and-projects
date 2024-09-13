<?php
include("../../BD.php");    

if($_POST){
    // Recolectamos los datos del método POST
    $nombredepuesto = isset($_POST["nombredepuesto"]) ? $_POST["nombredepuesto"] : "";

    // Inserción
    $sentencia = $conexion->prepare("INSERT INTO `tbl_puestos`(`id`, `nombredepuesto`) VALUES (NULL, :nombredepuesto)");

    // Asignando los valores que vienen del método POST
    $sentencia->bindParam(":nombredepuesto", $nombredepuesto);
    $sentencia->execute();
    $mensaje = "Registro Creado";
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
        <form action="" method="post" enctype="multipart/form-data"> <!-- Corregido from a form -->
            <div class="mb-3">
                <label for="nombredepuesto" class="form-label">Nombre del puesto:</label>
                <input type="text" 
                    class="form-control" name="nombredepuesto" id="nombredepuesto" aria-describedby="helpId" placeholder="Nombre del puesto" />
            </div>
            
            <button type="submit" class="btn btn-primary">Agregar</button>
            |
            <a name="" id="" class="btn btn-primary" href="index.php" role="button">Cancelar</a>
        </form> <!-- Corregido from a form -->
    </div>
    <div class="card-footer text-muted"></div>
</div>

<?php include("../../templates/footer.php"); ?>
