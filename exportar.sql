--------------------------------------------------------
--  Arquivo criado - Sexta-feira-Junho-21-2019
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Type T_ADDRESS
--------------------------------------------------------

  CREATE OR REPLACE NONEDITIONABLE TYPE "T_ADDRESS" FORCE AS OBJECT
(
  num      INTEGER,
  street   VARCHAR(30),
  district VARCHAR(20),
  city     VARCHAR(20)
)

/

--------------------------------------------------------
--  DDL for Type T_PHONES
--------------------------------------------------------

  CREATE OR REPLACE NONEDITIONABLE TYPE "T_PHONES" IS VARRAY (2) OF VARCHAR(15)

/
--------------------------------------------------------
--  DDL for Table AUCTION
--------------------------------------------------------

  CREATE TABLE "AUCTION"
   (	"ID" NUMBER(*,0),
	"POST_DATE" TIMESTAMP (6),
	"CONCLUSION_DATE" TIMESTAMP (6),
	"INITIAL_PRICE" NUMBER,
	"ITEM" VARCHAR2(20 BYTE),
	"QUANTITY" NUMBER
   ) SEGMENT CREATION DEFERRED
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
 NOCOMPRESS LOGGING
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table AUCTION_BIDS
--------------------------------------------------------

  CREATE TABLE "AUCTION_BIDS"
   (	"BIDDER" VARCHAR2(20 BYTE),
	"AUCTION" NUMBER,
	"VALUE" NUMBER,
	"OFFER_DATE" TIMESTAMP (6)
   ) SEGMENT CREATION DEFERRED
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
 NOCOMPRESS LOGGING
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table AUCTION_CREATOR
--------------------------------------------------------

  CREATE TABLE "AUCTION_CREATOR"
   (	"CREATOR" VARCHAR2(20 BYTE),
	"AUCTION" NUMBER
   ) SEGMENT CREATION DEFERRED
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
 NOCOMPRESS LOGGING
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table CATEGORIES
--------------------------------------------------------

  CREATE TABLE "CATEGORIES"
   (	"NAME" VARCHAR2(20 BYTE),
	"DESCRIPTION" VARCHAR2(50 BYTE)
   ) SEGMENT CREATION DEFERRED
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
 NOCOMPRESS LOGGING
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table DONATION
--------------------------------------------------------

  CREATE TABLE "DONATION"
   (	"ID" NUMBER(*,0),
	"ITEM" VARCHAR2(20 BYTE),
	"POST_DATE" TIMESTAMP (6),
	"CONCLUSION_DATE" TIMESTAMP (6),
	"QUANTITY" NUMBER
   ) SEGMENT CREATION DEFERRED
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
 NOCOMPRESS LOGGING
  STORAGE(
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"   NO INMEMORY ;
--------------------------------------------------------
--  DDL for Table DONATION_CREATOR
--------------------------------------------------------

  CREATE TABLE "DONATION_CREATOR"
   (	"CREATOR" VARCHAR2(20 BYTE),
	"DONATION" NUMBER
   ) SEGMENT CREATION DEFERRED
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
 NOCOMPRESS LOGGING
  STORAGE(
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"   NO INMEMORY ;
--------------------------------------------------------
--  DDL for Table DONATION_DONATEE
--------------------------------------------------------

  CREATE TABLE "DONATION_DONATEE"
   (	"BUYER" VARCHAR2(20 BYTE),
	"QUANTITY" NUMBER,
	"DONATION" NUMBER
   ) SEGMENT CREATION DEFERRED
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
 NOCOMPRESS LOGGING
  STORAGE(
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"   NO INMEMORY ;
--------------------------------------------------------
--  DDL for Table EXCHANGE
--------------------------------------------------------

  CREATE TABLE "EXCHANGE"
   (	"ID" NUMBER(*,0),
	"ITEM" VARCHAR2(20 BYTE),
	"POST_DATE" TIMESTAMP (6),
	"CONCLUSION_DATE" TIMESTAMP (6),
	"QUANTITY" NUMBER
   ) SEGMENT CREATION DEFERRED
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
 NOCOMPRESS LOGGING
  STORAGE(
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"   NO INMEMORY ;
--------------------------------------------------------
--  DDL for Table EXCHANGE_BUYER
--------------------------------------------------------

  CREATE TABLE "EXCHANGE_BUYER"
   (	"BUYER" VARCHAR2(20 BYTE),
	"QUANTITY" NUMBER,
	"EXCHANGE" NUMBER,
	"ITEM" VARCHAR2(20 BYTE)
   ) SEGMENT CREATION DEFERRED
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
 NOCOMPRESS LOGGING
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table EXCHANGE_CREATOR
--------------------------------------------------------

  CREATE TABLE "EXCHANGE_CREATOR"
   (	"CREATOR" VARCHAR2(20 BYTE),
	"EXCHANGE" NUMBER
   ) SEGMENT CREATION DEFERRED
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
 NOCOMPRESS LOGGING
  STORAGE(
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"   NO INMEMORY ;
--------------------------------------------------------
--  DDL for Table ITEM
--------------------------------------------------------

  CREATE TABLE "ITEM"
   (	"NAME" VARCHAR2(20 BYTE),
	"DESCRIPTION" VARCHAR2(60 BYTE),
	"CATEGORY" VARCHAR2(20 BYTE)
   ) SEGMENT CREATION DEFERRED
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
 NOCOMPRESS LOGGING
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table SERVICE
--------------------------------------------------------

  CREATE TABLE "SERVICE"
   (	"ID" NUMBER(*,0),
	"ITEM" VARCHAR2(20 BYTE),
	"TIME" NUMBER,
	"TIME_TYPE" VARCHAR2(20 BYTE),
	"PRICE" NUMBER,
	"POST_DATE" TIMESTAMP (6),
	"CONCLUSION_DATE" TIMESTAMP (6)
   ) SEGMENT CREATION DEFERRED
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
 NOCOMPRESS LOGGING
  STORAGE(
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"   NO INMEMORY ;
--------------------------------------------------------
--  DDL for Table SERVICE_CONTRACTOR
--------------------------------------------------------

  CREATE TABLE "SERVICE_CONTRACTOR"
   (	"CONTRACTOR" VARCHAR2(20 BYTE),
	"TIME" NUMBER,
	"SIMPLE" NUMBER
   ) SEGMENT CREATION DEFERRED
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
 NOCOMPRESS LOGGING
  STORAGE(
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"   NO INMEMORY ;
--------------------------------------------------------
--  DDL for Table SERVICE_CREATOR
--------------------------------------------------------

  CREATE TABLE "SERVICE_CREATOR"
   (	"CREATOR" VARCHAR2(20 BYTE),
	"SERVICE" NUMBER
   ) SEGMENT CREATION DEFERRED
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
 NOCOMPRESS LOGGING
  STORAGE(
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"   NO INMEMORY ;
--------------------------------------------------------
--  DDL for Table SIMPLE
--------------------------------------------------------

  CREATE TABLE "SIMPLE"
   (	"ID" NUMBER(*,0),
	"ITEM" VARCHAR2(20 BYTE),
	"PRICE" NUMBER,
	"POST_DATE" TIMESTAMP (6),
	"CONCLUSION_DATE" TIMESTAMP (6),
	"QUANTITY" NUMBER
   ) SEGMENT CREATION DEFERRED
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
 NOCOMPRESS LOGGING
  STORAGE(
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"   NO INMEMORY ;
--------------------------------------------------------
--  DDL for Table SIMPLE_BUYER
--------------------------------------------------------

  CREATE TABLE "SIMPLE_BUYER"
   (	"BUYER" VARCHAR2(20 BYTE),
	"QUANTITY" NUMBER,
	"SIMPLE" NUMBER
   ) SEGMENT CREATION DEFERRED
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
 NOCOMPRESS LOGGING
  STORAGE(
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"   NO INMEMORY ;
--------------------------------------------------------
--  DDL for Table SIMPLE_CREATOR
--------------------------------------------------------

  CREATE TABLE "SIMPLE_CREATOR"
   (	"CREATOR" VARCHAR2(20 BYTE),
	"SIMPLE" NUMBER
   ) SEGMENT CREATION DEFERRED
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
 NOCOMPRESS LOGGING
  STORAGE(
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"   NO INMEMORY ;
--------------------------------------------------------
--  DDL for Table USERS
--------------------------------------------------------

  CREATE TABLE "USERS"
   (	"ADDRESS" "T_ADDRESS" ,
	"PASSWORD" VARCHAR2(20 BYTE),
	"EMAIL" VARCHAR2(20 BYTE),
	"NAME" VARCHAR2(20 BYTE),
	"NICKNAME" VARCHAR2(20 BYTE),
	"PHONES" "T_PHONES"
   ) SEGMENT CREATION DEFERRED
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
 NOCOMPRESS LOGGING
  TABLESPACE "USERS" ;
REM INSERTING into C_PULGA.AUCTION
SET DEFINE OFF;
REM INSERTING into C_PULGA.AUCTION_BIDS
SET DEFINE OFF;
REM INSERTING into C_PULGA.AUCTION_CREATOR
SET DEFINE OFF;
REM INSERTING into C_PULGA.CATEGORIES
SET DEFINE OFF;
REM INSERTING into C_PULGA.DONATION
SET DEFINE OFF;
REM INSERTING into C_PULGA.DONATION_CREATOR
SET DEFINE OFF;
REM INSERTING into C_PULGA.DONATION_DONATEE
SET DEFINE OFF;
REM INSERTING into C_PULGA.EXCHANGE
SET DEFINE OFF;
REM INSERTING into C_PULGA.EXCHANGE_BUYER
SET DEFINE OFF;
REM INSERTING into C_PULGA.EXCHANGE_CREATOR
SET DEFINE OFF;
REM INSERTING into C_PULGA.ITEM
SET DEFINE OFF;
REM INSERTING into C_PULGA.SERVICE
SET DEFINE OFF;
REM INSERTING into C_PULGA.SERVICE_CONTRACTOR
SET DEFINE OFF;
REM INSERTING into C_PULGA.SERVICE_CREATOR
SET DEFINE OFF;
REM INSERTING into C_PULGA.SIMPLE
SET DEFINE OFF;
REM INSERTING into C_PULGA.SIMPLE_BUYER
SET DEFINE OFF;
REM INSERTING into C_PULGA.SIMPLE_CREATOR
SET DEFINE OFF;
REM INSERTING into C_PULGA.USERS
SET DEFINE OFF;
--------------------------------------------------------
--  DDL for Index AUCTION_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "AUCTION_PK" ON "AUCTION" ("ID")
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Index CATEGORIES_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "CATEGORIES_PK" ON "CATEGORIES" ("NAME")
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Index DONATION_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "DONATION_PK" ON "DONATION" ("ID")
  PCTFREE 10 INITRANS 2 MAXTRANS 255
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Index EXCHANGE_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "EXCHANGE_PK" ON "EXCHANGE" ("ID")
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Index ITEM_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "ITEM_PK" ON "ITEM" ("NAME")
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Index SERVICE_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "SERVICE_PK" ON "SERVICE" ("ID")
  PCTFREE 10 INITRANS 2 MAXTRANS 255
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Index SIMPLE_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "SIMPLE_PK" ON "SIMPLE" ("ID")
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Index USERS_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "USERS_PK" ON "USERS" ("EMAIL")
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  Constraints for Table ITEM
--------------------------------------------------------

  ALTER TABLE "ITEM" MODIFY ("NAME" NOT NULL ENABLE);
  ALTER TABLE "ITEM" MODIFY ("DESCRIPTION" NOT NULL ENABLE);
  ALTER TABLE "ITEM" MODIFY ("CATEGORY" NOT NULL ENABLE);
  ALTER TABLE "ITEM" ADD CONSTRAINT "ITEM_PK" PRIMARY KEY ("NAME")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS
  TABLESPACE "USERS"  ENABLE;
--------------------------------------------------------
--  Constraints for Table DONATION_CREATOR
--------------------------------------------------------

  ALTER TABLE "DONATION_CREATOR" MODIFY ("CREATOR" NOT NULL ENABLE);
  ALTER TABLE "DONATION_CREATOR" MODIFY ("DONATION" NOT NULL ENABLE);
--------------------------------------------------------
--  Constraints for Table DONATION
--------------------------------------------------------

  ALTER TABLE "DONATION" MODIFY ("ID" NOT NULL ENABLE);
  ALTER TABLE "DONATION" MODIFY ("ITEM" NOT NULL ENABLE);
  ALTER TABLE "DONATION" MODIFY ("POST_DATE" NOT NULL ENABLE);
  ALTER TABLE "DONATION" ADD CONSTRAINT "DONATION_PK" PRIMARY KEY ("ID")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255
  TABLESPACE "USERS"  ENABLE;
--------------------------------------------------------
--  Constraints for Table CATEGORIES
--------------------------------------------------------

  ALTER TABLE "CATEGORIES" MODIFY ("NAME" NOT NULL ENABLE);
  ALTER TABLE "CATEGORIES" ADD CONSTRAINT "CATEGORIES_PK" PRIMARY KEY ("NAME")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS
  TABLESPACE "USERS"  ENABLE;
--------------------------------------------------------
--  Constraints for Table SERVICE_CREATOR
--------------------------------------------------------

  ALTER TABLE "SERVICE_CREATOR" MODIFY ("CREATOR" NOT NULL ENABLE);
  ALTER TABLE "SERVICE_CREATOR" MODIFY ("SERVICE" NOT NULL ENABLE);
--------------------------------------------------------
--  Constraints for Table AUCTION
--------------------------------------------------------

  ALTER TABLE "AUCTION" MODIFY ("ID" NOT NULL ENABLE);
  ALTER TABLE "AUCTION" MODIFY ("POST_DATE" NOT NULL ENABLE);
  ALTER TABLE "AUCTION" MODIFY ("INITIAL_PRICE" NOT NULL ENABLE);
  ALTER TABLE "AUCTION" ADD CONSTRAINT "AUCTION_PK" PRIMARY KEY ("ID")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS
  TABLESPACE "USERS"  ENABLE;
  ALTER TABLE "AUCTION" MODIFY ("ITEM" NOT NULL ENABLE);
--------------------------------------------------------
--  Constraints for Table SIMPLE_CREATOR
--------------------------------------------------------

  ALTER TABLE "SIMPLE_CREATOR" MODIFY ("CREATOR" NOT NULL ENABLE);
  ALTER TABLE "SIMPLE_CREATOR" MODIFY ("SIMPLE" NOT NULL ENABLE);
--------------------------------------------------------
--  Constraints for Table EXCHANGE_CREATOR
--------------------------------------------------------

  ALTER TABLE "EXCHANGE_CREATOR" MODIFY ("CREATOR" NOT NULL ENABLE);
  ALTER TABLE "EXCHANGE_CREATOR" MODIFY ("EXCHANGE" NOT NULL ENABLE);
--------------------------------------------------------
--  Constraints for Table EXCHANGE
--------------------------------------------------------

  ALTER TABLE "EXCHANGE" MODIFY ("ID" NOT NULL ENABLE);
  ALTER TABLE "EXCHANGE" MODIFY ("ITEM" NOT NULL ENABLE);
  ALTER TABLE "EXCHANGE" MODIFY ("POST_DATE" NOT NULL ENABLE);
  ALTER TABLE "EXCHANGE" ADD CONSTRAINT "EXCHANGE_PK" PRIMARY KEY ("ID")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS
  TABLESPACE "USERS"  ENABLE;
--------------------------------------------------------
--  Constraints for Table SIMPLE
--------------------------------------------------------

  ALTER TABLE "SIMPLE" MODIFY ("ID" NOT NULL ENABLE);
  ALTER TABLE "SIMPLE" MODIFY ("ITEM" NOT NULL ENABLE);
  ALTER TABLE "SIMPLE" MODIFY ("PRICE" NOT NULL ENABLE);
  ALTER TABLE "SIMPLE" MODIFY ("POST_DATE" NOT NULL ENABLE);
  ALTER TABLE "SIMPLE" ADD CONSTRAINT "SIMPLE_PK" PRIMARY KEY ("ID")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS
  TABLESPACE "USERS"  ENABLE;
--------------------------------------------------------
--  Constraints for Table AUCTION_CREATOR
--------------------------------------------------------

  ALTER TABLE "AUCTION_CREATOR" MODIFY ("CREATOR" NOT NULL ENABLE);
  ALTER TABLE "AUCTION_CREATOR" MODIFY ("AUCTION" NOT NULL ENABLE);
--------------------------------------------------------
--  Constraints for Table SERVICE
--------------------------------------------------------

  ALTER TABLE "SERVICE" MODIFY ("ID" NOT NULL ENABLE);
  ALTER TABLE "SERVICE" MODIFY ("ITEM" NOT NULL ENABLE);
  ALTER TABLE "SERVICE" MODIFY ("TIME" NOT NULL ENABLE);
  ALTER TABLE "SERVICE" MODIFY ("TIME_TYPE" NOT NULL ENABLE);
  ALTER TABLE "SERVICE" MODIFY ("PRICE" NOT NULL ENABLE);
  ALTER TABLE "SERVICE" MODIFY ("POST_DATE" NOT NULL ENABLE);
  ALTER TABLE "SERVICE" ADD CONSTRAINT "SERVICE_PK" PRIMARY KEY ("ID")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255
  TABLESPACE "USERS"  ENABLE;
--------------------------------------------------------
--  Constraints for Table USERS
--------------------------------------------------------

  ALTER TABLE "USERS" MODIFY ("EMAIL" NOT NULL ENABLE);
  ALTER TABLE "USERS" ADD CONSTRAINT "USERS_PK" PRIMARY KEY ("EMAIL")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS
  TABLESPACE "USERS"  ENABLE;
  ALTER TABLE "USERS" MODIFY ("ADDRESS" NOT NULL ENABLE);
  ALTER TABLE "USERS" MODIFY ("NAME" NOT NULL ENABLE);
  ALTER TABLE "USERS" MODIFY ("NICKNAME" NOT NULL ENABLE);
  ALTER TABLE "USERS" MODIFY ("PHONES" NOT NULL ENABLE);
  ALTER TABLE "USERS" MODIFY ("PASSWORD" NOT NULL ENABLE);
--------------------------------------------------------
--  Ref Constraints for Table AUCTION
--------------------------------------------------------

  ALTER TABLE "AUCTION" ADD CONSTRAINT "ITEM" FOREIGN KEY ("ITEM")
	  REFERENCES "ITEM" ("NAME") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table AUCTION_BIDS
--------------------------------------------------------

  ALTER TABLE "AUCTION_BIDS" ADD CONSTRAINT "AUCTION_ID" FOREIGN KEY ("AUCTION")
	  REFERENCES "AUCTION" ("ID") ENABLE;
  ALTER TABLE "AUCTION_BIDS" ADD CONSTRAINT "BIDDER" FOREIGN KEY ("BIDDER")
	  REFERENCES "USERS" ("EMAIL") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table AUCTION_CREATOR
--------------------------------------------------------

  ALTER TABLE "AUCTION_CREATOR" ADD CONSTRAINT "CREATOR" FOREIGN KEY ("CREATOR")
	  REFERENCES "USERS" ("EMAIL") ENABLE;
  ALTER TABLE "AUCTION_CREATOR" ADD CONSTRAINT "AUCTION" FOREIGN KEY ("AUCTION")
	  REFERENCES "AUCTION" ("ID") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table DONATION
--------------------------------------------------------

  ALTER TABLE "DONATION" ADD CONSTRAINT "ITEMD" FOREIGN KEY ("ITEM")
	  REFERENCES "ITEM" ("NAME") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table DONATION_CREATOR
--------------------------------------------------------

  ALTER TABLE "DONATION_CREATOR" ADD CONSTRAINT "CREATOR3" FOREIGN KEY ("CREATOR")
	  REFERENCES "USERS" ("EMAIL") ENABLE;
  ALTER TABLE "DONATION_CREATOR" ADD CONSTRAINT "DONATION" FOREIGN KEY ("DONATION")
	  REFERENCES "DONATION" ("ID") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table DONATION_DONATEE
--------------------------------------------------------

  ALTER TABLE "DONATION_DONATEE" ADD CONSTRAINT "BUYER1" FOREIGN KEY ("BUYER")
	  REFERENCES "USERS" ("EMAIL") ENABLE;
  ALTER TABLE "DONATION_DONATEE" ADD CONSTRAINT "EXCHANGE_TABLE1" FOREIGN KEY ("QUANTITY")
	  REFERENCES "DONATION" ("ID") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table EXCHANGE
--------------------------------------------------------

  ALTER TABLE "EXCHANGE" ADD CONSTRAINT "ITEME" FOREIGN KEY ("ITEM")
	  REFERENCES "ITEM" ("NAME") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table EXCHANGE_BUYER
--------------------------------------------------------

  ALTER TABLE "EXCHANGE_BUYER" ADD CONSTRAINT "BUYER" FOREIGN KEY ("BUYER")
	  REFERENCES "USERS" ("EMAIL") ENABLE;
  ALTER TABLE "EXCHANGE_BUYER" ADD CONSTRAINT "EXCHANGE_TABLE" FOREIGN KEY ("EXCHANGE")
	  REFERENCES "EXCHANGE" ("ID") ENABLE;
  ALTER TABLE "EXCHANGE_BUYER" ADD CONSTRAINT "ITEM_OFFERED" FOREIGN KEY ("ITEM")
	  REFERENCES "ITEM" ("NAME") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table EXCHANGE_CREATOR
--------------------------------------------------------

  ALTER TABLE "EXCHANGE_CREATOR" ADD CONSTRAINT "EXCHANGE" FOREIGN KEY ("EXCHANGE")
	  REFERENCES "EXCHANGE" ("ID") ENABLE;
  ALTER TABLE "EXCHANGE_CREATOR" ADD CONSTRAINT "CREATOR1" FOREIGN KEY ("CREATOR")
	  REFERENCES "USERS" ("EMAIL") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table ITEM
--------------------------------------------------------

  ALTER TABLE "ITEM" ADD CONSTRAINT "CATEGORY" FOREIGN KEY ("CATEGORY")
	  REFERENCES "CATEGORIES" ("NAME") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table SERVICE_CONTRACTOR
--------------------------------------------------------

  ALTER TABLE "SERVICE_CONTRACTOR" ADD CONSTRAINT "BUYER3" FOREIGN KEY ("CONTRACTOR")
	  REFERENCES "USERS" ("EMAIL") ENABLE;
  ALTER TABLE "SERVICE_CONTRACTOR" ADD CONSTRAINT "CONTRACTOR" FOREIGN KEY ("SIMPLE")
	  REFERENCES "SERVICE" ("ID") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table SERVICE_CREATOR
--------------------------------------------------------

  ALTER TABLE "SERVICE_CREATOR" ADD CONSTRAINT "CREATOR4" FOREIGN KEY ("CREATOR")
	  REFERENCES "USERS" ("EMAIL") ENABLE;
  ALTER TABLE "SERVICE_CREATOR" ADD CONSTRAINT "SIMPLE1" FOREIGN KEY ("SERVICE")
	  REFERENCES "SERVICE" ("ID") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table SIMPLE
--------------------------------------------------------

  ALTER TABLE "SIMPLE" ADD CONSTRAINT "ITEMS" FOREIGN KEY ("ITEM")
	  REFERENCES "ITEM" ("NAME") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table SIMPLE_BUYER
--------------------------------------------------------

  ALTER TABLE "SIMPLE_BUYER" ADD CONSTRAINT "BUYER2" FOREIGN KEY ("BUYER")
	  REFERENCES "USERS" ("EMAIL") ENABLE;
  ALTER TABLE "SIMPLE_BUYER" ADD CONSTRAINT "EXCHANGE_TABLE2" FOREIGN KEY ("SIMPLE")
	  REFERENCES "SIMPLE" ("ID") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table SIMPLE_CREATOR
--------------------------------------------------------

  ALTER TABLE "SIMPLE_CREATOR" ADD CONSTRAINT "CREATOR2" FOREIGN KEY ("CREATOR")
	  REFERENCES "USERS" ("EMAIL") ENABLE;
  ALTER TABLE "SIMPLE_CREATOR" ADD CONSTRAINT "SIMPLE" FOREIGN KEY ("SIMPLE")
	  REFERENCES "SIMPLE" ("ID") ENABLE;
