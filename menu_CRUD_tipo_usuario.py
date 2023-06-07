from DTO.tipo_usuario import Tipo_Usuario
from termcolor import colored
import DAO.CRUD_Tipo_Usuario
import os, sys

def ingresar_tipo_usuario():
    rol = input("Ingrese el rol del usuario: ")
    estado = int(input("Ingrese su estado [1. Activo | 0. Inactivo]: "))
    tipo_usuario = Tipo_Usuario(nombre_tipo_usuario=rol, estado=estado)
    DAO.CRUD_Tipo_Usuario.ingresar(tipo_usuario)

def consultar_tipo_usuario(): #Falta mostrar todos los tipos de consulta
    while True:
        print("\n \n" + "\t" * 6 + "1- Mostrar todo")
        print("\t" * 6 + "2- Consulta particular")
        print("\t" * 6 + "3- Volver")
        opcion = int(input("\n" + "\t" * 6 +"Opcion: "))

        if opcion == 3:
            opcion_volver_salir = input("¡Desea salir? " + colored("Quedarse","green") + "/" + colored("Volver","red") + ": ").lower()
            if opcion_volver_salir == "volver":
                break
                

def menu_tipo_usuario():
    while True:
        print("\n \n" + "\t" * 6 + "1- Ingresar tipo_usuario")
        print("\t" * 6 + "2- Modificar tipo_usuario")
        print("\t" * 6 + "3- Eliminar tipo_usuario")
        print("\t" * 6 + "4- Consultar tipo_usuario")
        print("\t" * 6 + "5- Volver/salir")
        opcion = int(input("\n" + "\t" * 6 +"Opcion: "))

        if opcion == 1:
            ingresar_tipo_usuario()
        elif opcion == 4:
            consultar_tipo_usuario()
        elif opcion == 5:
            opcion_volver_salir = input("Ingrese aqui su respuesta: " + colored("volver","green") + "/" + colored("Salir","red") + ": ").lower()
            if opcion_volver_salir == "volver":
                break
            elif opcion_volver_salir == "salir":
                os.system("cls")
                sys.exit()   