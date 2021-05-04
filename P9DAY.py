import art
print(art.logo)


def maxim_from_dictionar(dictionar):
    max = 0
    for i in dictionar:
        if dictionar[i] > max:
            max = pers[i]
            winner = i
    print(f"Castigatorul este {winner} care a licitat cu {max}")


run = True
pers = {}
while run:
    name = input("Numele cu care liciteaza: ")
    suma = int(input("Suma = $"))
    pers[name] = suma
    again = input("Vrea cineva sa mai liciteze ? DA/NU").lower()
    if again == 'da':
        run = True
        # print('\n' * 50)
    elif again == 'nu':
        run = False
        maxim_from_dictionar(pers)


