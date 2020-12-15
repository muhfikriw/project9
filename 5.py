nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	   {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	   {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('====================================================\nNIM\tNAMA\t\tN.MID\t\tN.UAS\n----------------------------------------------------')
x = 0
for i in nilai:
    print(nilai[x]['nim'],end="")
    a = len(nilai[x]['nama'])
    print(nilai[x]['nama'].rjust(5+a),end="")
    z = str(nilai[x]['mid'])
    print(z.rjust(21-a),end="")
    z = str(nilai[x]['uas'])
    print(z.rjust(16))
    x += 1

print("----------------------------------------------------")