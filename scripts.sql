--------------------------------------------------------
--  Arquivo criado - Sexta-feira-Junho-21-2019
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Type T_ADDRESS
--------------------------------------------------------

CREATE OR REPLACE NONEDITIONABLE TYPE "T_ADDRESS" FORCE AS OBJECT
(
  num      INTEGER,
  street   VARCHAR2(60),
  district VARCHAR2(60),
  city     VARCHAR2(60)
)

/

--------------------------------------------------------
--  DDL for Type T_LIST_ADDRESS
--------------------------------------------------------

CREATE OR REPLACE TYPE "T_LIST_ADDRESS" as TABLE of "T_ADDRESS";

/

--------------------------------------------------------
--  DDL for Type T_PHONES
--------------------------------------------------------

CREATE OR REPLACE NONEDITIONABLE TYPE "T_PHONES" IS VARRAY (2) OF VARCHAR(15)

/

--------------------------------------------------------
--  DDL for Type T_USER
--------------------------------------------------------

CREATE OR REPLACE TYPE "T_USER" AS OBJECT
(
  "ADDRESSES"  "T_LIST_ADDRESS",
  "PASSWORD" VARCHAR2(60 BYTE),
  "EMAIL"    VARCHAR2(60 BYTE),
  "NAME"     VARCHAR2(60 BYTE),
  "NICKNAME" VARCHAR2(60 BYTE),
  "PHONES"   "T_PHONES"
)
/

--------------------------------------------------------
--  DDL for Type T_CATEGORIES
--------------------------------------------------------

CREATE OR REPLACE TYPE "T_CATEGORIES" AS OBJECT
(
  "NAME"        VARCHAR2(60 BYTE),
  "DESCRIPTION" VARCHAR2(50 BYTE)
)
/

--------------------------------------------------------
--  DDL for Table CATEGORIES
--------------------------------------------------------

CREATE TABLE "CATEGORIES" of "T_CATEGORIES"
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
  NOCOMPRESS LOGGING
  TABLESPACE "USERS";

--------------------------------------------------------
--  DDL for Type T_ITEM
--------------------------------------------------------

CREATE OR REPLACE TYPE "T_ITEM" AS OBJECT
(
  "NAME"        VARCHAR2(60 BYTE),
  "DESCRIPTION" VARCHAR2(60 BYTE),
  "CATEGORY"    REF "T_CATEGORIES"
)
/

--------------------------------------------------------
--  DDL for Table ITEM
--------------------------------------------------------

CREATE TABLE "ITEM" of "T_ITEM"
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
  NOCOMPRESS LOGGING
  TABLESPACE "USERS";

--------------------------------------------------------
--  DDL for Type T_BASE_SALE
--------------------------------------------------------

CREATE OR REPLACE TYPE "T_BASE_SALE" AS OBJECT
(
  "ID"              NUMBER,
  "POST_DATE"       TIMESTAMP,
  "CONCLUSION_DATE" DATE,
  "DURATION"        NUMBER,
  "CREATOR"         REF "T_USER"
) NOT FINAL;

/
--------------------------------------------------------
--  DDL for Type T_SIMPLE
--------------------------------------------------------

CREATE OR REPLACE TYPE "T_SIMPLE" UNDER "T_BASE_SALE"
(
  "ITEM"            REF "T_ITEM",
  "PRICE"           NUMBER,
  "QUANTITY"        NUMBER
)

/

--------------------------------------------------------
--  DDL for Type T_AUCTION
--------------------------------------------------------

CREATE OR REPLACE TYPE "T_AUCTION" UNDER "T_BASE_SALE"
(
  "ITEM"            REF "T_ITEM",
  "MINIMUM_OFFER"   NUMBER
)

/

--------------------------------------------------------
--  DDL for Type T_DONATION
--------------------------------------------------------

CREATE OR REPLACE TYPE "T_DONATION" UNDER "T_BASE_SALE"
(
  "ITEM"            REF "T_ITEM",
  "QUANTITY"        NUMBER
)

/

--------------------------------------------------------
--  DDL for Type T_EXCHAGE
--------------------------------------------------------

CREATE OR REPLACE TYPE "T_EXCHANGE" UNDER "T_BASE_SALE"
(
  "ITEM"            REF "T_ITEM",
  "QUANTITY"        NUMBER
)

/

--------------------------------------------------------
--  DDL for Type T_SERVICE
--------------------------------------------------------

CREATE OR REPLACE TYPE "T_SERVICE" UNDER "T_BASE_SALE"
(
  "ITEM"            REF "T_ITEM",
  "TIME"            NUMBER,
  "TIME_TYPE"       VARCHAR2(60 BYTE),
  "PRICE"           NUMBER
)

