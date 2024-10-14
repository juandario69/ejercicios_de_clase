#ejercicio 3 
USUARIO_BBDD = "admin"
PASSWORD_BBDD = 1234
print("escribe un nombre para tu usuario")
usuario = (input())
print("es necesario que te inventes una contraseña")
contraseña = int(input())
if (contraseña == USUARIO_BBDD) and (contraseña == PASSWORD_BBDD):
    print("acceso concedido")
    else:
        print("acceso denegado")