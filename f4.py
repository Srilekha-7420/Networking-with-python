#10/11/2022
#1.swap cases
first_no=34
second_no=65
first_no,second_no=second_no,first_no
print(first_no)
print(second_no)
#anotherway of swapcases
#3.palindrome
n=123
temp=str(n)
temp1=temp[::-1]
temp1=int(temp1)
if n==temp1:
    print("palindrome")
else:
    print("not palindrome")

#anotherway
m="hcl"
s=m[::-1]
print(s)
if m==s:
    print("pal")
else:
    print("not pal")
#anotherway of palidrome
#Convert dd_mm_yy format  to dd/mm/yy
dd_mm_yy="dd-mm-yy"
dd_mmm_yyyy=dd_mm_yy.replace("-","/")
print(dd_mmm_yyyy)

#password
password="Kiran@11"


