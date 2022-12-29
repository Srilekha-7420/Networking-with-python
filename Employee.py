import EmpSch
import pyodbc
server = 'HCL-02-12\SQLEXPRESS'
database = 'FileSearchResults'
username = 'Capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor=cnxn.cursor()
class ExistingError(Exception):
    pass
class RangeError(Exception):
    pass
class Employee_data:
    Bonus=2
    Projects=['Python','C','Java']
    def __init__(self,EName,Eid,Project,Salary):
        self.EName=EName
        self.Eid=Eid
        self.Project=Project
        self.Salary=Salary


    def insert_Values_to_Table(self):
        try:
            query = '''
            INSERT INTO EmpDetails(EName,Eid,Salary,Project)
            VALUES
            ('{0}',{1},'{2}',{3})  '''

            insertQuery=query.format(self.EName,self.Eid,self.Salary,self.Project)
            cursor.execute(insertQuery)
            cnxn.commit()
            print(" row inserted")
        except:
            print("Primary key not accept the same values")
    def Update_Salary(self,New_Salary,EName):
        try:
            self.New_Salary=New_Salary
            self.Name=EName
            if self.New_Salary!= self.Salary:
                Query = '''
                Update EmpDetails SET Salary ='{0}' WHERE EName = '{1}'
                '''
                updateQuery = Query.format(New_Salary,self.EName)
                cursor.execute(updateQuery)
                cursor.commit()
            else:
                raise ExistingError
        except ExistingError:
            print("No Change in Salary")
    def Add_Bonus(self,bonus,EName):
        self.bonus=bonus
        self.EName=EName
        try:
            if self.bonus not in range(1,self.Bonus+1):
                raise RangeError
            else:
                self.Salary=self.Salary+self.Salary*self.bonus
                Query = '''
                        Update Empdetails SET Salary ='{0}' WHERE EName = '{1}'
                                                                '''
                Query1 = Query.format(self.Salary,self.EName)
                cursor.execute(Query1)
                cursor.commit()
        except RangeError:
            print("Bonus is Not in Range")
    def Change_Project(self,project,EName):
        self.project=project
        self.EName=EName

        if self.project in self.Projects:
            if self.project == self.Project:
                print("Project is Already exists")
            else:
                Query = ''' Update Empdetails SET Project ='{0}' WHERE EName = '{1}' '''
                updateQuery = Query.format(project,EName)
                cursor.execute(updateQuery)
                cursor.commit()
        else:
            print("Project is not in list")
    def Display_details(self):
        query=''' select * from Empdetails WHERE EName='{0}' '''
        query1=query.format(self.EName)
        values=cursor.execute(query1)
        for details in values:
            print("Name:{0}  Salary:{1}  Project:{2}".format(details.Name,details.Salary,details.Project))
    def Delete_Employee_table(self):
        Query = ''' delete from Empdetails where EName='Srilekha'  '''
        cursor.execute(Query)
        cursor.commit()
        print("Employee has been deleted")

obj1=Employee_data('Srilekha',20000,'Python',1)
obj1.insert_Values_to_Table()
obj=empty1.employee_schema()
obj.employe_table()
obj1.insert_Values_to_Table()
obj1.Update_Salary(25000,'Srilekha')
obj1.Add_Bonus(1,'Srilekha')
obj1.Change_Project('c','python')
obj1.Display_details()
#obj1.Delete_Employee_table()