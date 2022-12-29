s="Python@1"
a=False
b=False
c=False
d=False
for i in s:
 if(s[i].isdigit()):
      a=True
   if(s[i].islower()):
      b=True
   if(s[i].isupper()):
      c=True
   if(s[i]=='@'):
      d=True
if a and b and c and d:
   print("password is valid")

