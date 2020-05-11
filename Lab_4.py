#Task 1

import string
import math
x=input("Enter a file name(.txt file): ")
f_hand=open(x)
for i in f_hand:
    i=i.strip()
    z=i.lower()
    z=z.strip(string.punctuation)
    x+=i
print(x)
