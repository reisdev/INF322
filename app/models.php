<?php

class BaseObject{
    protected function runSql($conn, $sql){
        $result = oci_execute(oci_parse($conn, $sql));
        oci_commit($conn);
        return $result;
    }
    protected function fetch($conn,$sql) {
        $result = array();
        $stid = oci_parse($conn,$sql);
        oci_execute($stid);
        oci_commit();
        while(($row = oci_fetch_object($stid))){
            array_push($result,$row);
        }
        oci_free_statement($stid);
        return $result;
    }
}

class Address extends BaseObject{
    private $num, $street, $district, $city;

    function __construct($n, $s, $d, $c){
        $this->num = $n;
        $this->street = $s;
        $this->district = $d;
        $this->city = $c;
    }

    function asType(){
        return "T_ADDRESS(" . $this->num . ", '" . $this->street . "', '"
                            . $this->district . "', '" . $this->city . "')";
    }

    function asTable(){
        return "T_LIST_ADDRESSES(" . $this->asType() .")";
    }
}

class Phone extends BaseObject{
    private $phones;

    function __construct($p1, $p2 = NULL){
        $phones = array($p1, $p2);
    }

    function asVarray(){
        $string = "T_PHONES(" . "'" .$this->phones[0] . "'";
        if($this->phones[1] != NULL)
            $string = $string . ", '" .$this->phones[1] . "')";
        else {
            $string = $string . ")";
        }
        return $string;
    }
}

class Item extends BaseObject{
    
}

class User extends BaseObject{
    private $email, $fullname, $nickname, $password, $addresses, $phones;
    function __construct($e, $f, $n, $p, $a, $ph){
        $this->email = "'" . $e . "'";
        $this->fullname = "'" . $f . "'";
        $this->nickname = "'" . $n . "'";
        $this->password = "'" . $p . "'";
        $this->addresses = $a;
        $this->phones = $ph;
    }
    public function save($conn){
        $statement = "INSERT INTO USERS (email, fullname ,  nickname, " .
            " password, addresses, phones) VALUES (" . $this->email . ", " .
                $this->fullname . ", " . $this->nickname . ", " . $this->password . ", " .
                $this->addresses->asTable() . ", " . $this->phones->asVarray() . ")";


        $this->runSql($conn, $statement);
    }

    public function getAll($conn) {
        $statement = "SELECT * FROM USERS";
        echo $statement;
        foreach($this->fetch($conn,$statement) as $user){
            echo $user['FULLNAME'];
        }
    }
}


?>
