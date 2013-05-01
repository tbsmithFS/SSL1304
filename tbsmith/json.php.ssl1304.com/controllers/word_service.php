<?php

include "models/DBConnector.php";

class WordService {

    var $db;

    function __construct() {
        $dbc = new DBConnector();
        $this->db = $dbc->connect();
    }

    function fnsearch($fn) {
        $sql = 'select * from address where firstname like ? limit 10';
        $q = $this->db->prepare($sql);
        $q->execute(array($fn));
        echo json_encode($q->fetchAll());
    }

    function duck($text='default') {

        $url = "http://api.duckduckgo.com/?q=" 
            . urlencode($text)
            . "&format=json&pretty=1";

        $contents = file_get_contents($url);

        $data = json_decode($contents);

        echo "<pre>";
        var_dump($data);
        echo "</pre>";
    }

}

?>
