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

    function __toString(){
        return $this->num . ", " . $this->street . ", "
                            . $this->district . ", " . $this->city . "</br>";
    }

    function asType(){
        return "T_ADDRESS(" . $this->num . ", '" . $this->street . "', '"
                            . $this->district . "', '" . $this->city . "')";
    }

    public static function asList($addresses){
        $address_list = "T_LIST_ADDRESS(";
        for($i = 0; $i < count($addresses); $i++){
            $address_list = $address_list . $addresses[$i]->asType();
            if($i + 1 < count($addresses))
                $address_list = $address_list . ", ";
        }
        return $address_list . ")";
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
            " password, addresses, phones) VALUES (" . $this->email . ", " .
                $this->name . ", " . $this->nickname . ", " . $this->password . ", " .
                Address::asList($this->addresses) . ", " . $this->phones->asVarray() . ")";
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

    public function getAddresses($conn){
        $statement = "SELECT a.* FROM USERS u, TABLE(u.ADDRESSES)a WHERE u.NAME = '$this->name'";
        $res = self::fetch($conn,$statement);

        $this->addresses = array();
        for($i = 0; $i < count($res); $i++){
            array_push($this->addresses, new Address($res[$i]->NUM, $res[$i]->STREET, $res[$i]->DISTRICT, $res[$i]->CITY));
        }
    }

    public static function getAll($conn) {
        $statement = "SELECT NAME, NICKNAME, EMAIL FROM USERS";
        $res = self::fetch($conn,$statement);
        foreach($res as $key => $user){
            $res[$key] = User::fromUser($user);
            $res[$key]->getPhones($conn);
            $res[$key]->getAddresses($conn);
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

    public static function getCategory($conn, $name){
        $statement = "SELECT * FROM CATEGORIES where name = '" . $name . "'";
        $res = self::fetch($conn, $statement);
        foreach($res as $key => $category){
            $res = Categories::fromCategory($category);
        }
        return $res;
    }

    public function asCategory(){
        return "CATEGORY('" . $this->name . "', '" . $this->description . "')";
    }
}

class Item extends BaseObject{
    public $name, $description, $category;

    function __construct($n, $d, $c){
        $this->name = $n;
        $this->description = $d;
        $this->category = $c;
    }

    public function fromItem($item){
        $i = new self("","","");
        if(isset($item->NAME)) $i->name = $item->NAME;
        if(isset($item->DESCRIPTION)) $i->description = $item->DESCRIPTION;
        if(isset($item->CATEGORY)) $i->category = $item->CATEGORY;

        return $i;
    }

    public function getCategory($conn){
        $statement = "SELECT c.* FROM CATEGORIES c WHERE c.NAME = '$this->category'";
        $res = self::fetch($conn,$statement);

        $res = new Categories($res[0]->NAME, $res[0]->DESCRIPTION);
        $this->category = $res;
        return $res;
    }

    public static function getAll($conn){
        $statement = "SELECT * FROM ITEM";
        $res = self::fetch($conn, $statement);
        foreach($res as $key => $item){
            $res[$key] = Item::fromItem($item);
        }
        return $res;
    }

    public function save($conn){
        $statement = "INSERT INTO ITEM (name, description, category) VALUES " .
            "('" . $this->name . "', '" . $this->description . "', '" . $this->category . "')";

        $this->runSql($conn, $statement);
    }
}

class Auction extends BaseObject{
    public $id, $post_date, $conclusion_date, $duration, $creator, $item, $minimum_offer;

    public function __construct($conn,$c, $d = 7, $i, $m, $pd = NULL, $cd = NULL){
        if (is_null($pd))
            $pd = date("dmyHis", time());

        $statement = "SELECT id FROM AUCTION ORDER BY id DESC";
        $res = self::fetch($conn, $statement);
        if (count($res) == 0){
            $this->id = 0;
        }
        else{
            $this->id = $res[0]->ID + 1;
        }
        $this->creator = $c;
        $this->duration = $d;
        $this->item = $i;
        $this->minimum_offer = $m;
        $this->post_date = $pd;
        $this->conclusion_date = $cd;
    }

    public function conclude($conn, $cd = NULL){
        if(is_null($cd))
            $cd = date("dmyHis", time());

        $duration = 0;
        $conclusion_date = $cd;

        $statement = "UPDATE AUCTION SET DURATION = 0, CONCLUSION_DATE = " .
            $conclusion_date . " WHERE ID = " . $this->id;
        $this->runSql($conn, $statement);
    }

    public function placeBid($conn, $bidder, $value){
        $statement = "SELECT value FROM AUCTION_BIDS ORDER BY value DESC";
        $res = self::fetch($conn, $statement);
        if (count($res) == 0){
            if($value < $this->minimum_offer)
                return;
        }
        else{
            if($value < $res[0]->VALUE)
                return;
        }

        $bidderRefStatement = "(select ref(u) from USERS u where u.EMAIL = '" . $bidder->email ."')";
        $statement = "INSERT INTO AUCTION_BIDS (BIDDER, AUCTION, VALUE, OFFER_DATE) VALUES " .
            "(" . $bidderRefStatement . ", " . $this->id . ", " . $value . ", " . date("dmyHis", time()) . ")";

        $this->runSql($conn, $statement);
    }

    public function extendAuction($conn){
        $this->duration += 7;
        $statement = "UPDATE AUCTION SET DURATION = " . $this->duration . " WHERE ID = " . $this->id;

        $this->runSql($conn, $statement);
    }

    public function save($conn){
        $creatorRefStatement = "(select ref(u) from USERS u where u.EMAIL = '" . $this->creator->email ."')";
        $statement = "INSERT INTO AUCTION (ID, POST_DATE, CONCLUSION_DATE, " .
                "DURATION, CREATOR, ITEM, MINIMUM_OFFER) " .
                "VALUES (" . $this->id . ", " . $this->post_date . ", null , " .
                $this->duration . ", " . $creatorRefStatement . ", '" .
                $this->item->name . "', " . $this->minimum_offer . ")";

        $this->runSql($conn, $statement);
    }
}

class Simple extends BaseObject{
    public $id, $post_date, $conclusion_date, $duration, $creator, $item, $price, $quantity;

    public function __construct($conn,$c, $d = 7, $i, $p, $q, $pd = NULL, $cd = NULL){
        if (is_null($pd))
            $pd = date("dmyHis", time());

        $statement = "SELECT id FROM SIMPLE ORDER BY id DESC";
        $res = self::fetch($conn, $statement);
        if (count($res) == 0){
            $this->id = 0;
        }
        else{
            $this->id = $res[0]->ID + 1;
        }
        $this->creator = $c;
        $this->duration = $d;
        $this->item = $i;
        $this->price = $p;
        $this->quantity = $q;
        $this->post_date = $pd;
        $this->conclusion_date = $cd;
    }

    public function conclude($conn, $cd = NULL){
        if(is_null($cd))
            $cd = date("dmyHis", time());

        $duration = 0;
        $conclusion_date = $cd;

        $statement = "UPDATE SIMPLE SET DURATION = 0, CONCLUSION_DATE = " .
            $conclusion_date . " WHERE ID = " . $this->id;

        $this->runSql($conn, $statement);
    }

    public function placePurchase($conn, $buyer, $quantity){

        if($this->quantity < $quantity)
            return;

        $buyerRefStatement = "(select ref(u) from USERS u where u.EMAIL = '" . $buyer->email ."')";
        $statement = "INSERT INTO SIMPLE_BUYER (BUYER, QUANTITY, SIMPLE, OFFER_DATE) VALUES " .
            "(" . $buyerRefStatement . ", " . $quantity . ", " . $this->id . ", " . date("dmyHis", time()) . ")";
        $this->runSql($conn, $statement);

        $statement = "UPDATE SIMPLE SET QUANTITY = " . ($this->quantity - $quantity) .
            " WHERE ID = " . $this->id;
        $this->runSql($conn, $statement);

        if($this->quantity == $quantity)
            $this->conclude($conn);

    }

    public function extendSale($conn){
        $this->duration += 7;
        $statement = "UPDATE SIMPLE SET DURATION = " . $this->duration . " WHERE ID = " . $this->id;

        $this->runSql($conn, $statement);
    }

    public function save($conn){
        $creatorRefStatement = "(select ref(u) from USERS u where u.EMAIL = '" . $this->creator->email ."')";
        $statement = "INSERT INTO SIMPLE (ID, POST_DATE, CONCLUSION_DATE, " .
                "DURATION, CREATOR, ITEM, PRICE, QUANTITY) " .
                "VALUES (" . $this->id . ", " . $this->post_date . ", null , " .
                $this->duration . ", " . $creatorRefStatement . ", '" .
                $this->item->name . "', " . $this->price . ", " . $this->quantity . ")";

        $this->runSql($conn, $statement);
    }
}

class Donation extends BaseObject{

}

class Service extends BaseObject{

}

class Exchange extends BaseObject{

}

?>
