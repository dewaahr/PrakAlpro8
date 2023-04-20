file_text=open('romeojuliet.txt','r')
cari_kata=input('Masukan Kata Yang ingin dicari:').lower()
jumlah_kata=0

for baris in file_text:
    baris=baris.lower()
    jumlah_kata=jumlah_kata+baris.count(cari_kata)

print(f'Jumlah {cari_kata} pada file adalah {jumlah_kata}')

file_text.close()