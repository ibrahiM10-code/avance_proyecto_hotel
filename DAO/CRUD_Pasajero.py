from DTO.conexion import Conexion
import time

#Datos de la conexión
host='localhost'
user='root'
password=''
db='mydb'

# Funcion Ingresar
def ingresar(pasajero):
    try:
        con = Conexion(db,host,password,user)
        sql = f"INSERT INTO pasajero SET idPasajero = NULL, nombre = '{pasajero.nombre}', apellido = '{pasajero.apellido}', direccion = '{pasajero.direccion}', telefono = '{pasajero.telefono}', rut = '{pasajero.rut}', email = '{pasajero.email}', responsable = '{pasajero.responsable}'";
        con.ejecutar_query(sql)
        con.commit()
        print("\n" + "\t" * 6 + "Datos del pasajero ingresados con Exito...")
        con.disconnect()
    except Exception as e:
        print("\n" + "\t" * 6 + "Error al insertar...", e)

# Funcion modificar
def modificar(pasajero):
    try:
        con = Conexion(db,host,password,user)

        sql = f"UPDATE pasajero SET nombre = '{pasajero[1]}', apellido = '{pasajero[2]}', direccion = '{pasajero[3]}', telefono = '{pasajero[4]}', rut = '{pasajero[5]}', email = '{pasajero[6]}', responsable = '{pasajero[7]}'"
        con.ejecutar_query(sql)
        con.commit()
        print("\n" + "\t" * 6 + "Modificacion del pasajero exitosa...")
        con.disconnect()
    except Exception as e:
        print("\n" + "\t" * 6 + "Error en la modificacion del pasajero...  ", e)
        time.sleep(5)

# Funcion eliminar

def eliminar(id):
    try:
        con = Conexion(db,host,password,user)

        sql = f"DELETE FROM pasajero WHERE idPasajero = {id}"
        con.ejecutar_query(sql)
        con.commit()
        print("\n" + "\t" * 6 + "Eliminacion del pasajero exitosa...")
        con.disconnect()
    except Exception as e:
        print("\n" + "\t" * 6 + "Error, no se pudo eliminar al pasajero...  ", e)

# Funcion MostrarTodos

def mostrar_todos():
    try:
        con = Conexion(db,host,password,user)
        sql = "SELECT * FROM pasajero"

        cursor = con.ejecutar_query(sql)

        datos = cursor.fetchall()
        con.disconnect()
        return datos
    except Exception as e:
        con.rollback()
        print("\n" + "\t" * 6 + "Error al mostrar todos los pasajeros...  ", e)
        
# Funcion Mostrar Particular

def mostrar_particular(id):
    try:
        con = Conexion(db,host,password,user)
        sql = f"SELECT * FROM pasajero WHERE idPasajero = {id}"
        
        cursor = con.ejecutar_query(sql)
        datos = cursor.fetchone()
        con.disconnect()
        return datos
    
    except Exception as e:
        con.rollback()
        print("\n" + "\t" * 6 + "Error al mostrar particularmente...  ", e)

# Funcion parcial

def mostrar_parcial(cant):
    try:
        con = Conexion(db,host,password,user)
        sql = "SELECT * FROM pasajero"

        cursor = con.ejecutar_query(sql)
        datos = cursor.fetchmany(cant)
        con.disconnect()
        return datos
    
    except Exception as e:
        con.rollback()
        print("\n" + "\t" * 6 + "Error al mostar parcialmente...  ", e)
