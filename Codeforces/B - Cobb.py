
for t in range(int(input())):
  n,k = map(int, input().split())
  a = list(map(int, input().split()))
  b = list(range(1,n+1))
  ans = -10000000000
  
  for i in range(max(0, n-201), n - 1):
    for j in range(i+1, n):
      ans = max(ans, (i+1)*(j+1) - k*(a[i]|a[j]))
  print(ans)
