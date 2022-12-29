
class NoProjectException(Exception):
    pass
class Employee:
    bonus=2
    project=['python','c','java']
    salary=0
    add_project=[]
    def DisplayEmpDetails(self,Emp_name,project):
        print("Employe name:",Emp_name)
        #print("salary:",salary)
        print("project:",project)

    def addBonus(self):
        self.salary=int(input("enter salary"))
        self.bonus=self.salary*(self.bonus/100)
    def updateSalary(self):
        self.salary+=self.bonus
        print(self.salary)
    def ChangeProject(self,updated_project):
        try:
            list_l=['c#','c++']
            if list_l in self.project:
                print("the projects are same")
            else:
                print("projects are not same")
                self.add_project=self.project.extend(list_l)
                print("updated project list",self.add_project)
                self.updated_project=int(input())
                if self.updated_project in self.add_project:
                    print("employee project is updated:")
        except NoProjectException as e:
            print(e)
emp=Employee()
emp.DisplayEmpDetails("abc",'python')
emp.addBonus()
emp.updateSalary()
emp.ChangeProject()