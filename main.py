from termcolor import colored
from menu_CRUD_usuario import *
from menu_crud_tipo_usuario import *
import DTO.validadores
import os, time, pwinput, sys

# Variables globales para mostrar texto centrado.
tabs_texto = 6
tabs_carga = 4
tabs_carga_texto = 7
lista_carga = [] # Lista de la barra de carga.

# Login
while True:
    print("\n \n" + "\t" * tabs_texto + "Autenticarse.")
    email = input("\n \n" + "\t" * tabs_texto + "Email: " )
    contrasena = pwinput.pwinput(prompt="\t" * tabs_texto + "Contraseña: ", mask="*")
    if DTO.validadores.validaEmail(email):
        print("\n \n" + "\t" * tabs_texto + colored(email, "green") + " es un correo válido.")
        time.sleep(1)
        break
    else:
        print("\n \n" + "\t" * tabs_texto + colored(email, "red") + " no es un correo válido.")
        # Con tal de no repetir el sleep y el limpiar pantalla 2 veces los puse en un bucle for.
        for _ in range(1):
            time.sleep(2)
            os.system("cls")

os.system("cls")

# Carga de la barra
for i in range(100 + 1):
    time.sleep(0.2)
    os.system("cls")
    print("\n \n" + "\t" * tabs_carga_texto + str(i) + "%")
    if i != 0:
        if i % 10 == 0:
            lista_carga.append("#")
    print("\n" + "\t" * tabs_carga + str(colored(lista_carga, "green")))

os.system("cls")


# Menu de todos los CRUD (Principal)
while True:

        print("\t" * tabs_texto + "********************")
        print("\t" * tabs_texto + "Menu principal")
        print("\t" * tabs_texto + "--------------------")
        print("")
        print("\t" * tabs_texto + "1- CRUD de Tipo de Usuario")
        print("\t" * tabs_texto + "2- CRUD de Usuario")
        print("\t" * tabs_texto  + "3- CRUD de Reserva")
        print("\t" * tabs_texto + "4- CRUD de Pasajero")
        print("\t" * tabs_texto  + "5- CRUD de Habitacion")
        print("\t" * tabs_texto + "6- CRUD de Tipo de Habitacion")
        print("\t" * tabs_texto + "7- Salir")
        print("")

        opcion = int(input("\t" * tabs_texto + "Ingresa opcion: "))

        if opcion == 1:
            os.system("cls")
            menu_tipo_usuario()
        elif opcion == 2:
            os.system("cls")
            menu_usuario()
        elif opcion == 7:
            respuesta_salir = input("\t" * 6 + "¿Desea salir: " + colored("Si", "green") + "/" + colored("No: ","red")).lower()
            if respuesta_salir == "si":
                os.system("cls")
                print(colored("\n \n \n \n" + "\t" * 6 + "Saliste...","red"))
                time.sleep(1)
                os.system("cls")
                sys.exit()      
            elif respuesta_salir == "no":
                    print("\t" * 6 + "Estas Aqui...")
        else:
            print("Esa opcion no es valida. Intentalo de nuevo")
            time.sleep(1)
            os.system("cls")