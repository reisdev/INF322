<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Pulga</title>
    <?php
        require("./app/imports.php");
        require_once("./app/database.php");
        require_once("./app/models.php");
    ?>
    <script>
        function LOG(m){
            console.log(m);
        }
    </script>
</head>
<body>
    <div class="ui container" style="text-align:center; margin-top: 25px">
        <h1><?php echo "Welcome to our Web Application!"; ?></h1>
        <?php
            try {
                $db = new Database();
                $db->connect();
                $db->buildDatabase();
                #$user = new User("pau@pau", "paupau", "paupauzinho", "tititi",
                #            new Address(54, "a", "b", "c"), new Phone(313131));
                #$user->insertIntoDb($db->getConnection());
            } catch(Exception $e){
                echo "Error: " + $e;
            }
        ?>
    </div>
</body>
</html>
