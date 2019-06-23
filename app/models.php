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
}

class Phone extends BaseObject{
    private $phones;

    function __construct($p1, $p2 = NULL){
        $this->phones = array($p1, $p2);
    }

    public static function fromPhone($phone){
        $instance = new self($phone[0],$phone[1]);
        return $instance;
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

    public function __toString() {
        $string ="";
        if($this->phones[0] != NULL){
            $string .= "" . $this->phones[0];
        }
        if($this->phones[1] !== NULL){
            $string .= " " . $this->phones[1];
        }
        return $string;
    }
    public function get($i){
        return $this->phones[$i];
    }
}

class Item extends BaseObject{

}

class User extends BaseObject{
    public $email, $name, $nickname, $password, $addresses, $phones;
    function __construct($e, $f, $n, $p, $a, $ph){
        $this->email = "'" . $e . "'";
        $this->name = "'" . $f . "'";
        $this->nickname = "'" . $n . "'";
        $this->password = "'" . $p . "'";
        $this->addresses = $a;
        $this->phones = $ph;
    }
    function fromUser($user){
        $u = new self("","","","","","");
        if(isset($user->EMAIL)) $u->email = $user->EMAIL;
        if(isset($user->NAME)) $u->name = $user->NAME;
        if(isset($user->NICKNAME)) $u->nickname = $user->NICKNAME;
        if(isset($user->PASSWORD)) $u->password = $user->PASSWORD;
        if(isset($user->ADDRESSES)) $u->addresses = $user->ADDRESSES;
        if(isset($user->PHONES)) $u->phones = $user->PHONES;
        return $u;
    }
    public function save($conn){
        $statement = "INSERT INTO USERS (email, name, nickname, " .
            " password, address, phones) VALUES (" . $this->email . ", " .
                $this->name . ", " . $this->nickname . ", " . $this->password . ", " .
                $this->addresses->asType() . ", " . $this->phones->asVarray() . ")";
        echo($statement);
        $this->runSql($conn, $statement);
    }

    public function getPhones($conn){
        $statement = "SELECT p.* FROM USERS u, TABLE(u.PHONES)p WHERE u.NAME = '$this->name'";
        $res = self::fetch($conn,$statement);
        if(count($res) == 2)
            $this->phones = new Phone($res[0]->COLUMN_VALUE,$res[1]->COLUMN_VALUE);
        else if(count($res) == 1)
            $this->phones = new Phone($res[0]->COLUMN_VALUE,"");
        else
            $this->phones = new Phone("", "");
        return $res;
    }

    public static function getAll($conn) {
        $statement = "SELECT NAME, NICKNAME, EMAIL FROM USERS";
        $res = self::fetch($conn,$statement);
        foreach($res as $key => $user){
            $res[$key] = User::fromUser($user);
            $res[$key]->getPhones($conn);
        }
        return $res;
    }
}

class Categories extends BaseObject{
    public $name, $description;

    function __construct($n, $d){
        $this->name = $n;
        $this->description = $d;
    }

    public function fromCategory($category){
        $c = new self("","");
        if(isset($category->NAME)) $c->name = $category->NAME;
        if(isset($category->DESCRIPTION)) $c->description = $category->DESCRIPTION;

        return $c;
    }

    public static function getAll($conn){
        $statement = "SELECT * FROM CATEGORIES";
        $res = self::fetch($conn, $statement);
        foreach($res as $key => $category){
            $res[$key] = Categories::fromCategory($category);
        }
        return $res;
    }
}


?>
