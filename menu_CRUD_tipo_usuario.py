import DAO.CRUD_Tipo_Usuario
from DTO.tipo_usuario import Tipo_Usuario

rol = input("Ingrese el rol del usuario: ")
estado = int(input("Ingrese su estado [1. Activo | 0. Inactivo]: "))
tipo_usuario = Tipo_Usuario(nombre_tipo_usuario=rol, estado=estado)
DAO.CRUD_Tipo_Usuario.ingresar(tipo_usuario)
