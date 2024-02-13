nilai = int(input('masukan nilai: '))
usia = int(input('Masukan usia: '))

if nilai >= 80:
    if(usia <15):
        print('selamat adik, kamu lulus!')
    else:
        print('Selamat kakak, kamu lulus!')
else:
    if(usia <15):
        print('Mohon maaf dek, coba lagi yak')
    else:
        print('mohon maaf kak, coba lagi yak')