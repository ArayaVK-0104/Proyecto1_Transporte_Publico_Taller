#PROYECTO 1 - TALLER DE PROGRAMACIÓN

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
            menu_user()
        elif opcion == "3":
            print("¡Gracias por preferirnos!")
            print("Saliendo...")
            break #Por el momento, buscar una mejor manera luego
        else:
            print("Opción no valida, porfavor escoja uno de los números disponibles")
#Inicializar menú
menu_principal()








#Creación de un sistema de contraseñas para acceso

#IDEA PRINCIPAL: Que cuando el usuario quiera acceder, tenga que ingresar una contraseña
#Se va a componer de Usuario;Contrseña, ambos guardados en un archivo de texto

#Desde el archivo Python recibe un solo string: "Kris;1234"
#Hay que buscar la manera de que reconozca a ; como separador
