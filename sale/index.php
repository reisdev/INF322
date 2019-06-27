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
?>
</div>