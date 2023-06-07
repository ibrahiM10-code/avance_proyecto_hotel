from DTO.usuario import Usuario
from termcolor import colored
import DAO.CRUD_Usuario
import os, sys

def ingresar_datos_usuario():
    nombre = input("Ingrese el nombre del empleado: ")
    apellido_paterno = input("Ingrese el apellido paterno del empleado: ")
    sexo = input("Ingrese el sexo del empleado: ")
    rut = input("Ingrese el RUT del empleado: ")
    direccion = input("Ingrese la dirección del empleado: ")
    correo = input("Ingrese el correo del empleado: ")
    telefono = input("Ingrese el telefono del empleado: ")
    tipo_usuario_id = int(input("Ingrese el ID del tipo de usuario: "))
    apellido_materno = input("Ingrese el apellido materno del empleado: ")

    nuevo_usuario = Usuario(nombre=nombre, apellido_paterno=apellido_paterno, sexo=sexo, rut=rut, direccion=direccion, correo=correo, telefono=telefono, id_tipo_usuario=tipo_usuario_id, apellido_materno=apellido_materno,email="")

    DAO.CRUD_Usuario.ingresar(nuevo_usuario)


def consultar_todo():
    print("Datos:")
    datos = DAO.CRUD_Usuario.mostrar_todos()
    for data in datos:
       print(f"ID: {data[0]}| Nombre: {data[1]} | A. Paterno: {data[2]} | A. Materno: {data[9]}\nSexo: {data[3]} | RUT: {data[4]} | Direccion: {data[5]} | Correo: {data[6]}\nTelefono: {data[7]}") 

def consultar_parcial(cantidad):
    print(f"Datos de {cantidad} usuario(s):")
    datos = DAO.CRUD_Usuario.mostrar_parcial(cant=cantidad)
    for data in datos:
       print(f"ID: {data[0]} | Nombre: {data[1]} | A. Paterno: {data[2]} | A. Materno: {data[9]} | Sexo: {data[3]}\nRUT: {data[4]} | Direccion: {data[5]} | Correo: {data[6]} | Telefono: {data[7]}") 

def consultar_particular(id_usuario):
    print(f"Datos del usuario con ID {id_usuario}:")
    data = DAO.CRUD_Usuario.mostrar_particular(id=id_usuario)
    print(f"ID: {data[0]} | Nombre: {data[1]} | A. Paterno: {data[2]} | A. Materno: {data[9]} | Sexo: {data[3]}\nRUT: {data[4]} | Direccion: {data[5]} | Correo: {data[6]}\nTelefono: {data[7]}") 

def consulta_usuario():
    while True:
        print("\n \n" + "\t" * 6 + "1- Mostrar todo")
        print("\n \n" + "\t" * 6 + "2- Consulta parcial")
        print("\t" * 6 + "3- Consulta particular")
        print("\t" * 6 + "4- Volver/salir")
        opcion = int(input("\n" + "\t" * 6 +"Opcion: "))

        if opcion == 1:
            consultar_todo()
        elif opcion == 2:
            cantidad_mostrar = int(input("Ingrese la cantidad de usuarios que desea mostrar: "))
            consultar_parcial(cantidad=cantidad_mostrar)
        elif opcion == 3:
            id_usuario_mostrar = int(input("Ingrese el ID del usuario que desea consultar: "))
            consultar_particular(id_usuario=id_usuario_mostrar)
        elif opcion == 4:
            opcion_volver_salir = input("Ingrese aqui su respuesta: " + colored("volver","green") + "/" + colored("Salir","red") + ": ").lower()
            if opcion_volver_salir == "volver":
                break
            if opcion_volver_salir == "salir":
                os.system("cls")
                sys.exit()

