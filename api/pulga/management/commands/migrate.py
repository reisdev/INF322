import os
import cx_Oracle
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

module_dir = os.path.dirname(__file__)
script_path = os.path.join(module_dir, '../../scripts.sql')

class Database:
    config = settings.DATABASES["default"]
    script = {}
    def __init__(self):
        file = open(script_path,"r")
        self.script = file.read()
        self.con = cx_Oracle.connect("%s/%s@%s"%(self.config["USER"], self.config["PASSWORD"],self.config["NAME"]))
    def migrateDatabase(self):
        for q in self.script.split("/"):
            if(len(q) < 5):
                continue
            try:    
                c = self.con.cursor()
                c.execute(q)
            except IOError: 
                    print("An error has ocurred")    
        self.con.close()
    def testInsert(self):
        c = self.con.cursor()
        c.execute("INSERT INTO USERS (email,fullname,nickname,addresses,phones) VALUES ('matheusdrdj@gmail.com','Matheus dos Reis de Jesus','mthrsj',addresses(address(501,'14','Promissão II','Lagoa Santa')),phones('31993102771'))")
        self.con.commit()
        print("Insert method tested!")
        self.con.close()

class Command(BaseCommand):
    help = 'Run the Oracle Database migrations'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        return
        db = Database()
        db.migrateDatabase()
        self.stdout.write(self.style.SUCCESS('Successfully migrated the Database'))