import art

print(art.logo)


def add(nr1, nr2):
    return nr1 + nr2


def scadere(nr1, nr2):
    return nr1 - nr2


def inmultire(nr1, nr2):
    return nr1 * nr2


def impartire(nr1, nr2):
    return nr1 / nr2


operatii = {
    '+': add,
    '-': scadere,
    '*': inmultire,
    '/': impartire
}


def calculator():
    run = True
    while run:

        num1 = int(input("Care este primul numar :"))
        for simbol in operatii:
            print(simbol)

        operatie_simbol = input("Alege te rog opetaroul pentru calcul: ")
        num2 = int(input("Care este al doilea numar :"))
        # Pana aici luam datele de la utilizator
        functie_calcul = operatii[operatie_simbol]
        first_rez = functie_calcul(nr1=num1, nr2=num2)
        print(f"{num1} {operatie_simbol} {num2} = {first_rez}")
        continuu = input(f"Tasteaza \'d\' pentru a contiua calculul cu {first_rez} altfel apasa \'n\' =")
        if continuu == 'n':
            print(f"Rezultat final = {first_rez}")
            run = False
        while continuu == 'd':

            operatie_simbol = input("Alege te rog opetaroul pentru alt calcul: ")
            num3 = int(input("Care este numarul?"))
            functie_calcul = operatii[operatie_simbol]
            second_rez = functie_calcul(first_rez, num3)
            print(f"{first_rez} {operatie_simbol} {num3} = {second_rez}")
            first_rez = second_rez
            continuu = input(f"Tasteaza \'d\' pentru a contiua calculul cu {first_rez} altfel apasa \'n\' =")
            if continuu == 'n':
                print(f"Rezultat final = {first_rez}")
                run = False



calculator()
