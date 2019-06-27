<?php require_once("../app/imports.php"); ?>

<div class="ui container">

<?php
    if(isset($_GET["view"])){
        switch($_GET["view"]){
            case "insert":
                require_once("insert.php");    
                break;
        }
    }
    else if($_SERVER['REQUEST_METHOD'] === 'POST'){
        if(!isset($_POST['name']) || !isset($_POST['email']) || !isset($_POST['password'])){
            echo "Error";
        }
        else {
            try {
                $phones = new Phone("31993102771","9310123");
                $address = new Address(120,"14","Sto. Ant.","Viçosa");
                $a = array($address);
                $user = new User($_POST['email'],$_POST['name'],$_POST['nickname'],$_POST["password"], $a,$phones);
                $db = new Database();
                $db->connect();
                $user->save($db->getConnection());
            }
            catch(Exception $e){
                echo $e;
            }
            
        }
    }
?>

</div>