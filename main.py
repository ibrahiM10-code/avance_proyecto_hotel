from termcolor import colored
import DTO.validadores
import os, time, pwinput

tabs_texto = 6
tabs_carga = 4
tabs_carga_texto = 7
lista_carga = []

while True:
    print("\n \n" + "\t" * tabs_texto + "Autenticarse.")
    email = input("\n \n" + "\t" * tabs_texto + "Usuario: " )
    contrasena = pwinput.pwinput(prompt="\t" * tabs_texto + "Contraseña: ", mask="*")
    if DTO.validadores.validaEmail(email):
        print("\n \n" + "\t" * tabs_texto + colored(email, "green") + " es un correo válido.")
        time.sleep(2)
        break
    else:
        print("\n \n" + "\t" * tabs_texto + colored(email, "red") + " no es un correo válido.")
        for _ in range(1):
            time.sleep(2)
            os.system("cls")

os.system("cls")

for i in range(100 + 1):
    time.sleep(0.1)
    os.system("cls")
    print("\n \n" + "\t" * tabs_carga_texto + str(i) + "%")
    if i != 0:
        if i % 10 == 0:
            lista_carga.append("🟩")
    print("\n" + "\t" * tabs_carga + str(lista_carga))

os.system("cls")