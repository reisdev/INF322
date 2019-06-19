BEGIN
  FOR c IN ( SELECT object_name, object_type, owner
             from all_objects
             WHERE object_name in
                   ('USERS', 'ITEMS', 'SALES', 'T_USER', 'T_SALE',
                    'T_ADDRESS', 'T_PHONES', 'T_LIST_ADDRESSES', 'T_ITEM'))
    LOOP
      EXECUTE IMMEDIATE ('DROP ' || c.object_type || ' ' || c.owner || '.' || c.object_name || ' FORCE');
    END LOOP;
END;
/

CREATE OR REPLACE TYPE T_ADDRESS FORCE AS OBJECT
(
  num      INTEGER,
  street   VARCHAR(30),
  district VARCHAR(20),
  city     VARCHAR(20)
)
/
CREATE OR REPLACE TYPE T_LIST_ADDRESSES IS TABLE OF T_ADDRESS
/
CREATE OR REPLACE TYPE T_PHONES IS VARRAY (2) OF VARCHAR(15)
/
CREATE OR REPLACE TYPE T_USER FORCE AS OBJECT
(
  email     VARCHAR(30),
  fullname  VARCHAR(50),
  nickname  VARCHAR(25),
  password  VARCHAR(25),
  addresses T_LIST_ADDRESSES,
  phones    T_PHONES
)
/
CREATE OR REPLACE TYPE T_SALE FORCE AS OBJECT
(
  time_left     NUMBER(2, 0),
  sold_price    NUMBER(2),
  initial_price NUMBER(2),
  post_date     TIMESTAMP(0),
  done          NUMBER(1, 0),
  conclusion    DATE
)
/
CREATE OR REPLACE TYPE T_ITEM FORCE AS OBJECT
(
  name VARCHAR(30)
)
/
CREATE TABLE ITEMS of T_ITEM
/
CREATE TABLE SALES of T_SALE
/
CREATE TABLE USERS of T_USER NESTED TABLE addresses STORE AS tabAdresses
/
