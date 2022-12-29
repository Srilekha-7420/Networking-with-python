def positional_arg(x=10,y=20):
    print(x,y)
positional_arg(x=5)

def greetings():
    print("hello")
greetings()
name=input()
greetings()
print(name)

def get_list(string_a):
    list_a=string_a.split(',')
    len_list_a=len(list_a)
    for i in range(len_list_a):
        list_a[i]=int(list_a[i])
        return list_a
string_a=input()
numbers_list=get_list(string_a)
print(numbers_list)

#return the given argument
def return_arg(word):
    msg="hi"+word
    print(msg)
    return msg
return_arg("hlo")

#the prefilled code will contain a function.write a program to concatinate the message
#"welcome HCL"
def return_arg(word):
    msg="welcome  "+word
    print(msg)
return_arg("HCL")

#write a program that accepts string 1,2,3,4
# and it splits into list and return suare of each no[1,4,9,16]
#string="1234"
#str_sqlist=[]
#temp=1

def string_split():
    a=input()
    str_sqlist=[]
    for i in a:
        if i.isdigit():
            str_sqlist.append(int(i)*int(i))
    print(str_sqlist)
string_split()

#write the function to return second character in the word
def sec_char():
    val1=input()
    val2=""
    for i in range(len(val1)):
        if (val1[i].isalpha()):
            val2+=val1[i]
    print(val2[1])
    #return se_char
sec_char()
#write the function to return no of lowercase and uppercase letters in a string
def lower_upper():
    a=input()
    low=0
    upp=0
    for i in range(len(a)):
        if(a[i].islower()):
            low+=1
            #print("lower count:",low)
        elif(a[i].isupper()):
            upp+=1
            #print("upper count:",upp)
    print("upper count is :", upp,"lower count is :",low)
lower_upper()
#write a function to check if the number is divisible by 7 return true or false
def divBy_7():
    number=int(input())
    if (number%7==0):
        print("{} is divisible by 7".format(number))

divBy_7()
#write a function to return area AND PERIMETER OF A Square
def squre_area_perimeter():
    a=int(input())
    area=a**2
    perimeter=4*a
    print("area=",area)
    print("perimeter=",perimeter)
squre_area_perimeter()
#write a function that takes number of wins,draws, and losses and calculate the number of points
#each win is 4 points,draw  is 2 points,loss is -1..
# input is single string containing win,draws an losses by comma seperated.
# the output is single line containing total points
def matches(w,d,l):
    m=int(input("enter no of wins,areas and loss").split(","))
    s=w*4,d*2,l*1
    total=(w+d)-l
    print(total)
matches(win,draw,loss)
#if a no is divisible by 3 it should return Macro,if a number is divisible by 5 it sholud return polo
#if its divisible by 3 and 5 it should return Macro Polo or else just return the no
def divBy_3_5():
    number=int(input())
    if (number%3==0 and number%5!=0):
        print("Macro")
    elif (number%5==0 and number%3!=0):
        print("Polo")
    elif (number%3==0 and number%5==0):
        print("Macro polo")
divBy_3_5()
#write a program to extract the numbers in given string and
# print sum,minimum and maximum of those numbers
#ex: c0d1n8 sum=9,min=0,max=8

def extract_num_from_string():
    string_s=input()
    list_a=list(string_s)
    val1=[]
    for i in list_a:
        if i.isdigit():
            val1.append(int(i))
    print(min(val1))
    print(max(val1))
    print(sum(val1))
extract_num_from_string()
#factorial of a number using recursion
#identify sum of first n natural numbers
#take a prefilled list.write a program to remove all the occurances of the given number(N)
#in a list.print list after removing those numbers