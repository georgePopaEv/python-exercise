bani = float(input("Cati bani ai in total? :"))
# trecem suma de bani
# alegem dobanda dintre 10, 12 sau 15
# vedem la cati o umprumuta sau a cata parte
# Calculam cat tre sa plateasca fiecare persoana inapoi

dobanda = int(input("Cat este dobanda la care imprumuti?10, 12 sau 15? "))
split = int(input("La cati oameni se imparte banca?"))

back = round(bani / split * (1+dobanda/100) , 2)

if (dobanda == 10) | (dobanda == 12) | (dobanda == 15):
    print(f"fiecare persoana trebuie sa plateasca : ${back} ")
else:
    print("Eroare de introducere a dobanzii!")