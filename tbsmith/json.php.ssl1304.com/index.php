<?php 

include "controllers/word_service.php";

header('Content-type: text/html');

$g = $_GET;
$p = $_POST;
$con = empty($g['controller']) ? 'word_service' : $g['controller'];
$action = empty($g['action']) ? 'encode' : $g['action'];

$ws = new WordService();

if ($action == 'fnsearch') {
    if (!empty($p['firstname'])) {
        $firstname = $p['firstname'];
        echo $ws->fnsearch($firstname);
    } else {
        echo "Nothing to search for.";
    }
} else if ($action == 'duck') {
    echo $ws->duck($p['text']);
}

?>

<html>
<body>
SEARCH USERS:<br/>
<form action="/word_service/fnsearch" 
    enctype="multipart/form-data" method="POST">
Firstname: <input name="firstname"><br/>
<input type="submit">
</form>

<br/>
SEARCH Duck Duck Go:<br/>
<form action="/word_service/duck"
    enctype="multipart/form-data" method="POST">
Keyword: <input name="text"><br/>
<input type="submit">
</form>
</body>
</html>
