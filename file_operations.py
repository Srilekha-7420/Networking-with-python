#file first program:file open,read and close

file=open('Dummy.txt','r')
print(file.read())
print(file)
print(file.name)
file.close()
#file open,close

file=open('Dummy.txt','r')
print(file.read())
print(file)
print(file.name)
print(file.mode)
file.close()

#context manager with readline

with open('Dummy.txt','r') as file:
    print(file.readline(),end="")
    print(file.readline(),end="")
#with for loop

with open('Dummy.txt','r') as file:
    for i in file:
        print(i)
#read:tells the position in file

with open('Dummy.txt','r') as file:
    file_content=file.read(10)
    print(file_content)
    file_content = file.readline()
    print(file_content)
    print(file.tell())
#tell

with open('Dummy.txt','r') as file:
    print(file.readline())
    print(file.readline())
    print(file.tell())

with open('Dummy.txt','r') as file:
    size_to_read=20
    file_content=file.read(size_to_read)
    while len(file_content)>0:
        print(file_content,end="*")
        file_content=file.read(size_to_read)
#append:it can add the data at the end of the content in a file

with open("Text.txt",'a') as file:
    file.write('test write...')

#write: override the existing data and print present data

file=open('new.text','w')
file.write('File')
file.close()

sampleFile=open("Text.txt",'a')
sampleFile.write("/n this should append to a file")
sampleFile.close()
#creating new file every time(fresh files)
#file is not exist
file=open('new2.txt','x')
file.write("File operations")
file.close()

file=open('Dummy.txt','r')
print(file.read())
#readline:this method is used to read the whole file but line by line.
# it updates the file by each line that is returned
file=open('Dummy.txt','r')
print(file.readline())
#readlines
file=open("Dummy.txt",'r')
print(file.readlines())

#print copy of one text file into another file
with open("Dummy1.txt",'r') as file1,open("Dummy2.txt",'a') as file2:
    for data in file1:
        file2.write(data)


file1=open("Dummy1.txt",'r')
file2=open("Dummy2.txt",'a')
for i in file1:
    temp=str(i)
    file2.write(temp)
file1.close()
file2.close()


#read(n)--specified length of characters
file=open("Dummy.txt",'r')
print(file.read(20))
file.close()
#r+ mode:read and write
file=open('new1.txt','r+')
file.write("line1\n")
file.write("line1\n")
file.close()

#writelines()-used to write a sequence of strings to a file
file=open("new1.txt",'a')
lines=["line 100","line101"]
file.writelines(lines)
file.close()

#remove a file
import os
os.remove("new1.txt")

#other file operations
#flush()-flush the internal buffer
#detach()-return the seperated raw stream from the buffer
#readable()-return true if the file stream can be read