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

    # Hacer una lista que contenga caracteres no admisibles en un correo para tener en consideracion durante la validacion.
    # Cambiar los returns de True o False a mensajes interactivos.

    validador = "xxx.xx"

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
    