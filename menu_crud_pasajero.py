import os,time
from termcolor import colored
from DTO.validadores import *
from DAO.CRUD_Pasajero import *
from DTO.pasajero import Pasajero 
from DAO.CRUD_Pasajero import *

# Funcion ingresar pasajero
# Hacer un validador del si es pasajero responsable o no.
# Indicar en los inputs 1 = responsable | 0 = no responsable.
# Centrar texto donde haga falta.
def ingresar_pasajero():
    print("\t" * 6 +"*****Ingreso de pasajero*****")
    nombre = input("\n \n"+ "\t" * 6 + "Ingrese el nombre del pasajero: ")
    apellido = input("\t" * 6 + "Ingrese el apellido del pasajero: ")
    direccion = input("\t" * 6 + "ingrese la direccion del pasajero: ")
    telefono = input("\t" * 6 + "Ingrese el telefono del pasajero: ")
    rut = input("\t" * 6 + "Ingrese el rut del pasajero: ")
    while(valida_rut(rut) == False):
        os.system("cls")
        print("Rut erroneo...")
        time.sleep(2)
        os.system("cls")
        rut = input("\t" * 6 + "Ingrese el rut nuevamente: ")
    email = input("\t" * 6 + "ingrese el email del pasajero: ")
    while(valida_email(email) == False):
        os.system("cls")
        print("Correo erroneo...")
        time.sleep(2)
        os.system("cls")
        email = input("\t" * 6 + "Ingrese el correo nuevamente: ")
    responsable = int(input("\t" * 6 + "Ingrese el responsable de la reserva: "))
    nuevo_pasajero = Pasajero(nombre = nombre,apellido=apellido,direccion=direccion,telefono=telefono,rut=rut,email=email,responsable=responsable)
    ingresar(nuevo_pasajero)
    time.sleep(1)

# Consultar todo

def consultar_todo():
    print("Datos del pasajero: ")
    datos = mostrar_todos()
    for data in datos:
        print("\n \n"+f"ID: {data[0]}| Nombre: {data[1]} | Apellido: {data[2]} | Direccion: {data[3]} | Telefono: {data[4]} | Rut: {data[5]} | Email: {data[6]} | Responsable: {data[7]}")

# Consulta parcial

def consultar_parcial(cantidad):
    print(f"Datos de {cantidad} pasajero(s): ")
    datos = mostrar_parcial(cantidad)
    for data in datos:
        print(f"ID: {data[0]}| Nombre: {data[1]} | Apellido: {data[2]} | Direccion: {data[3]} | Telefono: {data[4]} | Rut: {data[5]} | Email: {data[6]} | Responsable: {data[7]}")

# Consulta particular

def consultar_particular(id_pasajero):
    print(f"Datos del pasajero con ID {id_pasajero}: ")
    data = mostrar_particular(id = id_pasajero)
    print(f"ID: {data[0]}| Nombre: {data[1]} | Apellido: {data[2]} | Direccion: {data[3]} | Telefono: {data[4]} | Rut: {data[5]} | Email: {data[6]} | Responsable: {data[7]}")

# Menu de consultas
def menu_consultas():
    while True:
        print("\n \n" + "\t" * 6 + "1- Mostrar todo.")
        print("\t" * 6 + "2- Consulta parcial.")
        print("\t" * 6 + "3- Consulta particular.")
        print("\t" * 6 + "4- Salir del Menu de consultas.")
        opcion = int(input("\n" + "\t" * 6 +"Opcion: "))

        if opcion == 1:
            os.system("cls")
            consultar_todo()
        elif opcion == 2:
            cantidad_mostrar = int(input("Ingrese la cantidad de pasajeros que desea mostrar: "))
            os.system("cls")
            consultar_parcial(cantidad=cantidad_mostrar)
        elif opcion == 3:
            id_pasajero_mostrar = int(input("Ingrese el ID del pasajero que desea consultar: "))
            os.system("cls")
            consultar_particular(id_pasajero=id_pasajero_mostrar)
        elif opcion == 4:
            opcion_volver_salir = input("Ingrese aqui su respuesta: " + colored("Si","green") + "/" + colored("No","red") + ": ").lower()
            if opcion_volver_salir == "si":
                os.system("cls")
                break

# Funcion modificar pasajero

