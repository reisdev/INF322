<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Pulga</title>
</head>
<body>
<?php 
    echo "Welcome to our Web Application!";

    try {
        //                 ($USER,$PSWD,$HOST/$DATABASE)
        $conn = oci_connect("SYSTEM","Pulga1234","localhost:1521/pulga");
        if(!$conn){
            echo "Error when connecting to Database!";
        }
    } catch(Exception $e){
        echo "Error: " + $e;
    }
?>
</body>
</html>