def modificar_usuario():
    nuevos_datos = []
    consultar_todo()
    id_modificar = int(input("Ingrese el ID del usuario a modificar: "))
    datos_actuales = DAO.CRUD_Usuario.mostrar_particular(id=id_modificar)
    
    nuevos_datos.append(datos_actuales[0])
    nuevos_datos.append(datos_actuales[4])
    nuevos_datos.append(datos_actuales[10])

    opc = input(f"¿Desea modificar el nombre del usuario? Actual: {datos_actuales[1]} [SI/NO]: ").lower()
    if opc == "si":
        nuevo_nombre = input("Ingrese el nombre nuevo: ")
        nuevos_datos.append(nuevo_nombre)
    else:
        nuevos_datos.append(datos_actuales[1])

    opc = input(f"¿Desea modificar el apellido paterno del usuario? Actual: {datos_actuales[2]} [SI/NO]: ").lower()
    if opc == "si":
        nuevo_apellido_paterno = input("Ingrese el apellido paterno nuevo: ")
        nuevos_datos.append(nuevo_apellido_paterno)
    else:
        nuevos_datos.append(datos_actuales[2])

    opc = input(f"¿Desea modificar el sexo del usuario? Actual: {datos_actuales[3]} [SI/NO]: ").lower()
    if opc == "si":
        nuevo_sexo = input("Ingrese el sexo nuevo: ")
        nuevos_datos.append(nuevo_sexo)
    else:
        nuevos_datos.append(datos_actuales[3])

    opc = input(f"¿Desea modificar la dirección del usuario? Actual: {datos_actuales[5]} [SI/NO]: ").lower()
    if opc == "si":
        nueva_direccion = input("Ingrese la nueva dirección: ")
        nuevos_datos.append(nueva_direccion)
    else:
        nuevos_datos.append(datos_actuales[5])

    opc = input(f"¿Desea modificar el correo del usuario? Actual: {datos_actuales[6]} [SI/NO]: ").lower()
    if opc == "si":
        nuevo_correo = input("Ingrese el correo nuevo: ")
        nuevos_datos.append(nuevo_correo)
    else:
        nuevos_datos.append(datos_actuales[6])

    opc = input(f"¿Desea modificar el telefono del usuario? Actual: {datos_actuales[7]} [SI/NO]: ").lower()
    if opc == "si":
        nuevo_telefono = input("Ingrese el telefono nuevo: ")
        nuevos_datos.append(nuevo_telefono)
    else:
        nuevos_datos.append(datos_actuales[7])

    opc = input(f"¿Desea modificar el apellido materno del usuario? Actual: {datos_actuales[9]} [SI/NO]: ").lower()
    if opc == "si":
        nuevo_apellido_materno = input("Ingrese el apellido materno nuevo: ")
        nuevos_datos.append(nuevo_apellido_materno)
    else:
        nuevos_datos.append(datos_actuales[9])

    DAO.CRUD_Usuario.modificar(usu=nuevos_datos)

def menu_usuario():
    while True:
        print("\n \n" + "\t" * 6 + "1- Ingresar usuario")
        print("\t" * 6 + "2- Modificar usuario")
        print("\t" * 6 + "3- Eliminar usuario")
        print("\t" * 6 + "4- Consultar usuario")
        print("\t" * 6 + "5- Volver")
        opcion = int(input("\n" + "\t" * 6 +"Opcion: "))
        if opcion == 1:
            ingresar_datos_usuario()
        elif opcion == 2:
            modificar_usuario()
        elif opcion == 4:
            consulta_usuario()
        else:
            break
    # if opcion == 4:
    #     from DTO.MENUconsulta_usu import consulta_Usu
    #     consulta_Usu()        
    # if opcion == 5:
    #     opcionVolver_Salir = input("Ingrese aqui su respuesta: " + colored("volver","green") + "/" + colored("Salir","red") + ": ").lower()
    #     if opcionVolver_Salir == "volver":
    #         from DTO.menuPrincipal import MenuPrincipal
    #         MenuPrincipal()
    #     if opcionVolver_Salir == "salir":
    #         os.system("cls")
    #         sys.exit()
