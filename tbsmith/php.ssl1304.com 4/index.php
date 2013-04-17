<?php

include "models/DBConnector.php";

header('Content-type: text/html');

$db = new DBConnector();

$result = $db->getRandomUser();
var_dump($result);

$db->addUser('joe', 'smith', '123 main st', 'Capitol City', 'ST', 
    '12345', '334-232-4242');

?>
