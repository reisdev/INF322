BEGIN
  FOR c IN ( SELECT table_name
             from user_tables)
    LOOP
      EXECUTE IMMEDIATE ('DROP TABLE ' || c.table_name || ' 
cascade constraints PURGE');
    END LOOP;
END;
/
DROP TYPE T_BASE_SALE FORCE;
DROP TYPE T_ADDRESS FORCE;
DROP TYPE T_USER FORCE;
DROP TYPE T_SIMPLE FORCE;
DROP TYPE T_AUCTION FORCE;
DROP TYPE T_EXCHANGE FORCE;
DROP TYPE T_SERVICE FORCE;
DROP TYPE T_DONATION FORCE;
drop table "SIMPLE" cascade constraints PURGE;
drop table "SERVICE" cascade constraints PURGE;
drop table "EXCHANGE" cascade constraints PURGE;
drop table "DONATION" cascade constraints PURGE;
drop table "AUCTION" cascade constraints PURGE;
drop table "USERS" cascade constraints PURGE;