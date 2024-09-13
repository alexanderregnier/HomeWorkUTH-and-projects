<?php
session_start();
$url_base="http://localhost/5horas/";
if(!isset($_SESSION['usuario'])){
    header("location:".$url_base."login.php");
}else{
    
}

?>
<!doctype html>
<html lang="es">
    <head>
        <title>registro y asi</title>
        <!-- Required meta tags -->
        <meta charset="utf-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1, shrink-to-fit=no"
        />
        <link rel="shortcut icon" href="img\skull-sharp.svg" type="image/svg+xml">
        

        <!-- Bootstrap CSS v5.2.1 -->
        <link
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
            rel="stylesheet"
            integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
            crossorigin="anonymous"
        />
        <script
        src="https://code.jquery.com/jquery-3.6.3.min.js" 
        integrity="sha256-pvPw+upLPUjgMXY0G+8O0xUf+/Im1MZjXxxgOcBQBXU="
        crossorigin="anonymous"></script>
        <!-- integrity="sha256-pvPw+upLPUjgMXY0G+8o0" -->
        <link rel="stylesheet" href="https://cdn.datatables.net/2.0.8/css/dataTables.dataTables.css" />

        <script src="https://cdn.datatables.net/2.0.8/js/dataTables.js"></script>

        <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
    </head>

    <body>
        <header>
            <!-- place navbar here -->
        </header>
        <main>

        <nav class="navbar navbar-expand navbar-light bg-light">
            <ul class="nav navbar-nav">
                <li class="nav-item">
                    <a class="nav-link active" href="<?php echo $url_base;?>" aria-current="page">Sistema Web<span class="visually-hidden">(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="<?php echo $url_base;?>sections/empleados/">Empleados</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="<?php echo $url_base;?>sections/puestos/">Puestos</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="<?php echo $url_base;?>sections/usuarios/">Usuarios</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="<?php echo $url_base;?>close.php">Cerrar secion</a>
                </li>
            </ul>
        </nav>
        </main>

        <main class="container">
        <?php if(isset($_GET['mensaje'])) { ?>
            <script>
                Swal.fire({
                    icon: "success",
                    title: "<?php echo htmlspecialchars($_GET['mensaje'], ENT_QUOTES, 'UTF-8'); ?>"
                });
            </script>
        <?php } ?>