def valida_rut(rut):
    caracteres=".-"
    for x in range(len(caracteres)):
        rut=rut.replace(caracteres[x],"")

    rutsindigito=rut[:len(rut)-1]
    rutinvertido=rutsindigito[::-1]

    multi=2
    sum=0

    for i in range(0,len(rutinvertido)):
        if multi>7:
            multi=2
        sum+=int(rutinvertido[i])*multi
        multi+=1

    dv=11-(sum%11)
    dvu=rut[-1:]

    if dv==11:
        dv=0
    if dv==10:
        dv="K"

    if str(dv)==dvu:
        return True
    else:
        return False
    

def valida_email(email):

    # Caracteres invalidos en email validados
    caracteres_invalidos = ["''", "?", "¿", "¡", "!", "#", "$", "%", "&", "/", "(", ")", "=", "*", "-", "+"]
    validador = "xxx.xx"

    for caracter in caracteres_invalidos:
        if caracter in email:
            print("El email ingresado contiene caracteres invalidos.")
            break
    
    if "@" in email and "." in email:

        mail = email.split("@")[-1].split(".")[0] #gmail
        mail2 = email.split("@")[-1].split(".")[1] #com
        val = validador.split(".")[0] #xxx
        val2 = validador.split(".")[1] #xx
        try: 
            if len(mail) >= len(val) and len(mail2) >= len(val2):
                return True
            else: 
                return False
        except IndexError:
            print("Los correos deben contener un a @, una direccion de email, y un .com o .cl")
    else:
        return False
    
# Valida rol implementado
def valida_rol(rol_usuario):
    match rol_usuario:
        case 1:
            rol_usuario = "Administrador"
        case 0:
            rol_usuario = "Recepcionista"
        case _ :
            return "No hay un rol asociado con este digito"
    return rol_usuario

# Valida sexo implementado
def valida_sexo(sexo_usuario):
    match sexo_usuario:
        case 1:
            sexo_usuario = "Masculino"
        case 0:
            sexo_usuario = "Femenino"
        case _:
            return "No hay un sexo asociado con este digito"
    return sexo_usuario
