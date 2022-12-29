#referring the same objects

list_a=[1,2,3,5]
list_b=list_a
print(id(list_a))
print(id(list_b))
list_b[3]=4
print(list_a)
print(list_b)

#compound assignments example

list_a=[1,2]
list_b=list_a
list_a=list_a+[6,7]
print(str(list_a))
print(str(list_b))


list_a=[1,2]
list_b=list_a
list_a+=[6,7]
print(list_a)
print(list_b)

list_a=[1,2]
list_b=[3,list_a]
list_a[1]=4
print(list_a)
print(list_b)

#string reverse

s='abcdefg'
d=s[::-1]
print(d)

#negative indexing

list_a=[1,2,3,4,5]
print(list_a[4])
print(list_a[-1])

# slicing examples:to extract part of object

list_a=[1,2,3,4,5]
list_b=list_a[-5:-1]
print(list_b)

#negative step size:determines the decrement between each index for slicing start>end

list_a=[5,4,3,2,1]
list_b=list_a[4:0:-2]
print(list_b)

list_b=list_a[1:4:-1]
print(list_b)

list_b=list_a[::-1]
print(list_b)

#slicing &indexng strings

s1="program"
s2=s1[6:0:-2]
print(s2)

#splitting a string:str_var.split(seperator),default seperato is whitespace
#multiple whitespaces are considered as single whitespace

n="123  4"
n1=n.split()
print(n1)

n="1 234"
n1=n.split()
print(n1)

n="1,2,3,4"
n1=n.split()
print(n1)

l=[1,2,3,4,5]
print(l[-2:-4:-1])

s="pythona, is simple language"
list_a=s.split(',')
print(list_a)

l=['python is','progr','mmingl','ngu','ge']
s="a".join(l)
print(s)

l=list(range(4))
print(l)