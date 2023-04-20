buah_hapus=input('Masukan Nama Buah yg ingin dihapus:')
text=open('buah.txt','r')
buah_buah=[]
for baris in text:
    baris=baris.strip()
    buah_buah.append(baris)

for buah in buah_buah:   
    if buah==buah_hapus:
        buah_buah=buah_buah.remove(buah)
text.close()

text=open('buah.txt','w')
for buah in buah_buah:
        text.write(bu
    else:
        print('Buah Tidak ada dalam file')

text.close()