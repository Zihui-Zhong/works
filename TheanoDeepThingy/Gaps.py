

from decimal import *


f= open('1.txt', 'r')
r = f.read()
lines = r.split("\n")
for l in lines:
    s = l.split(" ")
    ret = []
    for i in range(len(s)-2):
         print(Decimal(s[i+1])-Decimal(s[i]),end = ' ')
    print('')