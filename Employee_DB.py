import pyodbc                    #pyodbc is going to be the bridge between SQL and Python
server = 'HCL-02-12\SQLEXPRESS'
database = 'FileSearchResults'
username = 'Capstone'
password = 'Capstone@123'
#database connectivity
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
#cursor object for executing sql statements
cursor = cnxn.cursor()

#creating class employee_schema
class employee_schema:
    def employe_table(self):                    #creating EmpDetails table
        try:
            query1 = cursor.execute('''use FileSearchResults''')    #To Execute sql query for "using the database"
            query2 = cursor.execute('''create table EmpDetails
                                               (
                                               Emp_Id int NOT NULL,
                                               Name varchar(50),
                                               project varchar(50),
                                               salary int,
                                               primary key (Emp_Id)
                                               )
                                               ''')
            query3 = cursor.execute('''select * from EmpDetails''')

            #used to confirm the changes made by the user
            cnxn.commit()
            print("Table created sucessfully")
        except:
            print("Table Existed")
obj=employee_schema()       #creating object for employee_schema class
obj.employe_table()         #calling the employe_table function by using object