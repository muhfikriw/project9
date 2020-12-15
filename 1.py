def ubahHuruf(x,y,z):
    a = y
    b = z
    c = x
    for i in range(len(b)):
        c = c.replace(a[i],b[i])
    print(c)

ubahHuruf("MATEMATIKA","T","S")