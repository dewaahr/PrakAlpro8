'''file=input('Nama File:')
with open(file,'r') as file:
    for kalimat in file:
        kalimat=kalimat.lower()
        bagian=kalimat.split('||')
        kata1=bagian[0].strip()
        kata2=bagian[1].strip()
        print (kata1)
        print(kata2)
        jawab=input('Jawab:').lower()
        if jawab==kata2:
            print('Jawaban Benar!')
        else: print('Jawaban Salah')'''
file=input('Nama File:')
a=open(file,'r')
for kalimat in a:
    kalimat=kalimat.lower()
    bagian=kalimat.split('||')
    kata1=bagian[0].strip()
    kata2=bagian[1].strip()
    print (kata1)
    jawab=input('Jawab:').lower()
    if jawab==kata2:
        print('Jawaban Benar!')
    else: print('Jawaban Salah')
        
