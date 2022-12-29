#every method having self parameter by default like class method and instance method except static method
class car:
    someclassdummyyar="dummy"
    def sample_car_instance_method(self,a):
        print(a)
        print(self.someclassdummyyar)
carObj=car()
carObj.sample_car_instance_method("hello world")
carObj2=car()
carObj2.sample_car_instance_method(2)

class carSample():
    dummyvar1="dummyvar1"
    dummyvar2="dummyvar2"
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def displayCarDetails(self):
        print(self.name)
        print(self.model)
carObj=CarSample("audi","a5")
carObj.displayCarDetails()

#static method
#static method doesnot need self parameter
#for static method we use staticmethod decorator
class StaticClass:
    @staticmethod
    def sample_static_method_addition(x,y): #static method doesnot need self parameter
        return x + y
    @staticmethod
    def sample_static_method_multiplication(x,y):
        return x * y

staticObj=StaticClass()
output_add=staticObj.sample_static_method_addition(2,3)
output_mul=staticObj.sample_static_method_multiplication(2, 7)
print(output_add,output_mul)

#class method
#for classmethod we use classmethod decorator
class ClassMethodExample:
    classVar1=False
    classVar2="ON"
    def print_classvariables(self):
        print(self.classVar1)
    @classmethod
    def sample_class_method(cls):
        cls.classVar1=True
        cls.classVar2="OFF"
ClassMethodExample.sample_class_method()
obj = ClassMethodExample()
obj.print_classvariables()
print(ClassMethodExample.classVar1)
print(ClassMethodExample.classVar2)

#Instance method:This is used to deal with instance objects.
# it is used to get and set instance objects
#__init()__ method is a instance method is an instance method,unless you speicify it with an decorator
#inorder to call an instance method,you have create a object/instance of an class
#__init()__=constructor
#self=current object.this
class animal:
    def __init__(self,species,gender):
        self.species=species
        self.gender=gender
animalObj=animal('dog','male')
print(animalObj.gender)
print(animalObj.species)

class My_class:
    dummyVar="Test"
    def instance_method_example(self,a):
        print(a)
        print(self.dummyVar)
myclassObj=My_class()
myclassObj.instance_method_example("Hola!")

class my_instance_class:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sample_instance_class(self):
        print(self.a,self.b)
obj=my_instance_class("Cap","IronMan")
obj.sample_instance_class()

#class methods
#in class methods cls is default parameter
class ClassMethod:
    @classmethod
    def class_method(cls):
        print("this is class mehod")
'''obj=ClassMethod()    #here we want to call the class method there are 2 ways 
obj.class_method()''' #one way is cal through object

ClassMethod.class_method()  #another way is we call the method by using classname

#static method:used as utility classes,self sufficient classes
#we  can call the methods in staticmethod by using 2 ways through object and classname
class StaticMethod:
    @staticmethod
    def static_method():
        print("this is static method")
'''obj=StaticMethod()
obj.static_method()'''

StaticMethod.static_method()



