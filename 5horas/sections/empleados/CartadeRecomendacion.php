<?php
include("../../BD.php");

if(isset($_GET['txtID'])){
    $txtID = $_GET['txtID'];

    $sentencia = $conexion->prepare("SELECT *, (
        SELECT nombredepuesto FROM tbl_puestos WHERE tbl_puestos.id = tbl_empleados.idpuesto LIMIT 1
    ) AS puesto FROM tbl_empleados WHERE id = :id");
    $sentencia->bindParam(":id", $txtID);
    $sentencia->execute();
    $registro = $sentencia->fetch(PDO::FETCH_LAZY);

    $nombres = htmlspecialchars($registro["nombres"]);
    $apellidoPA = htmlspecialchars($registro["apellidoPA"]);
    $apellidoMA = htmlspecialchars($registro["apellidoMA"]);
    $foto = htmlspecialchars($registro["foto"]);
    $cv = htmlspecialchars($registro["cv"]);
    
    $idpuesto = htmlspecialchars($registro["idpuesto"]);
    $puesto = htmlspecialchars($registro["puesto"]);
    
    $fechadeingreso = htmlspecialchars($registro["fechadeingreso"]);
    
    // Calcula la diferencia de años entre la fecha de ingreso y la fecha actual
    $fechaIngreso = new DateTime($fechadeingreso);
    $fechaActual = new DateTime();
    $diferencia = $fechaActual->diff($fechaIngreso);
}
ob_start();
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Carta de Recomendación</title>
</head>
<body>
    <h1>Carta de Recomendación</h1>
    <br/><br/>
    Hermosillo, Sonora, México a <strong><?php echo date('d-m-Y'); ?></strong>
    <br/><br/>
    A quien pueda interesar:
    <br/><br/>
    Reciba un cordial y respetuoso saludo.
    <br/><br/>

    A través de estas líneas deseo hacer de su conocimiento que el Sr(a).
    <strong><?php echo $nombres;?> <?php echo $apellidoPA;?> <?php echo $apellidoMA;?></strong>, 
    que laboró en mi organización durante <strong><?php echo $diferencia->y; ?> Año(s)</strong>, es un ciudadano con una conducta intachable. 
    Ha demostrado ser un gran trabajador, comprometido, responsable y fiel cumplidor de sus tareas. Siempre ha 
    manifestado preocupación por mejorar, capacitarse y actualizar sus conocimientos.
    <br/><br/>
    Durante estos años se ha desempeñado como: <strong><?php echo $puesto;?></strong>. 
    Es por ello que le sugiero considere esta recomendación, con la confianza de que siempre estará a la altura de sus compromisos y responsabilidades.
    <br><br>
    Sin más a que referirme y esperando que esta misiva sea tomada en cuenta, dejo mi número de contacto para cualquier información de interés.
    <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
    ______________________________________________<br>
    Atentamente,<br>
    Ing. Sadrach Juan Diego García Flores 
</body>
</html>
<?php
$HTML = ob_get_clean();

require_once("../../libs/autoload.inc.php");
use Dompdf\Dompdf;
$dompdf = new Dompdf();

$opciones=$dompdf->getOptions();
$opciones->set(array("isRemoteEnabled"=>true));

$dompdf->setOptions($opciones);

$dompdf->loadHTML($HTML);

$dompdf->setPaper('letter');
$dompdf->render();
$dompdf->stream("archivo.pdf", array("Attachment" => false));
?>
