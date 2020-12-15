mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print('='*80,'\nNIM\t\tNAMA MAHASISWA\t\tTGL LAHIR\t\tTEMPAT LAHIR\n','-'*79)
x=0
for i in mhs:
    split = i.split(":")
    print(split[0],end="")
    a = len(split[1])
    print(split[1].rjust(12+a),end="")
    c = split[2]
    b = c.replace("-","/")
    print(b.rjust(34-a),end='')
    a = len(split[3])
    print(split[3].rjust(15+a))

print('-'*80)
