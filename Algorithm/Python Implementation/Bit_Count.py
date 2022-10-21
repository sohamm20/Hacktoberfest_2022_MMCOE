

num = int(input("Please Enter any Number: "))


print ("binary value of {0} is: {1}".format(num, bin(num)))

# store the length of the binary number
length = len(bin(num))

# to get exact length total number of bits
# subtract 2 from the length
length -=2

# print length
print ("total number of bits: ", length)