/
--------------------------------------------------------
--  DDL for Table AUCTION
--------------------------------------------------------

CREATE TABLE "AUCTION" OF "T_AUCTION"
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
  NOCOMPRESS LOGGING
  TABLESPACE "USERS";

--------------------------------------------------------
--  DDL for Table AUCTION_BIDS
--------------------------------------------------------

CREATE TABLE "AUCTION_BIDS"
(
  "BIDDER"     REF "T_USER",
  "AUCTION"    NUMBER,
  "VALUE"      NUMBER,
  "OFFER_DATE" DATE
)
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
  NOCOMPRESS LOGGING
  TABLESPACE "USERS";

--------------------------------------------------------
--  DDL for Table DONATION
--------------------------------------------------------

CREATE TABLE "DONATION" OF "T_DONATION"
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
  NOCOMPRESS LOGGING
  STORAGE
(
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT
)
  TABLESPACE "USERS" NO INMEMORY;

--------------------------------------------------------
--  DDL for Table DONATION_DONATEE
--------------------------------------------------------

CREATE TABLE "DONATION_DONATEE"
(
  "BUYER"    REF "T_USER",
  "QUANTITY" NUMBER,
  "DONATION" NUMBER,
  "OFFER_DATE" DATE,
)
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
  NOCOMPRESS LOGGING
  STORAGE
(
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT
)
  TABLESPACE "USERS" NO INMEMORY;
--------------------------------------------------------
--  DDL for Table EXCHANGE
--------------------------------------------------------

CREATE TABLE "EXCHANGE" OF "T_EXCHANGE"
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
  NOCOMPRESS LOGGING
  STORAGE
(
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT
)
  TABLESPACE "USERS" NO INMEMORY;
--------------------------------------------------------
--  DDL for Table EXCHANGE_BUYER
--------------------------------------------------------

CREATE TABLE "EXCHANGE_BUYER"
(
  "BUYER"    REF "T_USER",
  "GIVING_QUANTITY" NUMBER,
  "RECEIVING_QUANTITY" NUMBER,
  "EXCHANGE" NUMBER,
  "ITEM"     REF "T_ITEM",
  "OFFER_DATE" DATE,
)
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
  NOCOMPRESS LOGGING
  TABLESPACE "USERS";


--------------------------------------------------------
--  DDL for Table SERVICE
--------------------------------------------------------

CREATE TABLE "SERVICE" OF "T_SERVICE"
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
  NOCOMPRESS LOGGING
  STORAGE
(
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT
)
  TABLESPACE "USERS" NO INMEMORY;
--------------------------------------------------------
--  DDL for Table SERVICE_CONTRACTOR
--------------------------------------------------------

CREATE TABLE "SERVICE_CONTRACTOR"
(
  "CONTRACTOR" REF "T_USER",
  "TIME"       NUMBER,
  "SERVICE"     NUMBER,
  "OFFER_DATE" DATE
)
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
  NOCOMPRESS LOGGING
  STORAGE
(
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT
)
  TABLESPACE "USERS" NO INMEMORY;

--------------------------------------------------------
--  DDL for Table SIMPLE
--------------------------------------------------------

CREATE TABLE "SIMPLE" OF "T_SIMPLE"
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
  NOCOMPRESS LOGGING
  STORAGE
(
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT
)
  TABLESPACE "USERS" NO INMEMORY;
--------------------------------------------------------
--  DDL for Table SIMPLE_BUYER
--------------------------------------------------------

CREATE TABLE "SIMPLE_BUYER"
(
  "BUYER"    REF "T_USER",
  "QUANTITY" NUMBER,
  "SIMPLE"   NUMBER,
  "OFFER_DATE" DATE
)
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
  NOCOMPRESS LOGGING
  STORAGE
(
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT
)
  TABLESPACE "USERS" NO INMEMORY;

--------------------------------------------------------
--  DDL for Table USERS
--------------------------------------------------------

CREATE TABLE "USERS" of "T_USER" NESTED TABLE addresses STORE AS tabAddresses
PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING TABLESPACE "USERS";

REM INSERTING INTO AUCTION

SET DEFINE OFF;

REM INSERTING INTO AUCTION_BIDS
SET DEFINE OFF;

REM INSERTING INTO CATEGORIES
SET DEFINE OFF;

REM INSERTING INTO DONATION
SET DEFINE OFF;

REM INSERTING INTO DONATION_DONATEE
SET DEFINE OFF;

REM INSERTING INTO EXCHANGE
SET DEFINE OFF;

REM INSERTING INTO EXCHANGE_BUYER
SET DEFINE OFF;

REM INSERTING INTO ITEM
SET DEFINE OFF;

REM INSERTING INTO SERVICE
SET DEFINE OFF;

