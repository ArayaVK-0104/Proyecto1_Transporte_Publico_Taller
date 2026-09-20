#PROYECTO 1 - TALLER DE PROGRAMACIÓN

#FUNCIÓN MENÚ PRINCIPAL
#E: No tiene, se carga automáticamente cuando se corre el archivo
#S: Despliega el menú principal,donde accederemos a varios modos
#R: Se limita a las opciones que se muestran en pantalla

def menu_principal():
    menu_p= True
    while menu_p == True:
        print("\nBienvenidos al Sistema TP")
        print("\n-- Menú Principal --")
        print("(1) Opciones Administrativas")
        print("(2) Opciones de Usuario")
        print("(3) Salir")

        opcion= input("Elija una opcion: ")
        if opcion == "1":
            print("Placeholder")
        elif opcion == "2":
            print("Placeholder")
        elif opcion == "3":
            print("¡Gracias por preferirnos!")
            print("Saliendo...")
            menu_p= False
        else:
            print("Opción no valida, porfavor escoja uno de los números disponibles")

menu_principal()

#Creación de un sistema de contraseñas para acceso

#IDEA PRINCIPAL: Que cuando el usuario quiera acceder, tenga que ingresar una contraseña
#Se va a componer de Usuario;Contrseña, ambos guardados en un archivo de texto

#Desde el archivo Python recibe un solo string: "Kris;1234"
#Hay que buscar la manera de que reconozca a ; como separador
