<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Pulga</title>
    <?php
        require("./app/imports.php");
    ?>
    <script>
        function LOG(m){
            console.log(m);
        }
    </script>
</head>
<body>
    <div class="ui centered container" style="text-align:center; margin-top: 25px">
        <h1><?php echo "Welcome to our Web Application!"; ?></h1>
        <div class="ui cards">
        <?php
            try {
                $db = new Database();
                $db->connect();
                /*
                $user = new User("pau@pau", "paupau", "paupauzinho", "tititi",
                            array(new Address(54, "a", "b", "c"), new Address(51, "e", "f", "g")),
                            new Phone("313131","31993728739"));
                $user->save($db->getConnection());
                */
                $users = User::getAll($db->getConnection());

                foreach($users as $user){
                    ?>
                        <div class="ui card">
                            <div class="content">
                                <div class="header"><?php echo $user->name ?> </div>
                            </div>
                            <div class="content">
                                <p> Email : <?php echo $user->email ?> </p>
                                <p> Telefones: <?php echo $user->phones; ?>
                                <p> Endereço(s): <?php echo implode("",$user->addresses); ?>
                            </div>
                        </div>
                    <?php
                }

                $categories = Categories::getAll($db->getConnection());
                foreach($categories as $cat){
                    ?>
                        <div class="ui card">
                            <div class="content">
                                <div class="header"><?php echo $cat->name ?> </div>
                            </div>
                            <div class="content">
                                <p> Descricao : <?php echo $cat->description; ?>
                            </div>
                        </div>
                    <?php
                }

                $itens = Item::getAll($db->getConnection());
                foreach($itens as $it){
                    ?>
                        <div class="ui card">
                            <div class="content">
                                <div class="header"><?php echo $it->name ?> </div>
                            </div>
                            <div class="content">
                                <p> Descricao : <?php echo $it->description; ?>
                                <p> Categoria : <?php echo $it->category; ?>
                            </div>
                        </div>
                    <?php
                }
            } catch(Exception $e){
                echo "Error: " + $e;
            }
        ?>
        </div>
    </div>
</body>
</html>
