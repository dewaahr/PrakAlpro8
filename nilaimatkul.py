# nama_file='data.txt'
# handle=open('data.txt','r')
# isi_file=handle.read() #membaca keseluruhan file
# handle.close() #menutup file

# "\\ = pembatas directory"



# a=open('soal.txt','r')
# baris=1
# for kata in a:
#     if kata.startswith('C'):
#         print(f'{baris}.{kata}',end="")
#         baris=baris+1
# a.close()



print('Daftar matkul')
a=open('matkul.txt','r')
baris=1
totalsks=0
totalbobot=0
sks=0
matkul=''
harus_diulang=''
for kata in a:
    if baris%3==1:
        print(kata,end="")
        matakuliah=kata.strip()
    elif baris%3==2:
        totalsks=totalsks+int(kata)
        sks=int(kata)
    elif baris%3==0:

        if kata.strip()=='A':
            totalbobot=totalbobot+sks*4
        elif kata.strip()=='B':
            totalbobot=totalbobot+sks*3
        elif kata.strip()=='C':
            totalbobot=totalbobot+sks*3
        elif kata.strip()=='D':
            totalbobot=totalbobot+sks*1
        elif kata.strip()=='E':
            harus_diulang=harus_diulang+matakuliah+"\n"
    baris=baris+1
print(totalbobot/totalsks)
print(f'Total SKS :{totalsks:.2f}')
print(f'Harus diulang:\n{harus_diulang}')
a.close()