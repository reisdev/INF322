<?php

class Database {
    private $conn;
    private $USER = "c_pulga";
    private $PSWD = "pulga";
    private $HOST = "localhost:1521/orcl";
    public function __construct() {
    }
    public function getConnection(){
        return $this->conn;
    }
    public function connect(){
        try {
            $this->conn = oci_connect($this->USER,$this->PSWD,$this->HOST);
            ?>
            <div style='vertical-align: middle; display: flex'>
                <svg height='26' width='26'><circle cx='13' cy='13' r='12' fill='green'></circle></svg>
                <p style='padding-top: 3px; padding-left: 4px'><span>Database</span></p>
            </div>
            <?php

            if(!$this->conn) {
                ?>
                <div style='vertical-align: middle; display: flex'>
                    <svg height='26' width='26'><circle cx='13' cy='13' r='12' fill='red'></circle></svg>
                    <p style='padding-top: 3px; padding-left: 4px'><span>Database</span></p>
                </div>
                <?php
                throw new Exception("Unnable to connect to the Database");
            }

        } catch(Error $e) {
            ?>
            <div style='vertical-align: middle; display: flex'>
                <svg height='26' width='26'><circle cx='13' cy='13' r='12' fill='red'></circle></svg>
                <p style='padding-top: 3px; padding-left: 4px'><span>Database</span></p>
            </div>
            <?php
            echo "<p><h3>An error has ocurred on connecting: </h3></p> $e";
        } catch(Exception $e) {
            echo "<p><h3>An exception has ocurred on connecting: </h3></p> $e";
        }
    }

    public static function buildDatabase($response = False){
        if($response == True)
            echo shell_exec('sqlplus c_pulga/pulga @scripts.sql');
        else {
            shell_exec('sqlplus c_pulga/pulga @scripts.sql');
        }
    }
}
?>
