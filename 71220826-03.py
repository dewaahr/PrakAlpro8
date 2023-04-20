text_nilai=open('nilai.txt','r')
nilai_akhir=0
baris=1
for nilai in text_nilai:
    nilai=nilai.strip()
    if baris==1:
        nilai_akhir=nilai_akhir+(int(nilai)*0.05)
        print(f'Nilai Tugas {baris}: {nilai}')
    elif baris==2:
        nilai_akhir=nilai_akhir+(int(nilai)*0.05)
        print(f'Nilai Tugas {baris}: {nilai}')
    elif baris==3:
        nilai_akhir=nilai_akhir+(int(nilai)*0.1)
        print(f'Nilai Tugas {baris}: {nilai}')
    elif baris==4:
        nilai_akhir=nilai_akhir+(int(nilai)*0.05)
        print(f'Nilai Tugas {baris}: {nilai}')
    elif baris==5:
        nilai_akhir=nilai_akhir+(int(nilai)*0.15)
        print(f'Nilai Tugas {baris}: {nilai}')
    elif baris==6:
        nilai_akhir=nilai_akhir+(int(nilai)*0.1)
        print(f'Nilai Tugas {baris}: {nilai}')
    elif baris==7:
        nilai_akhir=nilai_akhir+(int(nilai)*0.22)
        print(f'Nilai Tengah Semester: {nilai}')
    elif baris==8:
        nilai_akhir=nilai_akhir+(int(nilai)*0.28)
        print(f'Nilai Akhir Semester: {nilai}')
    baris=baris+1
print(f'Nilai Akhir:{nilai_akhir:.2f}')