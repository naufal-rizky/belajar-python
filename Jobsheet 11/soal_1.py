n = int(input('n = '))

for i in range(n):
    print(i+1, end="\t")
print()
print('________________________________________________________________________________')

for j in range(n):
    for k in range(n):
        print((j+1)*(k+1), end="\t")
    print('')