"""
Using 'yield' to generate suspended computations

The next computation is done only on request of user

In this example, we compute primes on demand
"""
#using 'yield' to compute primes 'on demand'
def naturals(n):
    yield n
    yield from naturals(n+1)

#creating generator object: naturals
s=naturals(2)

#obtaining primes by sieving through natural number list
def sieve(s):
    n=next(s)
    yield n 
    yield from sieve(i for i in s if i%n!=0)

#creating generator object: sieve 
x=sieve(naturals(2))

#taking input from user whilst trying to handle errors
def avoiderrors():
    try:
        usr=int(input("Enter the number of primes you want to generate: "))
        if usr>0 and usr<131:
            print(f"The first {usr} primes are: ")
            return usr
        elif usr>130:
            print("MAX Recursion depth limit reached! Enter a number less than 131")
            return avoiderrors()
        else:
            print("Positive integer is expected here")
            return avoiderrors()
    except:
        print("Positive integer is expected here")
        return avoiderrors()

#iterating through generator object 'user input' number of times[max recursive depth=130]
for p in range(avoiderrors()):
    #generating next prime "on demand" only
    print(next(x))
