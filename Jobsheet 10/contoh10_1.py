print('Penentuan bilangan terbesar')
print('di antara dua bilangan')
print('---------------------------')

bilanganX = int(input('Bilangan pertama = '))
bilanganY = int(input('Bilangan kedua   = '))

terbesar  = bilanganX
if bilanganY > terbesar:
    terbesar = bilanganY
    
print('Bilangan terbesar = ', terbesar)