import art


def encode(text, shift):
    code = ''
    if shift > 25:
        print("Valoare de deplasare prea mare")
    else:
        for i in text:
            if ((ord(i) >= 65) & (ord(i) <= 90)) | ((ord(i) >= 97) & (ord(i) <= 122)):
                if (ord(i) + int(shift) > 90) & (ord(i) <= 90):
                    i = chr(64 + ((ord(i) + shift) - 90))
                    code += i
                elif (ord(i) + int(shift) > 122) & (ord(i) <= 122):
                    i = chr(96 + ((ord(i) + shift) - 122))
                    code += i
                else:
                    i = chr(ord(i) + int(shift))
                    code += i
            else:
                code += i

    print(code)


def decode(text, shift):
    decode = ''
    if shift > 25:
        print("Numar de deplasare mai mare")
    else:
        for i in text:
            if ((ord(i) >= 65) & (ord(i) <= 90)) | ((ord(i) >= 97) & (ord(i) <= 122)):
                if (ord(i) - int(shift) < 65) & (ord(i) <= 90):
                    i = chr(91 - (65 - (ord(i) - shift)))
                    decode += i
                    print('ramura1', i)
                elif (ord(i) - int(shift) < 97) & (ord(i) >= 97):
                    i = chr(123 - (97 - (ord(i) - shift)))
                    decode += i
                    print('ramura2', i)
                else:
                    i = chr(ord(i) - int(shift))
                    decode += i
                    print('ramura3', i)
            else:
                decode += i

    print(decode)


run = True


print(art.logo)
while run:
    directie = input("Type decode sau encode :").lower()
    if directie == 'encode':
        text = input("introdu textu :")
        shift = int(input("Tasteaza pasul de litere :"))
        encode(text=text, shift=shift)
    elif directie == 'decode':
        text = input("introdu textu :")
        shift = int(input("Tasteaza pasul de litere :"))
        decode(text=text, shift=shift)
    again = input("Vrei sa mai incerci odata ? scrie Da sau Nu ").lower()
    if again == 'da':
        continue
    elif again == 'nu':
        print("Sfarsit joc si te mai asteptam")
        run = False
