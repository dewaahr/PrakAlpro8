buah_lama=input('Masukan Nama Buah yg ingin diganti:')
buah_baru=input('Masukan Nama Buah pengganti:')
a=open('buah.txt','r')
isi_file=''
for baris in a:
    if baris.strip()==buah_lama:
        isi_file=isi_file+buah_baru+'\n'
    else:
        isi_file=isi_file+baris 
a.close()

a=open('buah.txt','w')
a.write(isi_file)
a.close()
