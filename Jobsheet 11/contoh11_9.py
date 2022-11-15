print('pembuatan kotak')
print('---------------')

n = int(input('n (lebih besar daripada 2) = '))

for kolom in range(1, 2 * n + 1):
    print('*', end="")

print()

for indeks in range(1 * n - 1):
    print('*', end="")
    
    for kolom in range(1, 2 * n - 1):
        print(' ', end="")
        
    print('*')
    
for kolom in range(1, 2 * n + 1):
    print('*', end="")
    
print()