import pyodbc
server = 'HCL-02-12\SQLEXPRESS'
database = 'FileSearchResults'
username = 'Capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
class employee_schema:
    def employe_table(self):
        try:
            query1 = cursor.execute('''use FileSearchResults''')
            query2 = cursor.execute('''create table EmpDetails
                                               (
                                               EName varchar(50),
                                               Eid int NOT NULL
                                               project varchar(50),
                                               salary int,
                                               primary key (Eid)
                                               )
                                               ''')
            query3 = cursor.execute('''select * from EmpDetails''')
            cnxn.commit()
            print("Table created sucessfully")
        except:
            print("Table Existed")
obj=employee_schema()
obj.employe_table()