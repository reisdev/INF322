import os
import cx_Oracle
from django.apps import AppConfig
from django.conf import settings

module_dir = os.path.dirname(__file__)
script_path = os.path.join(module_dir, 'scripts.sql')

class SetDatabase:
    config = settings.DATABASES["default"]
    script = {}
    def __init__(self):
        file = open(script_path,"r")
        self.script = file.read()
        self.con = cx_Oracle.connect("%s/%s@%s"%(self.config["USER"], self.config["PASSWORD"],self.config["NAME"]))
        

class PulgaConfig(AppConfig):
    name = 'pulga'
    def ready(self):
        db = SetDatabase()
        for q in db.script.split("/"):
            print(len(q))
            if(len(q) < 5):
                continue
            try:    
                c = db.con.cursor()
                print(q)
                c.execute(q)
            except IOError: 
                    print("An error has ocurred")    
        db.con.close()
        self.testInsert()

    def testInsert(self):
        db = SetDatabase()
        c = db.con.cursor()
        c.execute("INSERT INTO USERS (email,fullname,nickname,addresses,phones) VALUES ('matheusdrdj@gmail.com','Matheus dos Reis de Jesus','mthrsj',addresses(address(501,'14','Promissão II','Lagoa Santa')),phones('31993102771'))")
        db.con.commit()
        print("Insert method tested!")
        db.con.close()

        