def modificar_pasajero():
    nuevos_datos = []
    consultar_todo()
    id_modificar = int(input("Ingrese el ID del pasajero a modificar: "))
    datos_actuales = mostrar_particular(id=id_modificar)

    nuevos_datos.append(datos_actuales[0])

    opc = input(f"¿Desea modificar el nombre del pasajero? Datos actuales: {datos_actuales[1]} [SI/NO]: ").lower()
    if opc == "si":
        nuevo_nombre = input("Ingrese el nuevo nombre del pasajero: ")
        nuevos_datos.append(nuevo_nombre)
    else:
        nuevos_datos.append(datos_actuales[1])


    opc = input(f"¿Desea modificar el apellido del pasajero? Datos actuales: {datos_actuales[2]} [SI/NO]: ").lower()
    if opc == "si":
        nuevo_apellido = input("Ingrese el nuevo apellido del pasajero: ")
        nuevos_datos.append(nuevo_apellido)
    else:
        nuevos_datos.append(datos_actuales[2])


    opc = input(f"¿Desea modificar la direccion del pasajero? Datos actuales: {datos_actuales[3]} [SI/NO]: ").lower()
    if opc == "si":
        nuevo_direccion = input("Ingrese el nuevo direccion del pasajero: ")
        nuevos_datos.append(nuevo_direccion)
    else:
        nuevos_datos.append(datos_actuales[3])


    opc = input(f"¿Desea modificar el telefono del pasajero? Datos actuales: {datos_actuales[4]} [SI/NO]: ").lower()
    if opc == "si":
        nuevo_telefono = input("Ingrese el nuevo telefono del pasajero: ")
        nuevos_datos.append(nuevo_telefono)
    else:
        nuevos_datos.append(datos_actuales[4])


    opc = input(f"¿Desea modificar el rut del pasajero? Datos actuales: {datos_actuales[5]} [SI/NO]: ").lower()
    if opc == "si":
        nuevo_rut = input("Ingrese el nuevo rut del pasajero: ")
        while(valida_rut(nuevo_rut) == False):
            print("\t" * 6 + "Rut invalido...")
            time.sleep(2)
            os.system("cls")
            nuevo_rut = input("Ingrese nuevamente el nuevo rut del pasajero: ")

        nuevos_datos.append(nuevo_nombre)
    else:
        nuevos_datos.append(datos_actuales[5])


    opc = input(f"¿Desea modificar el email del pasajero? Datos actuales: {datos_actuales[6]} [SI/NO]: ").lower()
    if opc == "si":
        nuevo_email = input("Ingrese el nuevo email del pasajero: ")
        while(valida_email(nuevo_email) == False):
            print("\t" * 6 + "Email invalido...")
            time.sleep(2)
            os.system("cls")
            nuevo_email = input("Ingrese nuevamente el nuevo email del pasajero: ")

        nuevos_datos.append(nuevo_email)
    else:
        nuevos_datos.append(datos_actuales[6])


    opc = input(f"¿Desea modificar el responsable del pasajero? Datos actuales: {datos_actuales[7]} [SI/NO]: ").lower()
    if opc == "si":
        nuevo_responsable = input("Ingrese el nuevo responsable del pasajero: ")
        nuevos_datos.append(nuevo_responsable)
    else:
        nuevos_datos.append(datos_actuales[7])
    modificar(pasajero=nuevos_datos)
    time.sleep(1)

# Funcion eliminar pasajero
def eliminar_pasajero():
    consultar_todo()
    id_eliminar = int(input("Ingrese el ID del pasajero a eliminar: "))
    eliminar(id=id_eliminar)
    time.sleep(1)


# menu del pasajero
def menu_pasajero():
    while True:
        os.system("cls")
        print("\n \n" + "\t" * 6 + "1- Ingresar pasajero")
        print("\t" * 6 + "2- Modificar pasajero")
        print("\t" * 6 + "3- Eliminar pasajero")
        print("\t" * 6 + "4- Consultar pasajero")
        print("\t" * 6 + "5- Salir del CRUD de pasajero")
        opcion = int(input("\n" + "\t" * 6 +"Opcion: "))
        if opcion == 1:
            os.system("cls")
            ingresar_pasajero()
        elif opcion == 2:
            os.system("cls")
            modificar_pasajero()
        elif opcion == 3:
            os.system("cls")
            eliminar_pasajero()
        elif opcion == 4:
            os.system("cls")
            menu_consultas()
        elif opcion == 5:
            opcion_salir = input("Desea salir? "+ colored("Si","green") + "/" + colored("No","red")+ ": ").lower()
            if opcion_salir == "si":
                os.system("cls")
                break
        else:
            print("Esa opcion no es valida. Intentalo de nuevo")
            time.sleep(1)
    