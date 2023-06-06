from DTO.conexion import Conexion

#Definir los datos para la conexión
host='localhost'
user='root'
password=''
db='mydb'

#Función Ingresar
def ingresar(usu):
    try:
        con=Conexion(db, host, password, user)

        sql="INSERT INTO usuario SET nombre='{}',apellidoPaterno='{}',sexo='{}'," \
            "rut='{}',direccion='{}',correo='{}',telefono='{}', Tipo_Usuario_idTipo_Usuario = 1," \
            "apellidoMaterno='{}'".\
            format(usu.nombre,usu.apellido_paterno,usu.sexo,usu.rut,usu.direccion,usu.correo,
                   usu.telefono,usu.apellido_materno)

        con.ejecutar_query(sql)
        con.commit()
        print("Datos Ingresados con Éxito :)")
        con.disconnect()

    except Exception as e:
        print("Error al Insertar: ",e)

#Función Modificar
def modificar(usu):
    try:
        con=Conexion(db, host, password, user)

        sql="UPDATE usuario SET rut='{}', nombre='{},'apellidoPaterno='{}',sexo='{}'," \
            ",direccion='{}',correo='{}',telefono='{}'," \
            "apellidoMaterno='{}' WHERE idUsuario= {}".\
            format(usu[4],usu[1],usu[2],usu[3],usu[5],usu[6],usu[7],usu[9],usu[0])

        con.ejecutar_query(sql)
        con.commit()
        print("Modificación Exitosa :)")
        con.disconnect()

    except Exception as e:
        print("Error en la Modificación: ",e)


#Función eliminar
def eliminar(id):
    try:
        con=Conexion(db, host, password, user)

        sql="DELETE FROM usuario WHERE idUsuario={}".\
            format(id)

        con.ejecutar_query(sql)
        con.commit()
        print("Eliminación Exitosa :)")
        con.disconnect()

    except Exception as e:
        print("Error al eliminar: ",e)

#Función MosrtrarTodos

def mostrarTodos():
    try:
        con=Conexion(db, host, password, user)
        sql="SELECT * FROM usuario"

        cursor=con.ejecutar_query(sql)
        datos=cursor.fetchall()
        con.disconnect()
        return datos

    except Exception as e:
        con.rollBack()
        print("Errora al Mostrar Todos: ",e)

#Función Mostrar Particular

def mostrarParticular(id):
    try:
        con=Conexion(db, host, password, user)
        sql="SELECT * FROM usuario WHERE idUsuario={}".format(id)

        cursor=con.ejecutar_query(sql)
        datos=cursor.fetchone()
        con.disconnect()
        return datos

    except Exception as e:
        con.rollBack()
        print("Error en Mosrar Particular: ",e)

def mostrarParcial(cant):
    try:
        con=Conexion(db, host, password, user)
        sql="SELECT * FROM usuario"
        
        cursor=con.ejecutar_query(sql)
        datos=cursor.fetchmany(cant)
        con.disconnect()
        return datos

    except Exception as e:
        con.rollBack()
        print("Error Consulta Parcial: ",e)
