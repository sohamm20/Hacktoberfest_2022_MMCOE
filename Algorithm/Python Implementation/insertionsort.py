def ISort(ar):
    x = ar
    for i in range(len(ar)):
        temp = ar[i]
        j=i-1
        while j>=0 and temp < ar[j]:
            ar[j+1] = ar[j]
            j-=1
        ar[j+1] = temp
    display (ar)
def display(ar):
    print ("The top 5 percentages are::",ar[-5:])
n = int(input("Enter the number of students::"))
x = []
for i in range(n):
    x.append(input("Enter percentage of students::"))
ISort(x)