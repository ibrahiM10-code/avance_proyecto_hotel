import DAO.CRUD_Usuario
from DTO.usuario import Usuario

nombre = input("Ingrese el nombre del empleado: ")
apellido_paterno = input("Ingrese el apellido paterno del empleado: ")
sexo = input("Ingrese el sexo del empleado: ")
rut = input("Ingrese el RUT del empleado: ")
direccion = input("Ingrese la dirección del empleado: ")
correo = input("Ingrese el correo del empleado: ")
telefono = input("Ingrese el telefono del empleado: ")
apellido_materno = input("Ingrese el apellido materno del empleado: ")

nuevo_usuario = Usuario(nombre=nombre, apellido_paterno=apellido_paterno, sexo=sexo, rut=rut, direccion=direccion, correo=correo, telefono=telefono, apellido_materno=apellido_materno,email="")

DAO.CRUD_Usuario.ingresar(nuevo_usuario)