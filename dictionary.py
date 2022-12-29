#write a program that contains keys an numbers from 1 to M and values are squares of keys
number=list(map(int,input().split(" ")))
dict1={}
for i  in number:
    dict1[i]=i**2
print(dict1)
#dictionary comprehension
number=[1,5,6,7]
dict1={x:x**2 for i in number}
print(dict1)
#update value of particular key
dict1={1:'a',2:'b',3:'c'}
dict1[2]='d'
print(dict1)
#remove a key
dict1={1:'a',2:'b',3:'c'}
del dict1[2]
print(dict1)
#prefilled code will contain dictionary write a program to update the value of given key
dict1={1:'a',2:'b',3:'c'}
dict1[2]='d'
print(dict1)
#determine no of rotations.python,onpyth-cloud udclo

#given M*N matrix,write a program to printthe matric after ordering all elements of the matrix in increasing order
#read two numbers.M and N.print all the perfect squares between M and N
m=int(input("enter from"))
n=int(input("to dead"))
b=[]
for i in range(m,n):
    a=i**2
    if(a<n):
        b.append(a)
print(b)

#write a program to return the sum and average of digits of all numbers that appear in the string,ignoring all the
#other characters
string_1="1234"
number=list(string_1)
print(number)
sum1=0
for i in number:
    a=int(i)
    sum1+=a
b=sum1/len(number)
print(sum1)
print(b)





