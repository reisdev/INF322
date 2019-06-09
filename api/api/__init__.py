
import cx_Oracle

class Migrations:
    def __init__(self):
        self.scripts = {}
        self.connection = cx_Oracle.connect("warmachine/")    
    def userMigration(self):
        self.scripts["users"] = "\
            CREATE TYPE phone AS OBJECT (\
                num VARCHAR(15)\
            )\
            CREATE TYPE user AS OBJECT ( \
                email VARCHAR(30),       \
                fullName VARCHAR(50)     \
                nickname VARCHAR(15)     \
                address ROW(             \
                    number CHAR(6),      \
                    street VARCHAR(20),  \
                    nbHood VARCHAR(20)   \
                ),                       \
                phoneNumbers phone       \
            )                            \
            CREATE TABLE USERS OF TYPE user \
            NESTED TABLE phoneNumbers as phoneTable \
           "

    def saleMigration(self):
        self.scripts["sales"] = "\
            CREATE TABLE (    \
                id INTEGER NOT NULL,        \
                timeLeft INTEGER,           \
                soldPrice FLOAT,            \
                initialPrice FLOAT,         \
                postDate TIMESTAMP NOT NULL,\
                done NUMBER(1) \
                conclusion DATE             \
            )                               \
        "

    def itemMigration(self):
        self.scripts["item"] = "\
            CREATE TABLE items ( \
                id INTEGER,              \
                name VARCHAR(30)         \
            )                            \
        "