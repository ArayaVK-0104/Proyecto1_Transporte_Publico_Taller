#PROYECTO 1 - TALLER DE PROGRAMACIÓN

"""
                                                          ===  SECCIÓN DE LAS FUNCIONES OPERATIVAS ===
                                                          
                            Aqui es desde donde se trabaja roda la lógica detrás del programa: Validaciones, manejo de archivos y operaciones
                                        en general. Todas estas funciones son llamadas desde el menú según lo requiera el usuario.
"""


#FUNCIÓN AUXILIAR - Detectar repetidos
#E: Abre el archivo según el caso de gestión
#S: repetido nos dira si lo que ingreso el usuario ya existe o no
#R: El usuario no puede tener control directo sobre la función, solo su input

def detecta_repetidos(archivo, dato_user):
    with open(archivo, "r") as archivo: 
        linea= archivo.readline()
        repetido= False
        while linea != "" and repetido == False:
            i= 0
            descripcion= ""
            FIN_descripcion= False
            while i < len(linea):
                if linea[i] != ";" and FIN_descripcion == False:
                    descripcion= descripcion + linea[i]
                else:
                    FIN_descripcion= True
                i= i +1
            if dato_user == descripcion:
                repetido= True
            else:
                linea= archivo.readline()
        return repetido

#AGREGAR UNIDADES
#E:
#S:
#R:

def incluir_unidades(archivo):
    archivo_origen= archivo
    print("\nPorfavor ingrese los datos de la unidad de autobús que desea agregar")
    placa= input("Placa de la unidad: ")

    repetido= detecta_repetidos(archivo, placa)
    while repetido == True:
        print("\nEsta placa ya existe, porfavor ingrese otra")
        placa= input("Placa de la unidad: ")
        repetido= detecta_repetidos(archivo, placa)

    save_modelos= []
    with open("modelos.txt", "r") as archivo:
        linea= archivo.readline()
        num= 1
        while linea != "":
            i= 0
            descripcion= ""
            FIN_descripcion= False
            while i < len(linea):
                if linea[i] != ";" and FIN_descripcion == False:
                    descripcion= descripcion + linea[i]
                else:
                    FIN_descripcion= True
                i= i + 1
            print(num,"-", descripcion)
            save_modelos= save_modelos + [descripcion]
            num= num + 1
            linea= archivo.readline()

    modelo= input("Seleccione el modelo: ")
    modelo= int(modelo)
    modelo_selecto= save_modelos[modelo - 1]
    año= input("Año de la unidad: ")
    empresa= input("Empresa Operadora: ")
    incluir= placa + ";" + modelo_selecto + ";" + año + ";" + empresa
    with open(archivo_origen, "a") as archivo:
        archivo.write(incluir + "\n" )
    
    
#MOSTRAR MODELOS
#E: Recibe el archivo de modelos.txt
#S: Muestra todos los modelos actualmente registrados al usuario 
#R: Solo mostrara los modelos que existen

def mostrar_modelos(archivo):
    with open(archivo, "r") as archivo:
        linea= archivo.readline()
        while linea != "":
            i= 0
            campo= 1 #Variable para decicidir en que campo ira el dato mostrado
            descripcion= ""
            marca= ""
            cant_asientos= ""
            cant_de_pie= ""
            while i < len(linea):
                if linea[i] != ";":
                    if campo == 1:
                        descripcion= descripcion + linea[i]
                    if campo == 2:
                        marca= marca + linea[i]
                    if campo == 3:
                        cant_asientos= cant_asientos + linea[i]
                    if campo == 4:
                        cant_de_pie= cant_de_pie + linea[i]
                else:
                    campo= campo + 1
                i= i+1
            cant_total= int(cant_asientos) + int(cant_de_pie)
            print("\n=== DATOS DEL MODELO ===")
            print("Descripción del modelo:", descripcion)
            print("Marca del modelo:", marca)
            print("Cantidad de asientos:", cant_asientos)
            print("Cantidad de espacios a pie:", cant_de_pie.strip())
            print("Capacidad total:", cant_total)
            linea= archivo.readline()


