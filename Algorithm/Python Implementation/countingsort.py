def sort(ar):
    max_ = int(max(ar))
    min_ = int (min(ar))
    ran = max_-min_+1
    count = [0 for i in range(ran)]
    out = [0 for i  in range(len(ar))]
    for i in range(0, len(ar)):
        count[ar[i]-min_] += 1
    for i in range(1,len(count)):
        count[i] += count[i-1]
    for i in range(len(ar)-1,-1,-1):
        out[count[ar[i]-min_]-1] = ar[i]
        count[ar[i]-min_] -= 1
    for i in range(0,len(ar)):
        ar[i] = out[i]
    print(ar)
arr = [-5, -10, 0, -3, 8, 5, -1, 10]
sort(arr)