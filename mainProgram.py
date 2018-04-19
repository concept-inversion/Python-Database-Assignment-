import json
from databaseModule import DB_connect
from crudController import CRUD
import dis
import os


class Program():
    def __init__(self, *args, **kwargs):
        self.crud = CRUD()

    def Delete(self):
        # [Column name] [operation][cond]
        cond = input("[Delete]Enter the query starting from column name: ")
        self.crud.Delete(cond)

    def Insert(self):
        format = {
        "Bio": "",
        "Name": "",
        "Dob": "",
        "Gender": "",
        "Image": "",
        "Longitude": "",
        "Phone": "",
        "Link": "",
        "Address": "",
        "Latitude": "",
        "Email": ""
        }
        for key in format:
            format[key]= input("Enter the  "+key )
        self.crud.Create(format)

    def Update(self):
        # [Column name] [operation][cond]
        cond = input("[Update]Enter the query starting from column name: ")
        self.crud.Read(cond)

    def Select(self):
        # [Column name] [operation][cond]
        cond = input("[Select]Enter the query starting from column name: ")
        print("read called")
        output = self.crud.Read(cond)
        print("data retrieved")
        print(output.fetchall())
        if output:
            for each in output:
                print (each)

        else:
            print("no data")
        return output
    
    def upload_json(self):
        data = input("Enter json file: ")
        self.crud.JsonLoader(data)
        

if __name__== '__main__':
    new = Program()
    options = [None,new.Insert,new.Select,new.Update,new.Delete,new.upload_json]
    while True:
        action = int(input(
            '''
            Press 1 to Insert
            Press 2 to Select
            Press 3 to Update
            Press 4 to Delete
            Press 5 to Load JSON
            Press 0 to exit
            '''
        ))
        if(action==0):
            break
        else:
            options[action]()
        

