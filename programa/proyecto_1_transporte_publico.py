#PROYECTO 1 - TALLER DE PROGRAMACIÓN

#LEER ARCHIVO DE USUARIOS Y CONTRASEÑAS
#E: Recibe el nombre del archivo con todas las claves y usuarios
#S: Retorna una lista ya preparada con los usuarios y claves separados en texto
#R: El usuario no puede controlar esta función, se ejecuta por medio de login

def usuarios(archivo):
    if isinstance(archivo, str):
        usuarios= []
        contraseñas= []
        with open(archivo, "r") as archivo:
            linea= archivo.readline()
            while linea != "":
                separa= False
                i= 0
                user= ""
                passw= ""
                caracter= ""
                while i < len(linea):
                    caracter= linea[i]
                    if separa != True:
                        if caracter == ";":
                            separa= True
                        else:
                            user= user + caracter
                    else:
                        if caracter != "\n":
                            passw= passw + caracter
                    i= i+1
                usuarios= usuarios + [user]
                contraseñas= contraseñas + [passw]
                linea= archivo.readline()
        return [usuarios, contraseñas]


#INICIO DE SESIÓN
#E: Se llama al querer entrar a el menú de admins
#S: Si la contraseña y el usuario esta bien, permite la entrada, si no, la niega
#R: Solo acepta aquellos usuario y contraseñas que esten el archivo de texto leido por la función usuarios

def login():
    datos= usuarios("login.txt")
    usuario= datos[0]
    contraseña= datos[1]
    print("\nMenú de administradores, porfavor ingrese sus credenciales")
    user= input("Usuario: ")
    password= input("Contraseña: ")
    i= 0
    acceso= False
    while i < len(usuario):
        if user == usuario[i] and password == contraseña[i]:
            acceso= True
        i= i+1
    if acceso == True:
        print("\n¡Bienvenido!")
        menu_admin()
    else:
        print("\nUsuario o contraseña incorrectos, vuelva a intentarlo")


#MENÚ USUARIOS
#E: Cuando se ingresa 2 en el menú principal
#S: Muestra todas las opciones del menu para usuarios
#R: Se limita a las opciones que se muestran en pantalla

def menu_user():
    while True:
        print("\n== MENÚ DE USUARIO ==")
        print("(21) Consulta de salidas")
        print("(22) Registro de abordaje")
        print("(23) Anulación de abordaje")
        print("(24) Regresar al menú principal")
        opcion= input("Elija una opción: ")

        if opcion == "24":
            print("Volviendo al menú principal")
            menu_principal()
        else:
            print("Esto no es una opción,porfavor escoja un número valido")

#MENÚ ADMINISTRATIVO
#E: Cuando se ingresa 1 en el menú principal
#S: Muestra todas las opciones del menu administrativo
#R: Se limita a las opciones que se muestran en pantalla

def menu_admin():
    while True:
        print("\n== MENÚ ADMINISTRATIVO ==")
        print("(11) Gestión de modelos de autobús")
        print("(12) Gestión de unidades")
        print("(13) Gestión de conductores")
        print("(14) Gestión de rutas")
        print("(15) Gestión de paradas por ruta")
        print("(16) Programación de salidas")
        print("(17) Consultar historial de abordajes")
        print("(18) Regresar al menú principal")
        opcion= input("Elija una opción: ")
        
        if opcion == "11":
            print("PLACEHOLDER")
        elif opcion == "18":
            print("Volviendo al menú principal")
            menu_principal()
        else:
            print("Esto no es una opción,porfavor escoja un número valido")


#FUNCIÓN MENÚ PRINCIPAL
#E: No tiene, se carga automáticamente cuando se corre el archivo
#S: Despliega el menú principal,donde accederemos a varios modos
#R: Se limita a las opciones que se muestran en pantalla

def menu_principal():
    while True:
        print("\nBienvenidos al Sistema TP")
        print("\n== MENÚ PRINCIPAL ==")
        print("(1) Opciones Administrativas")
        print("(2) Opciones de Usuario")
        print("(3) Salir")

        opcion= input("Elija una opcion: ")
        if opcion == "1":
            menu_admin()
        elif opcion == "2":
            login()
        elif opcion == "3":
            print("¡Gracias por preferirnos!")
            print("Saliendo...")
            break #Por el momento, buscar una mejor manera luego
        else:
            print("Opción no valida, porfavor escoja uno de los números disponibles")
#Inicializar menú
menu_principal()

