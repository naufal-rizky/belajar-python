print('Penentuan bilangan terbesar')
print('di antara dua bilangan')
print('---------------------------')

bilanganX = int(input('Bilangan pertama = '))
bilanganY = int(input('Bilangan kedua   = '))

if bilanganX > bilanganY:
    terbesar = bilanganX
else:
    terbesar = bilanganY
    
print('Bilangan terbesar = ', terbesar)