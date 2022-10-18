def mi():
    return map(int, input().split())
def li():
    return list(mi())
def si():
    return str(input())
def ni():
    return int(input())

"""

Codeforces round 827 div.4

"""
try:
    for _ in range(int(input())):

        found = False
        input()

        for i in range(8):
            a = str(input())
            
            if a == "R"*8:
                found = True

        if found:
            print("R")
        else:
            print("B")
except:
    pass
