print('Penentuan diskon')
print('----------------')

besarPembelian = int(input('Nilai nominal pembelian = '))

diskon = 0
if besarPembelian >= 200000:
    diskon = 0.05 * besarPembelian
else:
  diskon = 0
    
besarPembayaran = besarPembelian - diskon

print()
print('Pembelian  = ', besarPembelian)
print('Diskon     = ', diskon)
print('Pembayaran = ', besarPembayaran) 