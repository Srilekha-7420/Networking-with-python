import Employee_DB                      #Accessing Employee_DB classes and Methods
import pyodbc                            #pyodbc is going to be the bridge between SQL and Python
server = 'HCL-02-12\SQLEXPRESS'
database = 'FileSearchResults'
username = 'Capstone'
password = 'Capstone@123'
#database connectivity
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
#cursor object for executing sql statements
cursor=cnxn.cursor()
#Custom Exceptions
class ExistingError(Exception):
    pass
class RangeError(Exception):
    pass
class Employee_data:                                    #creating class for employee details
    Bonus=2
    Projects=['Python','C','Java']
    def __init__(self,Name,Salary,Project,Emp_Id):      #class constructor:intializing the instance variables
        self.Name=Name
        self.Salary=Salary
        self.Project=Project
        self.Emp_Id=Emp_Id

    # inserting values into table
    def insert_Values_to_Table(self):
        try:                                        #try block is used to check some code for errors
            query = '''
            INSERT INTO EmpDetails(Name,Salary,Project,Emp_Id)
            VALUES
            ('{0}',{1},'{2}',{3})  '''

            insertQuery=query.format(self.Name,self.Salary,self.Project,self.Emp_Id)
            cursor.execute(insertQuery)
            cnxn.commit()
            print(" row inserted")
        except:                                     #except is used to handle the exception
            print("Primary key not accept the same values")

    # updating salary in the table
    def Update_Salary(self,New_Salary,Name):
        try:
            self.New_Salary=New_Salary
            self.Name=Name
            if self.New_Salary!= self.Salary:
                Query = '''
                Update EmpDetails SET Salary ='{0}' WHERE Name = '{1}'
                '''
                updateQuery = Query.format(New_Salary,self.Name)
                cursor.execute(updateQuery)
                cursor.commit()
            else:
                raise ExistingError              #programmatically generate an exception to indicate an error condition.
        except ExistingError:
            print("No Change in Salary")

     # add the bonus value to the salary
    def Add_Bonus(self,bonus,Name):
        self.bonus=bonus
        self.Name=Name
        try:
            if self.bonus not in range(1,self.Bonus+1):
                raise RangeError
            else:
                self.Salary=self.Salary+self.Salary*self.bonus
                Query = '''
                        Update Empdetails SET Salary ='{0}' WHERE Name = '{1}'
                                                                '''
                Query1 = Query.format(self.Salary,self.Name)
                cursor.execute(Query1)
                cursor.commit()
        except RangeError:
            print("Bonus is Not in Range")

    # used to change the project of employee
    def Change_Project(self,project,Name):
        self.project=project
        self.Name=Name

        if self.project in self.Projects:
            if self.project == self.Project:
                print("Project is Already exists")
            else:
                Query = ''' Update Empdetails SET Project ='{0}' WHERE Name = '{1}' '''
                updateQuery = Query.format(project, Name)
                cursor.execute(updateQuery)
                cursor.commit()
        else:
            print("Project is not in list")

    # used to display the details of employee
    def Display_details(self):
        query=''' select * from Empdetails WHERE Name='{0}' '''
        query1=query.format(self.Name)
        values=cursor.execute(query1)
        for details in values:
            print("Name:{0}  Salary:{1}  Project:{2}".format(details.Name,details.Salary,details.Project))

    #used to delete the values from employee table
    def Delete_Employee_table(self):
        Query = ''' delete from Empdetails where Name='Srilekha'  '''
        cursor.execute(Query)
        cursor.commit()
        print("Employee has been deleted")

obj1=Employee_data('Srilekha',20000,'Python',1) #creating object for Employee_data class
obj1.insert_Values_to_Table()
obj=Employee_DB.employee_schema()               #creating object for employee_schema of Employee_DB file
obj.employe_table()
obj1.insert_Values_to_Table()
obj1.Update_Salary(25000,'Srilekha')
obj1.Add_Bonus(1,'Srilekha')
obj1.Change_Project('c','python')
obj1.Display_details()
#obj1.Delete_Employee_table()