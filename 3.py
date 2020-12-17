import math
n = int(input("berapa n ? "))
def bintang(n):
    try:
        if n > 0:
            if (n%2 != 0):
                n = math.ceil(n/2)
                for i in range(n):
                    a = "*" + "**"*i
                    print(a.center(20," "))
                xx = 0
                x = n -1
                for i in range(x):
                    xx += 1
                    a = "*" + "**"*(x - xx)
                    print(a.center(20," "))
            else:
                print("angkamu negatif \natau \nbukan bil ganjil")
    except ValueError:
        print("bukan angka")

bintang(n)