#MODIFICAR MODELOS
#E: Toma el archivo de "modelos.txt"
#S: Retorna el modelo deseado con las nuevas especificaciones
#R: No se puede modificar el modelo (Osea, si es Torino, no puedes cambiar Torino, solo puedes cambiar la marca, los asientos y espacios de pie)
    
def modificar_modelos(archivo):
    archivo_origen= archivo
    print("\nIngrese el modelo que desea modificar")
    modelo= input("Descripción del modelo: ")
    if detecta_repetidos(archivo, modelo) == False:
        print("ERROR: Este modelo no existe porfavor refierase a (4) Mostrar modelos, para ver la lista de modelos registrados")
        menu_admin()
    else:
        new_marca= input("Marca nueva: ")
        new_cant_asientos= input("La nueva cantidad de asientos: ")
        new_cant_de_pie= input("La nueva cantidad de espacios a pie: ")
        nuevos_datos= modelo + ";" + new_marca + ";" + new_cant_asientos + ";" + new_cant_de_pie + "\n"
        with open(archivo, "r") as archivo:
            linea= archivo.readline()
            guardar= ""
            while linea != "":
                i= 0
                descripcion= ""
                FIN_descripcion= False
                while i < len(linea):
                    if linea[i] != ";" and FIN_descripcion == False:
                        descripcion= descripcion + linea[i]
                    else:
                        FIN_descripcion= True
                    i= i + 1
                if descripcion != modelo:
                    guardar= guardar + linea
                else:
                    guardar= guardar + nuevos_datos
                linea= archivo.readline()
        with open(archivo_origen, "w") as archivo:
            archivo.write(guardar)

            
#ELIMINAR MODELOS
#E: Recibe el archivo a analizar y el input de modelo que queremos eliminar 
#S: Se elimina el modelo especificado y queda todo lo demás
#R: Solo puede borrar una opción a la vez

def eliminar_modelo(archivo):
    archivo_origen= archivo
    print("\nIngrese el modelo que desea eliminar")
    modelo= input("Descripción del modelo: ")
    if detecta_repetidos(archivo, modelo) == False:
        print("ERROR: Este modelo no existe porfavor refierase a (4) Mostrar modelos, para ver la lista de modelos registrados")
        menu_admin()
    else:
        with open(archivo, "r") as archivo:
            linea= archivo.readline()
            guardar= ""
            while linea != "":
                i= 0
                descripcion= ""
                FIN_descripcion= False
                while i < len(linea):
                    if linea[i] != ";" and FIN_descripcion == False:
                        descripcion= descripcion + linea[i]
                    else:
                        FIN_descripcion= True
                    i= i + 1
                if descripcion != modelo:
                    guardar= guardar + linea
                linea= archivo.readline()
        with open(archivo_origen, "w") as archivo:
            archivo.write(guardar)

        
#AGREGAR MODELOS
#E: Recibe el archivo a analizar y los inputs que el usuario desea agregar
#S: Si el proceso se realiza de manera satisfactoria, sus datos se agregaran
#R: No pueden existir 2 modelos iguales 

def incluir_modelos(archivo):
    print("\nPorfavor ingrese los datos del modelo de autobús que desea agregar")
    modelo= input("Descripción del modelo: ")
    
    repetido= detecta_repetidos(archivo, modelo)
    while repetido == True:
        print("\nEste modelo que usted ingreso ya existe, porfavor eliga otro")
        modelo= input("Descripción del modelo: ")
        repetido= detecta_repetidos(archivo, modelo)
        
    marca= input("Marca del autobús: ")
    cant_asientos= input("Cantidad de asientos: ")
    cant_de_pie= input("Cantidad de espacios a pie: ")
    incluir=  modelo + ";" + marca + ";" + cant_asientos + ";" + cant_de_pie
    with open(archivo, "a") as archivo:
        archivo.write(incluir + "\n" )
        

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








"""
                                                           ===  SECCIÓN DEL MENU  ===
                                                               
                        Aqui es de donde se trabajan las llamadas de las funciones que trabajan en archviso .txt, asi como
                                controlar y asegurarse de que todos los menús se desplieguen cuando se requieran. 

"""



