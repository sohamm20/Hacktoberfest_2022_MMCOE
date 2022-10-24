#a very simple trick to count digits, this can be used in competetive prgramming and also improves complexity
import math
n = int(input())
if n == 0:
    print(1)
#this is our simple trick function
else:
    print(math.ceil(math.log10(abs(n))))