REM INSERTING INTO SERVICE_CONTRACTOR
SET DEFINE OFF;

REM INSERTING INTO SIMPLE
SET DEFINE OFF;

REM INSERTING INTO SIMPLE_BUYER
SET DEFINE OFF;

REM INSERTING INTO USERS
SET DEFINE OFF;

--------------------------------------------------------
--  DDL for Index AUCTION_PK
--------------------------------------------------------

CREATE UNIQUE INDEX "AUCTION_PK" ON "AUCTION" ("ID") PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS TABLESPACE "USERS";

--------------------------------------------------------
--  DDL for Index CATEGORIES_PK
--------------------------------------------------------

CREATE UNIQUE INDEX "CATEGORIES_PK" ON "CATEGORIES" ("NAME") PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS TABLESPACE "USERS";

--------------------------------------------------------
--  DDL for Index DONATION_PK
--------------------------------------------------------

CREATE UNIQUE INDEX "DONATION_PK" ON "DONATION" ("ID") PCTFREE 10 INITRANS 2 MAXTRANS 255 TABLESPACE "USERS";

--------------------------------------------------------
--  DDL for Index EXCHANGE_PK
--------------------------------------------------------

CREATE UNIQUE INDEX "EXCHANGE_PK" ON "EXCHANGE" ("ID") PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS TABLESPACE "USERS";

--------------------------------------------------------
--  DDL for Index ITEM_PK
--------------------------------------------------------

CREATE UNIQUE INDEX "ITEM_PK" ON "ITEM" ("NAME") PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS TABLESPACE "USERS";

--------------------------------------------------------
--  DDL for Index SERVICE_PK
--------------------------------------------------------

CREATE UNIQUE INDEX "SERVICE_PK" ON "SERVICE" ("ID") PCTFREE 10 INITRANS 2 MAXTRANS 255 TABLESPACE "USERS";

--------------------------------------------------------
--  DDL for Index SIMPLE_PK
--------------------------------------------------------

CREATE UNIQUE INDEX "SIMPLE_PK" ON "SIMPLE" ("ID") PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS TABLESPACE "USERS";

--------------------------------------------------------
--  DDL for Index USERS_PK
--------------------------------------------------------

CREATE UNIQUE INDEX "USERS_PK" ON "USERS" ("EMAIL") PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS TABLESPACE "USERS";

--------------------------------------------------------
--  Constraints for Table ITEM
--------------------------------------------------------

ALTER TABLE "ITEM" MODIFY ("NAME" NOT NULL ENABLE);

ALTER TABLE "ITEM" MODIFY ("DESCRIPTION" NOT NULL ENABLE);

ALTER TABLE "ITEM" MODIFY ("CATEGORY" NOT NULL ENABLE);

ALTER TABLE "ITEM" ADD CONSTRAINT "ITEM_PK" PRIMARY KEY ("NAME")
USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS TABLESPACE "USERS" ENABLE;

--------------------------------------------------------
--  Constraints for Table DONATION
--------------------------------------------------------

ALTER TABLE "DONATION" MODIFY ("ID" NOT NULL ENABLE);

ALTER TABLE "DONATION" MODIFY ("POST_DATE" NOT NULL ENABLE);

ALTER TABLE "DONATION" ADD CONSTRAINT "DONATION_PK" PRIMARY KEY ("ID")
USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 TABLESPACE "USERS" ENABLE;

--------------------------------------------------------
--  Constraints for Table CATEGORIES
--------------------------------------------------------

ALTER TABLE "CATEGORIES" MODIFY ("NAME" NOT NULL ENABLE);

ALTER TABLE "CATEGORIES" ADD CONSTRAINT "CATEGORIES_PK" PRIMARY KEY ("NAME")
USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS TABLESPACE "USERS" ENABLE;

--------------------------------------------------------
--  Constraints for Table AUCTION
--------------------------------------------------------

ALTER TABLE "AUCTION" MODIFY ("ID" NOT NULL ENABLE);

ALTER TABLE "AUCTION" MODIFY ("POST_DATE" NOT NULL ENABLE);

ALTER TABLE "AUCTION" MODIFY ("MINIMUM_OFFER" NOT NULL ENABLE);

ALTER TABLE "AUCTION" ADD CONSTRAINT "AUCTION_PK" PRIMARY KEY ("ID")
USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS TABLESPACE "USERS" ENABLE;

--------------------------------------------------------
--  Constraints for Table EXCHANGE
--------------------------------------------------------

ALTER TABLE "EXCHANGE" MODIFY ("ID" NOT NULL ENABLE);

ALTER TABLE "EXCHANGE" MODIFY ("POST_DATE" NOT NULL ENABLE);

