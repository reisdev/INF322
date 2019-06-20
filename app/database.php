<?php

class Database {
    private $conn;
    private $USER = "";
    private $PSWD = "";
    private $HOST = "localhost:1521/";
    public function __construct() {
    }
    public function getConnection(){
        return $this->conn;
    }
    public function connect(){
        try {
            $this->conn = oci_connect($this->USER,$this->PSWD,$this->HOST);
            if(!$this->conn) {
                ?>
                <div style='vertical-align: middle; display: flex'>
                    <svg height='26' width='26'><circle cx='13' cy='13' r='12' fill='red'></circle></svg>
                    <p style='padding-top: 3px; padding-left: 4px'><span>Database</span></p>
                </div>
                <?php
                throw new Exception("Unnable to connect to the Database");
            } else {
                ?>
                <div style='vertical-align: middle; display: flex'>
                    <svg height='26' width='26'><circle cx='13' cy='13' r='12' fill='green'></circle></svg>
                    <p style='padding-top: 3px; padding-left: 4px'><span>Database</span></p>
                </div>
                <?php
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

    public function buildDatabase($response = False){
        try {
            if($response == True){
                echo shell_exec("sqlplus $this->USER/$this->PSWD @scripts.sql 2>&1");
            }
            else {
                shell_exec("sqlplus $this->USER/$this->PSWD @scripts.sql");
            }
        }
        catch(Error $e) {
            echo "An error has ocurred: $e";
        }
        catch (Excpetion $e){
            echo "An exception has ocurred: $e";
        }
    }
}
?>
