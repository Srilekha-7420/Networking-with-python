#14/11/2022
var=None
print(var)
print(type(var))
#Tuple is ordered sequence of items.Tuple is immutable object
#Tuple concatination
a=2
tuple_a=(5,"six",a,8.2)
print(tuple_a)
tuple_b=("hi",5,10.22,"hola!")
print(tuple_b)
print(tuple_a+tuple_b)

#access tuple value
print(tuple_a[2])

#string to tuple
color="Red"
tuple_a=tuple(color)
print(tuple_a)

#list to tuple
list_a=[1,2,3,4]
tuple_a=tuple(list_a)
print(tuple_a)

#sequence to tuple
tuple_a=tuple(range(4))
print(tuple_a)

#in and not in
#tuple
tuple_a=(1,2,3,4)
tuple_b=4 in tuple_a
print(tuple_b)

tuple_a=(1,2,3,4)
tuple_b=5 not in tuple_a
print(tuple_b)
#list
list_a=[1,2,3,4]
list_b=5 in list_a
print(list_b)

#string
word="python"
is_part="th" in word
print(is_part)
#finding type of nested tuple or list
data=(1,[1,2,3])
tuple_1=1,2,data,
print(type(tuple_1[2][1]))

#unpacking
#values of any sequence can be directly assigned to variables
#number of variables in th left should match the length of sequence
tuple_a=('r','e','d')
(s1,s2,s3)=tuple_a
print(s1)
print(s2)
print(s3)
#error
tuple_a=('r','e','d')
(s1,s2)=tuple_a
print(s1)
print(s2)

#packing
a=1,2,3
print(type(a))
print(a)

a=1,
print(a)
print(type(a))

#Sets
#unorderd collection of items.Every set element is unique and immutable
a=2
set_a={5,"six",a,8.2}
print(type(set_a))
print(set_a)

#no duplicates
set_a={"a","b","c","a"}
print(set_a)
#immmutable items
set_a={"a",["c","a"]}
print(set_a)
#create empty set
set_a=set()
print(type(set_a))
print(set_a)
#set conversion
list_a=[1,2,1]
set_a=set(list_a)
print(set_a)
#string to set
set_a=set("apple")
print(set_a)
#tuple to set
set_a=set((1,2,3))
print(set_a)
#as items are not ordered
#set does not allowed indexing and slicing
set_a={1,2,3}
print(set_a[1])
print(set_a[1:3])
#add items
# using add() we can add single element
set_a={1,3,6,2,9}
set_a.add(7)
print(set_a)
#add multiple items
set_a={1,3,6,2,9}
set_a.update([2,3])
print(set_a)
#remove specific item by using discard  if the element exists we can remove element from list
#if the element is not present in list it shows nothing
set_a={1,3,6,2,9}
set_a.discard(3)
print(set_a)

set_a={1,3,6,2,9}
set_a.discard(7)
print(set_a)
#remove throws error
set_a={1,3,6,2,9}
set_a.remove(6)
print(set_a)
#key error
set_a={1,3,6,2,9}
set_a.remove(7)
print(set_a)
#clear set
set_a={1,3,6,2,9}
set_a.clear()
print(set_a)
#length of set
set_a={1,3,6,2,9}
print(len(set_a))
#set operations

