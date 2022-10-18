# Bit count

n = 15

count = 0

for i in range(32):
    if n & ( 1 << i) != 0:
        count += 1

print(count)
