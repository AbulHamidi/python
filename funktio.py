luvut = []
#toiminnot------------------------------------------------
def kysy_toiminto(valitse):

    valitse = input("mitä tehdään? [summa, parittomat, parilliset]: ")

    if valitse == "summa":
        summa_luvut(luvut)

    elif valitse == "parilliset":
        poimi_parilliset(luvut)

    elif valitse == "parittomat":
        poimi_parittomat(luvut)


    else:
        kysy_toiminto(valitse)

#summa-------------------------------------------------
def summa_luvut(luvut):
    print(sum(luvut))

#parilliset--------------------------------------------
def poimi_parilliset(luvut):
    for num in luvut:
        if num % 2 == 0:
            print(num, end = "")

#parittomat--------------------------------------------
def poimi_parittomat(luvut):
    for num in luvut:
        if num % 2 != 0:
            print(num, end = " , ")


while True:
    print()
    luku = input("anna luku: ")
    luvut.append(int(luku))

    luku = input("anna luku: ")
    luvut.append(int(luku))

    luku = input("anna luku: ")
    luvut.append(int(luku))

    kysy_toiminto(luvut)

    luvut.clear()
    

    





