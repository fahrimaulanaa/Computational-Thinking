bilangan = int(input("Masukkan bilangan: "))

def check():
    if bilangan > 1:
        for i in range(2, bilangan):
            if (bilangan % i) == 0:
                print(bilangan, "bukan bilangan prima")
                break
        else:
            print(bilangan, "adalah bilangan prima")

    else:
        print(bilangan, "bukan bilangan prima")

check()

