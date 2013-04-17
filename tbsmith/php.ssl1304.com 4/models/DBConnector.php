<?php

class DBConnector {

    public $db;

    function __construct() {
        $host = '127.0.0.1';
        $user = 'root';
        $pass = 'root';
        $port = '3306';
        $dbname = 'fakeUsers';
        $this->db = new PDO("mysql:host=$host;port=$port;dbname=$dbname", $user, $pass);
        return $this->db;
    }

    public function getRandomUser() {
        $stmnt = $this->db->query("SELECT * from address ORDER BY rand() LIMIT 1");
        return $stmnt->fetchAll(PDO::FETCH_ASSOC);
    }

    public function addUser($firstname='', $lastname='', $address='', $city='', 
        $state='', $zip='', $phone='') {
            $stmnt = $this->db->prepare("INSERT INTO address(firstname, lastname,
                address, city, state, zip, phone) values (:fn, :ln, :add,
                :city, :st, :zip, :phone)");
            $stmnt->execute(array(
                ':fn'=>$firstname, 
                ':ln'=>$lastname,
                ':add'=>$address,
                ':city'=>$city,
                ':st'=>$state,
                ':zip'=>$zip,
                ':phone'=>$phone));
    }

}

?>
