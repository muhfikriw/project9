n = int(input("berapa n ? "))
def bintang(n):
    try:
        if n > 0 :
            for i in range(n):
                a = "*" + "**"*i
                print(a.center(10," "))
        else:
            print("angkamu negatif \nmana bisa gitu")

    except ValueError:
        print("bukan angka")

bintang(n)