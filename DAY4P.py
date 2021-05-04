import random
print("Ce alegi? 0 - piatra, 1 - Plasa, 2 - Foarfeca")
print("Bine ai venit la jocul balenelor albastre de Piatra Hartie sau Foarfeca:))))")
# user = int(input("Alege ceva: "))
hartie = '''
    _________
___*    _____)_____
            _______)
            ________)
           ________)
---*_____________)
'''
foarfeca = '''
    _________
___*    _____)_____
            _______)
            ________)
        (____)
---*____(___)
'''
piatra = '''
    _________
___*    _____)
        (_____)
        (_____)
        (____)
---* ___(___)
'''
# 0 piatra 1 Hartie 2 Foarfeca


forme = [piatra, hartie, foarfeca]
score_pc = 0
score_user = 0
username = input("Introdu numele de user: ")
while(score_pc < 3) & (score_user < 3):
    print(f"Scorul general este de {username}== {score_user} si /// pc=={score_pc}")
    user = int(input("Alege ceva(0-p, 1-h , 2-f ) :"))
    pc = random.randint(0, 2)
    # piatra - piatra
    if pc == user == 0:
        print('-----EGALITATE-----')
        print(f"pc-ul a dat \n{forme[pc]} ")
        print(f"Ai dat \n {forme[user]}")
    # piatra hartie
    elif(pc == 0) & (user == 1):
        print("Ai Castigat un punct")
        print(f"pc-ul a dat \n{forme[pc]} ")
        print(f"Ai dat \n {forme[user]}")
        score_user += 1
    # piatra foarfeca
    elif(pc == 0) & (user == 2):
        print("Ai pierdut un punct")
        print(f"pc-ul a dat \n{forme[pc]} ")
        print(f"Ai dat \n {forme[user]}")
        score_pc += 1
    # hartie piatra
    elif (pc == 1) & (user == 0):
        print("Ai pierdut un punct")
        print(f"pc-ul a dat \n{forme[pc]} ")
        print(f"Ai dat \n {forme[user]}")
        score_pc += 1
    # HARTIE - foarfeca
    elif (pc == 1) & (user == 2):
        print("Ai castigat un punct")
        print(f"pc-ul a dat \n{forme[pc]} ")
        print(f"Ai dat \n {forme[user]}")
        score_user += 1
    # Hartie Hartie
    elif (pc == 1) & (user == 1):
        print("-----EGALITATE-----")
        print(f"pc-ul a dat \n{forme[pc]} ")
        print(f"Ai dat \n {forme[user]}")
    # Foarfeca - Foarfeca
    elif (pc == 2) & (user == 2):
        print("-----EGALITATE-----")
        print(f"pc-ul a dat \n{forme[pc]} ")
        print(f"Ai dat \n {forme[user]}")
    # Foarfeca - HARTIE
    elif (pc == 2) & (user == 1):
        print("Ai pierdut un punct")
        print(f"pc-ul a dat \n{forme[pc]} ")
        print(f"Ai dat \n {forme[user]}")
        score_pc += 1
    # Foarfeca - piatra
    elif (pc == 2) & (user == 0):
        print("Ai castigat un punct")
        print(f"pc-ul a dat \n{forme[pc]} ")
        print(f"Ai dat \n {forme[user]}")
        score_user += 1

if score_user > score_pc:
    print(f"Felicitari ai castigat cu scorul de {score_user} -- {score_pc}")
else:
    print(f"Din pacate esti un pierzator :(((( cu scorul de {score_user} -- {score_pc}")
