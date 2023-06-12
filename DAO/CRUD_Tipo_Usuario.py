from DTO.conexion import Conexion

#Definir los datos para la conexión
host='localhost'
user='root'
password=''
db='mydb'

#Función Ingresar
def ingresar(tipo_usu):
    try:
        con = Conexion(db, host, password, user)

        sql=f"INSERT INTO tipo_usuario SET nombre_tipo_usuario = '{tipo_usu.nombre_tipo_usuario}', estado ='{tipo_usu.estado}'"

        con.ejecutar_query(sql)
        con.commit()
        print("Datos Ingresados con Éxito :)")
        con.disconnect()

    except Exception as e:
        print("Error al Insertar: ",e)

#Función Modificar
def modificar(tipo_usu):
    try:
        con = Conexion(db, host, password, user)

        sql = f"UPDATE tipo_usuario SET nombre_tipo_usuario = '{tipo_usu[1]}', estado = '{tipo_usu[2]}' WHERE idTipo_Usuario = {tipo_usu[0]}"

        con.ejecutar_query(sql)
        con.commit()
        print("Modificación Exitosa :)")
        con.disconnect()

    except Exception as e:
        print("Error en la Modificación: ",e)


#Función eliminar
def eliminar(id):
    try:
        con = Conexion(db, host, password, user)

        sql = f"DELETE FROM tipo_usuario WHERE idTipo_Usuario = {id}"

        con.ejecutar_query(sql)
        con.commit()
        print("Eliminación Exitosa :)")
        con.disconnect()

    except Exception as e:
        print("Error al eliminar: ",e)

#Función MosrtrarTodos

def mostrarTodos():
    try:
        con = Conexion(db, host, password, user)
        sql="SELECT * FROM tipo_usuario"

        cursor=con.ejecutar_query(sql)
        datos=cursor.fetchall()
        con.disconnect()
        return datos

    except Exception as e:
        con.rollback()
        print("Errora al Mostrar Todos: ",e)

#Función Mostrar Particular

def mostrarParticular(id):
    try:
        con = Conexion(db, host, password, user)
        sql = f"SELECT * FROM tipo_usuario WHERE idTipo_Usuario = {id}"

        cursor=con.ejecutar_query(sql)
        datos=cursor.fetchone()
        con.disconnect()
        return datos

    except Exception as e:
        con.rollback()
        print("Error en Mosrar Particular: ",e)

def mostrarParcial(cant):
    try:
        con=Conexion(db, host, password, user)
        sql="SELECT * FROM tipo_usuario"
        
        cursor=con.ejecutar_query(sql)
        datos=cursor.fetchmany(cant)
        con.disconnect()
        return datos

    except Exception as e:
        con.rollback()
        print("Error Consulta Parcial: ",e)