#MENÚ USUARIOS
#E: Cuando se ingresa 2 en el menú principal
#S: Muestra todas las opciones del menu para usuarios
#R: Se limita a las opciones que se muestran en pantalla

def menu_user():
    while True:
        print("\n=== MENÚ DE USUARIO ===")
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
        print("\n=== MENÚ ADMINISTRATIVO ===")
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
            print("\n=== GESTIÓN DE MODELOS DE AUTOBÚS ===")
            print("(1) Incluir modelo")
            print("(2) Eliminar modelo")
            print("(3) Modificar modelo")
            print("(4) Mostrar modelos")
            print("(5) Volver")

            opcion_gm= input("Elija una opción: ")
            if opcion_gm == "1":
                archivo= "modelos.txt"
                incluir_modelos(archivo)
                print("Se incluyo el modelo de forma exitosa!")
                menu_admin()
                
            if opcion_gm == "2":
                archivo= "modelos.txt"
                eliminar_modelo(archivo)
                print ("Se elimino el modelo de forma exitosa!")
                menu_admin()

            if opcion_gm == "3":
                archivo= "modelos.txt"
                modificar_modelos(archivo)
                print("Se modifico el modelo de forma exitosa!")
                menu_admin()

            if opcion_gm == "4":
                archivo= "modelos.txt"
                mostrar_modelos(archivo)
                menu_admin()

            if opcion_gm == "5":
                menu_admin()
            else:
                print("Esto no es una opción,porfavor escoja un número valido")
                
        if opcion == "12":
            print ("\nGestión de unidades")
            print("(1) Incluir unidad")
            print("(2) Eliminar unidad")
            print("(3) Modificar unidad")
            print("(4) Mostrar unidades")
            print("(5) Volver")

            opcion_gu= input("Elija una opción: ")
            if opcion_gu == "1":
                archivo= "unidades.txt"
                incluir_unidades(archivo)
                print("Se incluyo la unidad de forma exitosa!")
                menu_admin()
                
            if opcion_gu == "2":
                #ARCHIVO "unidades.txt"
                #AQUI VA ELIMINAR UNIDAD
                menu_admin()

            if opcion_gu == "3":
                #ARCHIVO "unidades.txt"
                #AQUI VA MODIFICAR UNIDAD
                menu_admin()

            if opcion_gu == "4":
                #ARCHIVO "unidades.txt"
                #AQUI VA MOSTRAR UNIDADES
                menu_admin()

            if opcion_gu == "5":
                menu_admin()
            else:
                print("Esto no es una opción,porfavor escoja un número valido")

        if opcion == "13":
            print("\nGestión de conductores")
            print("(1)Incluir un conductor")
            print("(2) Eliminar un conductor")
            print("(3) Modificar información de un conductor")
            print("(4) Mostrar a los conductores")
            print("(5) Volver")

            opcion_gc= input("Elija una opción: ")
            if opcion_gc == "1":
                #ARCHIVO "conductores.txt"
                #AQUI VA INCLUIR CONDUCTOR
                menu_admin()
                
            if opcion_gc == "2":
                #ARCHIVO ""conductores.txt"
                #AQUI VA ELIMINAR CONDUCTOR
                menu_admin()

            if opcion_gc == "3":
                #ARCHIVO "conductores.txt"
                #AQUI VA MODIFICAR CONDUCTOR
                menu_admin()

            if opcion_gc == "4":
                #ARCHIVO "conductores.txt"
                #AQUI VA MOSTRAR CONDUCTORES
                menu_admin()
            
            if opcion_gc == "5":
                menu_admin()
            else:
                print("Esto no es una opción,porfavor escoja un número valido")
            
            
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
        print("\n=== MENÚ PRINCIPAL ===")
        print("(1) Opciones Administrativas")
        print("(2) Opciones de Usuario")
        print("(3) Salir")

        opcion= input("Elija una opcion: ")
        if opcion == "1":
            login()
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

