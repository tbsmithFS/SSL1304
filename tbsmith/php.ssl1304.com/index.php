<?php

include("settings/db.php");
include("models/view.php");

$view = new View();
$view->printHeader();

$data = array(
    'bottomLeftContent' => "Newest Bathroom Review",
    'bottomRightContent' => "Newest Electric Review",
    'copyright_info' => "Full Sail University 2013",
);

$view->getView("header", $data);
$view->getView("body", $data);
$view->getView("footer", $data);

?>



