from math import gcd
def lcm(a,b):
  return (a*b)//gcd(a,b)
 
for t in range(int(input())):
  
  a,b,c,d = map(int, input().split())
  
  ans = -1
  temp = -1
  for x in range(a + 1, c+1):
      y = lcm(a*b, x)//x
      target = y*(int(d//y))
      if target <= d and target > b:
        ans = int(x)
        temp = int(target)
        break
  print(ans, temp)
