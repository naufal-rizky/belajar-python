print('pembuatan piramida terbalik')
print('---------------------------')

n = int(input('n = '))

for baris in range(1, n + 1):
    for kolom in range(1, baris):
        print(' ', end="")
    
    for indeks in range(1, 2 * (n - baris) + 2):
        print('*', end="")
    print()