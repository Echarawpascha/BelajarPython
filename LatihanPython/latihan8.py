keranjang_buah = ['rambutan', 'jeruk', 'apel', 'mangga', 'melon']
nama_buah = input('Masukkan nama buah dalam huruf kecil: ')

if nama_buah in keranjang_buah:
    print(f'Buah {nama_buah} yang anda cari tersedia!')
else:
    print(f'Buah {nama_buah} yang anda cari tidak tersedia!')
