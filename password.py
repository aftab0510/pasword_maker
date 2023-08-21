import string
import random
s1=string.ascii_lowercase
s2=string.ascii_uppercase
s3=string.digits
s4=string.puncutio
try:
    password=int(input("enter the length of password: "))

except ValueError:
    print("valueerror")

s=[]
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)
random.shuffle(s)
print("-".join(s[0:password]))
