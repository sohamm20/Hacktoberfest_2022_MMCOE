#QUICKSORT
def partition(ar, l , h):

    pi = l
    p = ar[pi]
    while l<h:
        while l<len(ar) and ar[l]<p:
            l += 1
        while ar[h]>p:
            h -= 1
        if(l<h):
            ar[l],ar[h] = ar[h],ar[l]   
    ar[h],ar[pi] = ar[h],ar[pi]
    return h

def QSort(ar, l, h):
    if l<h:

        i = partition(ar, l, h)

        QSort(ar,i+1,h)
        QSort(ar,l,i-1)
       
 
def display(ar):
    print ("The top 5 percentages are::",ar[-5:])

n = int(input("Enter the number of students::"))
ar = []
for i in range(n):
    ar.append(input("Enter percentage of students::"))
QSort(ar, 0, len(ar)-1)
display (ar)
