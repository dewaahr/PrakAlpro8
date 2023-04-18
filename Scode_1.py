text_a=open('soal_1a.txt','r')
text_b=open('soal_1b.txt','r')
baris_texta = text_a.readlines()
baris_textb = text_b.readlines()

for baris_a in baris_texta:
    for baris_b in baris_textb:
        if baris_a == baris_b:
            print(f'{baris_a.strip()} sama dengan {baris_b.strip()}')
        else:
            print(f'{baris_a.strip()} berbeda dengan {baris_b.strip()}')