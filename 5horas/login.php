<?php
session_start();
if ($_POST) {    
    include("./BD.php");
    
    // Seleccionamos todos los usuarios
    $sentencia = $conexion->prepare("SELECT *, COUNT(*) as n_usuarios FROM tbl_usuarios WHERE usuario = :usuario AND contrasena = :contrasena");

    $usuario = $_POST["usuario"];
    $contrasena = $_POST["contrasena"];

    $sentencia->bindParam(":usuario", $usuario);
    $sentencia->bindParam(":contrasena", $contrasena);
    $sentencia->execute();

    $Registro = $sentencia->fetch(PDO::FETCH_LAZY);
    if ($Registro["n_usuarios"] > 0) {
        $_SESSION['usuario'] = $Registro["usuario"];
        $_SESSION['logeado'] = true;
        header("Location: index.php");
        exit();
    } else {
        $mensaje = "Error: el usuario o la contraseña son incorrectos";
    }
}
?>
<!doctype html>
<html lang="es">
    <head>
        <title>Login</title>
        <!-- Required meta tags -->
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />

        <!-- Bootstrap CSS v5.2.1 -->
        <link
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
            rel="stylesheet"
            integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
            crossorigin="anonymous"
        />
    </head>

    <body>
        <header>
            <!-- place navbar here -->
        </header>
        <main class="container">
            <div class="row">
                <div class="col-md-4"></div>
                <div class="col-md-4">
                    <br><br>
                    <div class="card">
                        <div class="card-header">Login</div>
                        <div class="card-body">
                            <?php if (isset($mensaje)) { ?>
                                <div class="alert alert-danger" role="alert">
                                    <strong><?php echo $mensaje; ?></strong>
                                </div>
                            <?php } ?>

                            <form action="" method="post">
                                <div class="mb-3">
                                    <label for="usuario" class="form-label">Usuario:</label>
                                    <input type="text" class="form-control" name="usuario" id="usuario" placeholder="Escriba su usuario" required />
                                </div>
                                <div class="mb-3">
                                    <label for="contrasena" class="form-label">Contraseña:</label>
                                    <input type="password" class="form-control" name="contrasena" id="contrasena" placeholder="Escriba su contraseña" required />
                                </div>
                                <button type="submit" class="btn btn-primary">Entrar al sistema</button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </main>
        <footer>
            <!-- place footer here -->
        </footer>
        <!-- Bootstrap JavaScript Libraries -->
        <script
            src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js"
            integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r"
            crossorigin="anonymous"
        ></script>

        <script
            src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js"
            integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+"
            crossorigin="anonymous"
        ></script>
    </body>
</html>
