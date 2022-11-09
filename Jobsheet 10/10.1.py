# Penentuan bilangan terbesar
#   di antara dua bilangan

print('Penentuan bilangan terbesar')
print('di antara dua bilangan')
print('...........................')

bilanganX = int(input('Bilangan pertama = '))
bilanganY = int(input('Bilangan kedua = '))

# Penentuan bilangan terbesar
terbesar = bilanganX
if bilanganY > terbesar:
    terbesar = bilanganY
    
# Tampilkan hasilnya
print('Bilangan terbesar =', terbesar)