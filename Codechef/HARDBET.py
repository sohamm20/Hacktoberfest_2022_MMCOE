for _ in range(int(input())):
    arr = list(map(int,input().split(' ')))
    mini = min(arr)
    for i in range(len(arr)):
        if arr[i]==mini:
            num = i
    if num == 0:
        print('Draw')
    elif num == 1:
        print('Bob')
    else: print('Alice')
