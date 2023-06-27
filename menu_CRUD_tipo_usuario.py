from DTO.tipo_usuario import Tipo_Usuario
from DTO.validadores import *
from termcolor import colored
import DAO.CRUD_Tipo_Usuario
import os, time

# Centrar texto
def ingresar_tipo_usuario():
    rol = int(input("Ingrese el rol del usuario [1. Administrador | 0. Recepcionista]: "))
    if valida_rol(rol) == False:
        os.system("cls")
        print(valida_rol(rol))
        rol = int(input("Ingrese el rol del usuario [1. Administrador | 0. Recepcionista]: "))
    rol = valida_rol(rol_usuario=rol)
    estado = int(input("Ingrese su estado [1. Activo | 0. Inactivo]: "))
    tipo_usuario = Tipo_Usuario(nombre_tipo_usuario=rol, estado=estado)
    DAO.CRUD_Tipo_Usuario.ingresar(tipo_usuario)
    time.sleep(1)

def consultar_todo():
    datos = DAO.CRUD_Tipo_Usuario.mostrar_todos()
    for data in datos:
        print(f"ID Tipo de Usuario: {data[0]} | Nombre del Tipo de Usuario: {data[1]} | Estado: {data[2]}")

def consulta_parcial(cantidad):
    datos = DAO.CRUD_Tipo_Usuario.mostrar_parcial(cant=cantidad)
    for data in datos:
        print(f"ID Tipo de Usuario: {data[0]} | Nombre del Tipo de Usuario: {data[1]} | Estado: {data[2]}")

def consulta_particular(id_tipo_usuario):
    print(f"Datos del Tipo de Usuario con ID {id_tipo_usuario}")
    data = DAO.CRUD_Tipo_Usuario.mostrar_particular(id=id_tipo_usuario)
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
            consulta_parcial(cantidad=cantidad_mostrar)
        elif opcion == 3:
            os.system("cls")
            id_tipo_usuario_mostrar = int(input("Ingrese el ID del tipo de usuario a eliminar: "))
            consulta_particular(id_tipo_usuario=id_tipo_usuario_mostrar)
        elif opcion == 4:
            opcion_volver_salir = input("Desea salir? " + colored("Si","green") + "/" + colored("No","red") + ": ").lower()
            if opcion_volver_salir == "si":
                break


# Rol validado al modificar
def modificar_tipo_usuario():
    nuevos_datos = []
    consultar_todo()
    id_modificar = int(input("Ingrese el ID del tipo de usuario a modificar: "))
    datos_actuales = DAO.CRUD_Tipo_Usuario.mostrar_particular(id=id_modificar)

    nuevos_datos.append(datos_actuales[0])

    opc = input(f"¿Desea modificar el tipo de usuario? [1. Administrador | 0. Recepcionista] Actual: {datos_actuales[1]} [SI/NO]: ").lower()
    if opc == "si":
        nuevo_tipo_usuario = int(input("Ingrese el nuevo tipo de usuario: "))
        if valida_rol(nuevo_tipo_usuario) == False:
            os.system("cls")
            print(valida_rol(nuevo_tipo_usuario))
            nuevo_tipo_usuario = int(input("Ingrese el rol del usuario [1. Administrador | 0. Recepcionista]: "))
            nuevo_tipo_usuario = valida_rol(nuevo_tipo_usuario)
            nuevos_datos.append(nuevo_tipo_usuario)
        else:
            nuevo_tipo_usuario = valida_rol(nuevo_tipo_usuario)
            nuevos_datos.append(nuevo_tipo_usuario)
    else:
        nuevos_datos.append(datos_actuales[1])

    opc = input(f"¿Desea modificar el estado del tipo de usuario? Actual: {datos_actuales[2]} [SI/NO]: ").lower()
    if opc == "si":
        nuevo_estado = int(input("Ingrese el nuevo estado [1. Activo | 0. Inactivo]: "))
        nuevos_datos.append(nuevo_estado)
    else:
        nuevos_datos.append(datos_actuales[2])

    DAO.CRUD_Tipo_Usuario.modificar(tipo_usu=nuevos_datos)
    time.sleep(1)
                
def eliminar_tipo_usuario():
    consultar_todo()
    id_eliminar = int(input("Ingrese el ID del Tipo de Usuario a eliminar: "))
    DAO.CRUD_Tipo_Usuario.eliminar(id=id_eliminar)
    time.sleep(1)

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
            modificar_tipo_usuario()
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