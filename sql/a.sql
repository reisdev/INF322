INSERT INTO USERS (EMAIL,NAME,NICKNAME,PASSWORD,ADDRESSES,PHONES) 
    VALUES ( 'matheus@gmail.com','Matheus','Reis','123',
        T_LIST_ADDRESS(T_ADDRESS(125,'Carijós','Sto. Ant.','Viçosa'),T_ADDRESS(100,'Benjamim Araújo','Centro','Viçosa')),
        T_PHONES('96587452639','316874596')
    );

INSERT INTO USERS (EMAIL,NAME,NICKNAME,PASSWORD,ADDRESSES,PHONES) 
    VALUES ( 'jugurta@ufv.br','Jugurta Filho','Jugurta','bd123',
        T_LIST_ADDRESS(T_ADDRESS(456,'PH Rolfs','Centro','Viçosa')),
        T_PHONES('5798562152','74286355478')
    );