ALTER TABLE "EXCHANGE" ADD CONSTRAINT "EXCHANGE_PK" PRIMARY KEY ("ID")
USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS TABLESPACE "USERS" ENABLE;

--------------------------------------------------------
--  Constraints for Table SIMPLE
--------------------------------------------------------

ALTER TABLE "SIMPLE" MODIFY ("ID" NOT NULL ENABLE);

ALTER TABLE "SIMPLE" MODIFY ("PRICE" NOT NULL ENABLE);

ALTER TABLE "SIMPLE" MODIFY ("POST_DATE" NOT NULL ENABLE);

ALTER TABLE "SIMPLE" ADD CONSTRAINT "SIMPLE_PK" PRIMARY KEY ("ID")
USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS TABLESPACE "USERS" ENABLE;

--------------------------------------------------------
--  Constraints for Table SERVICE
--------------------------------------------------------

ALTER TABLE "SERVICE" MODIFY ("ID" NOT NULL ENABLE);

ALTER TABLE "SERVICE" MODIFY ("TIME" NOT NULL ENABLE);

ALTER TABLE "SERVICE" MODIFY ("TIME_TYPE" NOT NULL ENABLE);

ALTER TABLE "SERVICE" MODIFY ("PRICE" NOT NULL ENABLE);

ALTER TABLE "SERVICE" MODIFY ("POST_DATE" NOT NULL ENABLE);

ALTER TABLE "SERVICE" ADD CONSTRAINT "SERVICE_PK" PRIMARY KEY ("ID") USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 TABLESPACE "USERS" ENABLE;

--------------------------------------------------------
--  Constraints for Table USERS
--------------------------------------------------------

ALTER TABLE "USERS" MODIFY ("EMAIL" NOT NULL ENABLE);

ALTER TABLE "USERS" ADD CONSTRAINT "USERS_PK" PRIMARY KEY ("EMAIL") USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS TABLESPACE "USERS" ENABLE;

ALTER TABLE "USERS" MODIFY ("NAME" NOT NULL ENABLE);

ALTER TABLE "USERS" MODIFY ("NICKNAME" NOT NULL ENABLE);

ALTER TABLE "USERS" MODIFY ("PHONES" NOT NULL ENABLE);

ALTER TABLE "USERS" MODIFY ("PASSWORD" NOT NULL ENABLE);

--------------------------------------------------------
--  Ref Constraints for Table AUCTION_BIDS
--------------------------------------------------------

ALTER TABLE "AUCTION_BIDS" ADD CONSTRAINT "AUCTION_ID"
FOREIGN KEY ("AUCTION") REFERENCES "AUCTION" ("ID") ENABLE;

--------------------------------------------------------
--  Ref Constraints for Table DONATION_DONATEE
--------------------------------------------------------

ALTER TABLE "DONATION_DONATEE" ADD CONSTRAINT "EXCHANGE_TABLE1"
FOREIGN KEY ("DONATION") REFERENCES "DONATION" ("ID") ENABLE;

--------------------------------------------------------
--  Ref Constraints for Table EXCHANGE_BUYER
--------------------------------------------------------

ALTER TABLE "EXCHANGE_BUYER" ADD CONSTRAINT "EXCHANGE_TABLE"
FOREIGN KEY ("EXCHANGE") REFERENCES "EXCHANGE" ("ID") ENABLE;

--------------------------------------------------------
--  Ref Constraints for Table SERVICE_CONTRACTOR
--------------------------------------------------------

ALTER TABLE "SERVICE_CONTRACTOR" ADD CONSTRAINT "CONTRACTOR"
FOREIGN KEY ("SERVICE") REFERENCES "SERVICE" ("ID") ENABLE;

--------------------------------------------------------
--  Ref Constraints for Table SIMPLE_BUYER
--------------------------------------------------------

ALTER TABLE "SIMPLE_BUYER" ADD CONSTRAINT "EXCHANGE_TABLE2"
FOREIGN KEY ("SIMPLE") REFERENCES "SIMPLE" ("ID") ENABLE;

--------------------------------------------------------
--  Default insertions do CATEGORIES
--------------------------------------------------------

INSERT INTO CATEGORIES (NAME, DESCRIPTION)
VALUES ('Tecnologia', 'Produtos tecnologicos para o seu lar');
/
INSERT INTO CATEGORIES (NAME, DESCRIPTION)
VALUES ('Eletrodomesticos', 'Eletrodomesticos para o seu lar');
/
INSERT INTO CATEGORIES (NAME, DESCRIPTION)
VALUES ('Jardinagem', 'Conjuntos de jardinagem para o seu lar');
/
INSERT INTO CATEGORIES (NAME, DESCRIPTION)
VALUES ('Brinquedos', 'Brinquedos para o seu lar');
/
COMMIT WORK;
