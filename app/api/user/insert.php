<?php
    if(!isset($_POST["name"]) || !isset($_POST["email"]) || !isset($_POST["nickname"]) || !isset($_POST["password"]) || !isset($_POST[])){
        $res = array();
        array_push($res,["status"=> 403]);
        echo json_encode($res);
    }
?>