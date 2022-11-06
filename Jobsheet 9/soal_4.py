badu = int(input('masukan umur badu = '))

# umur sita adalah umur badu yang dikurangi 3
sita = badu - 3

# jika umur sita sama dengan 0 maka sita belum lahir
if sita == 0:
    print('umur badu adalah %d, sedangkan sita belum lahir' %badu)
else:
    print('umur badu adalah {} tahun, lebih tua 3 tahun dari sita yang berumur {}' .format(badu, sita)) 