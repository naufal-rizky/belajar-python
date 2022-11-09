# Penentuan diskon

print('Penentuan diskon')
print('----------------')

besarPembelian = int(input('Nilai nominal pembelian = '))

# Penentuan diskon
diskon = 0
if besarPembelian >= 200000:
    diskon = 0.05 * besarPembelian
    
besarPembayaran = besarPembelian - diskon

# Tampilkan hasilnya
print()
print('Pembelian =', besarPembelian)
print('Diskon =', diskon)
print('Pembayaran =', besarPembayaran)