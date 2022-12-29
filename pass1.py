s = input("Enter password")
a = False
b = False
c = False
d = False
for i in s:
    if (i.isdigit()):
        a = True
    if (i.islower()):
        b = True
    if (i.isupper()):
        c = True
    if (i=='@'or i=='$' or i=="#"):
        d = True
if a and b and c and d:
    print("password is valid")
else:
    print("password is invalid")

