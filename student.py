class Student:
    mark_bonus=1.5
    year=2022
    somevalue=""
    def __init__(self,first,last,marks):
        self.first=first
        self.last=last
        self.marks=marks
    #decoarator is used to get and set the value
    @property
    def email(self):
        return '{}.{}@gmail.com '.format(self.first,self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_bonus(self):
        self.marks=int(self.marks*self.marks_bonus)
    def fun(self):
        self.year+=1
    def function(self,mname):
        self.somevalue=self.fullname+self.email+mname