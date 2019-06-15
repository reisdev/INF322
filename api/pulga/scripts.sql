BEGIN
    FOR c IN ( SELECT table_name from user_tables WHERE table_name in ('USERS','ITEMS','SALES','addressesTable','phoneTable')) 
    LOOP 
        EXECUTE IMMEDIATE ('DROP TABLE ' || c.table_name || ' CASCADE CONSTRAINTS PURGE'); 
    END LOOP; 
END;/
CREATE OR REPLACE TYPE ADDRESS FORCE AS OBJECT( num INTEGER, street VARCHAR(30), neighborhood VARCHAR(20), city VARCHAR(20))/
CREATE OR REPLACE TYPE ADDRESSES IS TABLE OF ADDRESS/
CREATE OR REPLACE TYPE PHONES IS VARRAY(2) OF VARCHAR(15)/
CREATE TABLE ITEMS( id NUMBER(1,0) PRIMARY KEY, name VARCHAR(30) )/
CREATE TABLE SALES( id NUMBER(1,0) PRIMARY KEY, time_left NUMBER(2,0), sold_price NUMBER(2), initial_price NUMBER(2), post_date TIMESTAMP(0), done NUMBER(1,0), conclusion DATE)/
CREATE TABLE USERS ( email VARCHAR(30), fullname VARCHAR(50), nickname VARCHAR(15), addresses ADDRESSES, phones PHONES)NESTED TABLE addresses STORE AS addressesTable