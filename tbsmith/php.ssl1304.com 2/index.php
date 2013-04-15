<?php

if (empty($_GET["controller"])) {
    $con = 'home';
} else {
    $con = $_GET["controller"];
}

if ($con == 'home') {
    include "controllers/home.php";
    $controller = new Home();
    $controller->get($_GET);
} else if ($con == 'utilities') {
    include "controllers/utilities.php";
    $controller = new Utilities();
    $controller->get($_GET);
} else if ($con == 'user') {
    include "controllers/user.php";
    $controller = new User();
    $controller->get($_GET);
}

?>


