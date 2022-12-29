#10/11/2022
if True:
    print("if block")
    print("inside if")


n=int(input())
if n>0:
    print("positive")
else:
    print("negative")
print("end")

#nested conditional blocks
matches_won=int(input())
goals=int(input())
if matches_won>8:
    if goals>20:
        print("hurry")
print("winner")
#nested condition in else block
a=2
b=3
c=1
is_a_greatest=(a>b) and (a>c)
if is_a_greatest:
    print(a)
else:
    is_b_greatest=(b>c)
    if is_b_greatest:
        print(b)
    else:
        print(c)


number=int(input())
is_divisible_by_10=(number%10==0)
is_divisible_by_5=(number%5==0)
if is_divisible_by_10:
    print("divisible by 10")
elif is_divisible_by_5:
    print("divisible by 5")
else:
    print("not divisible by 10 or 5")

m=70
p=65
c=65
d=((m>=70 and p>=60 and c>=60) or m+p+c>=180)
print(d)

#10/11/2022
#write a program tp print the digit in the one's place
a=input()
b=int(a[-1])
print(type(b))
#absolute difference
num1=100
num2=150
num_result=abs(num1-num2)
print(num_result)
#number of days as input(N).write program to convert N to years Y weeks W AND Days D :1329=365 3+ 33 7 +3

#loops 11/11/22
#while
n=int(input())
condition=1
while condition<n:
    print("hi")
    condition+=1

a=int(input())
counter=0
while counter<3:
    a=a+1
    print(a)
    counter=counter+1

a=int(input())
while counter<3:
    a=a+1
    print(a)
    counter = counter + 1
print("End")

a=int(input())
counter=0
while counter<3:
    a=a+1
    print(a)
print("End")
word="Python"

#for
#sum of given numbers
l=[1,2,3,4,5]
s=0
for i in l:
    s=s+i
print(s)

#sum of N natural numbers
n=int(input())
s=0
for i in range(0,n):
    s=s+i
print(s)

#product of given numbers
l=[1,2,3]
s=1
for i in l:
    s=s*i
print(s)

#for
#square pattern
m=int(input())
for i in range(0,m):
    for j in range(0,m):
        print("*",end=" ")
    print()
print("square pattern")
#rectangular square
m=int(input()) #rows
n=int(input()) #cols
for i in range(0,m):
    for j in range(0,n):
        print("*",end=" ")
    print()
print("Rectangular pattern")
#Rightangle traingle pattern

m=int(input())
for i in range(0,m):
    for j in range(0,i+1):
        print("*",end=" ")
    print()

#left angle traingle

m=int(input())
for i in range(0,m):
    for j in range(0,m-i+1):
        print(" ",end=" ")
    for k in range(0,i+1):
        print("*",end=" ")
    print()

#Right angle Traingle
m=int(input())
for i in range(m):
    for j in range(m-i+1):
        print(" ",end=" ")
    for k in range(i):
        print("* ",end=" ")
    print()
