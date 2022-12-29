#9/11/2022
#2nd first 3 characters
#Tasks
#1st 9/11/2022
#take two integers M &N,write a program to create a list with element M repeated by N times

a=10
b=[20]
print(list(b*a))

#Take a list,your program should crete newlist with all the elements
# in existing list that are greater than given number

l=[1,2,38,8,9,54,23]
n=8
s=[]
for i in l:
    if n<i:
        s.append(i)
print(s)

#3
list1=[1,2,3,4]
list2=list1[::-1]
print(list2)



#10/11/2022
#1 check if the three characters of a string are same or not
s="Apple"
s1="Application"
print(s[:3]==s1[:3])
#write a program that reads two 3 digit numbers and check if the first digit of A is less than last digit o B
#1st way
l1='786'
l2='589'
l3=int(l1[0])
l4=int(l2[2])
print(l3<l4)
 #2nd way
a=786
b=589
c=a%10
d=b//100
print(c<d)
#write a program that read the marks in MPC.check if any of the conditions is satisfied
#M>=70,P>=60,C>=60 M+P+C>=180
m=int(input())
p=int(input())
c=int(input())
if((m>=70 and p>=60 and c>=60) or (m+p+c>=180)):
    print("pass")
else:
    print("no pass")
#slicing
a="Waterfall"
part=a[0:7:2]
print(part)
#isdigit
is_digit="4756a".isdigit()
print(is_digit)
#strip
mobile="  9876 543210  "
mobile=mobile.strip()
print(mobile)

name=".srilekha."
name=name.strip(".")
print(name)

name=",...,sri.lekha.,,,"
name=name.strip(".,")
print(name)

#replace
sentence="teh cat teh dog"
sentence=sentence.replace("teh","the")
print(sentence)

mobile="  9876 543210  "
mobile=mobile.replace(" ","")
print(mobile)

#starts with
url="https://onthegomodel.com"
is_secure_url=url.startswith("https://")
print(is_secure_url)

#endswith

#gmail="rahul123@gmail.com"
gmail="fdgf.com"
gmaild=gmail.endswith("com")
print(gmaild)
#upper
name="raVi"
print(name.upper())
#lower
name="RAVI"
print(name.lower())


