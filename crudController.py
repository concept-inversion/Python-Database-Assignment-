import json
from databaseModule import DB_connect
from postgreModule import Postgre_db
#generate query from user input
class CRUD():
    '''
    Class to implement CRUD functionality:
    1. Create(self, each)
        Inserts data in the database.
        each -> Python dict input
    2. Update(self,param)
        Updates  columns 
    3. Read(self, param)
    
    4. Delete(self,param)
    
    5. View(self, param)

    6. Jsonloader(self, data)
    
    '''
    
    def __init__(self, select):
        # use without self
        if select == 1:
            self.db = DB_connect('mysql.db') 
            print("SQL")
        elif select ==2:
            self.db = Postgre_db()
            print("PostgreSQL")
        else:
            print("No Choice selected. Default = PostgreSQL")
            self.db= Postgre_db()

    def Create(self,data):
        self.db.Create(data)
        print("Create operation Successful")

    def Update(self,param):
        statement= 'UPDATE PEOPLE SET %s'% (param)
        print(statement)
        data=self.db.executeDB(statement,param)
        print("Data Updated")
        return data 

    def Read(self, param):
        statement= ' SELECT * FROM PEOPLE WHERE (%s)'% (param)
        data=self.db.executeDB(statement,param)
        if data:
            return data.fetchall()
    
    def View(self,param=[]):
        statement= ' SELECT * FROM PEOPLE ' 
        data=self.db.executeDB(statement,param)
        if data:
            return data

    def Delete(self, param):
        statement= 'DELETE FROM PEOPLE WHERE (%s)'%(param)
        data=self.db.executeDB(statement,param)
        return data

    def JsonLoader(self,data):
        self.db.JsonLoader(data)
        print("JSON uploaded")
    
    def close(self):
        self.db.closeDB()


