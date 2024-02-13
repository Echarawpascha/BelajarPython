kota, provinsi = 'Bandung', 'Jawa Barat'

def contoh_var_lokal():
    provinsi = "Jawa Timur"
    print(kota, provinsi)

print('[Panggil Fungsi contoh_var_lokal()]')
contoh_var_lokal()

print('\n[Panggil variabel secara langsung]')
print(kota, provinsi)