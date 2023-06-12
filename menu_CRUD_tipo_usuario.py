from DTO.tipo_usuario import Tipo_Usuario
from DTO.validadores import *
from termcolor import colored
import DAO.CRUD_Tipo_Usuario
import os, time

def ingresar_tipo_usuario():
    rol = input("Ingrese el rol del usuario: ")
    estado = int(input("Ingrese su estado [1. Activo | 0. Inactivo]: "))
    tipo_usuario = Tipo_Usuario(nombre_tipo_usuario=rol, estado=estado)
    DAO.CRUD_Tipo_Usuario.ingresar(tipo_usuario)

def consultar_todo():
    datos = DAO.CRUD_Tipo_Usuario.mostrarTodos()
    for data in datos:
        print(f"ID Tipo de Usuario: {data[0]} | Nombre del Tipo de Usuario: {data[1]} | Estado: {data[2]}")

def consulta_parcial(cantidad):
    datos = DAO.CRUD_Tipo_Usuario.mostrarParcial(cant=cantidad)
    for data in datos:
        print(f"ID Tipo de Usuario: {data[0]} | Nombre del Tipo de Usuario: {data[1]} | Estado: {data[2]}")

def consulta_particular(id_tipo_usuario):
    print(f"Datos del Tipo de Usuario con ID {id_tipo_usuario}")
    data = DAO.CRUD_Tipo_Usuario.mostrarParticular(id=id_tipo_usuario)
    print(f"ID Tipo de Usuario: {data[0]} | Nombre del Tipo de Usuario: {data[1]} | Estado: {data[2]}")

def consultar_tipo_usuario():
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
            os.system("cls")
            cantidad_mostrar = int(input("Ingrese la cantidad de tipos de usuario a visualizar: "))
            # Validar la cantidad introducida.
            consulta_parcial(cantidad=cantidad_mostrar)
        elif opcion == 3:
            os.system("cls")
            id_tipo_usuario_mostrar = int(input("Ingrese el ID del tipo de usuario a eliminar: "))
            # Validar el ID introducido
            consulta_particular(id_tipo_usuario=id_tipo_usuario_mostrar)
        elif opcion == 4:
            opcion_volver_salir = input("Desea salir? " + colored("Si","green") + "/" + colored("No","red") + ": ").lower()
            if opcion_volver_salir == "si":
                break
                
def eliminar_tipo_usuario():
    consultar_todo()
    id_eliminar = int(input("Ingrese el ID del Tipo de Usuario a eliminar: "))
    time.sleep(1)
    DAO.CRUD_Tipo_Usuario.eliminar(id=id_eliminar)

def menu_tipo_usuario():
    while True:
        print("\n \n" + "\t" * 6 + "1- Ingresar tipo_usuario")
        print("\t" * 6 + "2- Modificar tipo_usuario")
        print("\t" * 6 + "3- Eliminar tipo_usuario")
        print("\t" * 6 + "4- Consultar tipo_usuario")
        print("\t" * 6 + "5- Salir del CRUD de Tipo de Usuario")
        opcion = int(input("\n" + "\t" * 6 +"Opcion: "))

        if opcion == 1:
            os.system("cls")
            ingresar_tipo_usuario()
        elif opcion == 2:
            os.system("cls")
            print("Work in progress")
            time.sleep(2)
        elif opcion == 3:
            os.system("cls")
            eliminar_tipo_usuario()
        elif opcion == 4:
            os.system("cls")
            consultar_tipo_usuario()
        elif opcion == 5:
            opcion_volver_salir = input("Desea salir?: " + colored("Si","green") + "/" + colored("No","red") + ": ").lower()
            if opcion_volver_salir == "si":
                os.system("cls")
                break
        else:
            print("Esa opcion no es valida. Intentalo de nuevo")
            time.sleep(1)