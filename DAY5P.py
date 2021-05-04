# ord sa transformam din char in int
# chr sa transformam din int in char
# caractere speciale
# start 33 ----------------Finish 129
# 33 la 47 inclusiv char special 58 la 64, 91 la 96, 123 la 128
# 48 la 57 inclusiv cifre
# 65 la 90 si de la 97 la 122 litere mari si mici

import random
print("Bine ai venit la Generatorul de parole BY POPA GEORGE-ALEXANDRU <3")
cifre = []
litere = []
caractere = []

for i in range(33, 127):
    if (i >= 48) & (i <= 57):
        cifre.append(chr(i))
    elif ((i >= 65) & (i <= 90)) | ((i >= 97) & (i <= 122)):
        litere.append(chr(i))
    else:
        caractere.append(chr(i))
password = ''
print("Pentru a parola sigura aceasta trebuie sa contina : \n ")
print("-- 8 elemente")
print("-- cel puitin o litera mica")
print("-- cel putin litera mare")
print("-- cel putin 1 caracter special")
print("-- cel putin o cifra")
nr_litere = int(input("Cate litere vrei sa contina parola? :"))
nr_cifre = int(input("Cate cifre  vrei sa contina parola? :"))
nr_char = int(input("Cate caractere vrei sa contina? :"))

for i in range(nr_cifre):
    password += random.choice(cifre)
for i in range(nr_litere):
    password += random.choice(litere)
for i in range(nr_char):
    password += random.choice(caractere)

# amestecarea caracterelor
print(f"Parola generata de catre noi este ==  \"{''.join(random.sample(password, len(password)))}\"")
