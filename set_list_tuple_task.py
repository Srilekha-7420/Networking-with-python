#14/11/2022
#min and max values in list of tuples
list_a=[(4,2,3),(7,1,9)]
list_b=list_a[0]+list_a[1]
print(list_b)
print(min(list_b))
print(max(list_b))
#read the inputs in N lines and print them as list of tuples
m=[1,2,3]
n=[4,5,6]
o=[7,8,9]
p=(tuple(m),tuple(n),tuple(o))
print(list(p))

#character frequency.the input string will contain only alphabets and whitespaces.ignore case sensitivity
#"Pop Up" p:3 u:1 o:1
string1=input()
string2=string1.lower()
list_a=list(string2)
set_str=set(list_a)
for i in  set_str:
    if i!='':
        print(i+ ":",end=" ")
        print(list_a.count(i),end=" ")

#write a program to remove duplicate numbers in the list
list_a=[1,2,3,1]
set_a=set(list_a)
print(set_a)
#write a program to remove a list of numbers if present in the set.read inputs as comma seperated
set_a={1,2,3}
set_b={3,4,5}
diff=set_a-set_b
print(diff)
#given two lines of comma separated integer,
# write a program to print the numbers that are present in both the lines
set_a={1,2,3}
set_b={3,4,5}
comm=set_a & set_b
print(comm)
#write a program to remove the elements other than numbers in the list
#ex:1,2,3,#,5 2,@,5,7#,^
list_a=input()
for i in list_a:
    if i.isdigit():
        print(i,end=" ")