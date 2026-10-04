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

#FUNCIÓN AUXILIAR - Comprobar_asociado
#E: Recibe el archvio a comprobar, el dato que quiere borrar, y el campo en el archivo de destino
#S: Si el dato que quiero borrar, existe en el archivo en el campo indicado que evaluo, significa que esta asociado, no permitira borrarlo
#R: Restringe que pueden y que no pueden eliminar las funciones de eliminar x dato

def comprobar_asociado(archivo, dato, campo):
    with open(archivo, "r") as archivo:
        linea= archivo.readline()
        no_borrar= False
        while linea != "":
            i= 0
            campo_actual= 1
            dato_buscado= ""
            while i < len(linea):
                if linea[i] != ";" and no_borrar == False:
                    if campo_actual == campo:
                        dato_buscado= dato_buscado + linea[i]
                else:
                    campo_actual= campo_actual + 1
                i= i + 1
            if dato_buscado == dato:
                no_borrar= True
            else:
                linea= archivo.readline()
        return no_borrar
                
"""

SECCIÓN DE GESTIÓN DE CONDUCTORES

"""

#MOSTRAR CONDUCTORES
#E: Recibe conductores.txt
#S: Muestra todos los conductores registrados
#R: Solo muestra los datos, no hace ninguna modificación sobre el archivo

def mostrar_conductores(archivo):
    with open(archivo, "r") as archivo:
        linea= archivo.readline()
        while linea != "":
            i= 0
            campo= 1 
            cedula= ""
            nombre= ""
            tipo_licencia= ""
            vence_licencia= ""
            jornada_max= ""
            while i < len(linea):
                if linea[i] != ";":
                    if campo == 1:
                        cedula= cedula + linea[i]
                    if campo == 2:
                        nombre= nombre + linea[i]
                    if campo == 3:
                        tipo_licencia= tipo_licencia + linea[i]
                    if campo == 4:
                        vence_licencia= vence_licencia + linea[i]
                    if campo == 5:
                        jornada_max= jornada_max + linea[i]
                else:
                    campo= campo + 1
                i= i+1
            print("\n=== DATOS DEL CONDUCTOR ===")
            print("Cédula del conductor:", cedula)
            print("Nombre completo del conductor:", nombre )
            print("Tipo de licencia:", tipo_licencia)
            print("Vencimiento de la licencia:", vence_licencia)
            print("Horas máximas de jornada diaria:", jornada_max.strip())
            linea= archivo.readline()


#MODIFICAR CONDUCTORES
#E: Recibe el archvivo de conductores.txt
#S: Modificara la información del conductor cuya cédula haya sido ingresada
#R: La cédula debe de existir antes de modificarla 

def modificar_conductores(archivo):
    archivo_origen= archivo
    print("\nIngrese la cédula del conductor al que le modificara sus datos")
    cedula= input("Cédula del conductor: ")
    if detecta_repetidos(archivo, cedula) == False:
        print("ERROR: Esta cédula no existe porfavor refierase a (4) Mostrar conductores,\npara ver la lista de cédula y conductores válidos")
    else:
        new_nombre= input("Nombre del conductor: ")
        new_tipo_licencia= input("Tipo de licencia: ")
        new_vence_licencia= input("Nueva fecha de vencimiento: ")
        new_jornada_max= input("Actualización a las horas máx de jornada diaria: ")
        nuevos_datos= cedula + ";" + new_nombre + ";" + new_tipo_licencia + ";" + new_vence_licencia + ";" + new_jornada_max + "\n"
        with open(archivo, "r") as archivo:
            linea= archivo.readline()
            guardar= ""
            while linea != "":
                i= 0
                new_cedula= ""
                FIN_cedula= False
                while i < len(linea):
                    if linea[i] != ";" and FIN_cedula == False:
                        new_cedula= new_cedula + linea[i]
                    else:
                        FIN_cedula= True
                    i= i + 1
                if new_cedula != cedula:
                    guardar= guardar + linea
                else:
                    guardar= guardar + nuevos_datos
                linea= archivo.readline()
        with open(archivo_origen, "w") as archivo:
            archivo.write(guardar)
            print("Se ha modificado al conductor correctamente")


#ELIMINAR CONDUCTORES
#E: Recibe el archivo de conductores.txt
#S: La cédula que ingrese el usuario sera eliminada
#R: La cédula debe de existir antes de ser eliminada 

def eliminar_conductores(archivo):
    archivo_origen= archivo
    print("\nIngrese la cédula del conductor que desea eliminar")
    cedula= input("Cédula del conductor: ")
    if detecta_repetidos(archivo, cedula) == False:
        print("ERROR: Esta cédula no existe porfavor refierase a (4) Mostrar conductores,\npara ver la lista de cédula y conductores válidos")
    else:
        with open(archivo, "r") as archivo:
            linea= archivo.readline()
            guardar= ""
            while linea != "":
                i= 0
                del_cedula= ""
                FIN_cedula= False
                while i < len(linea):
                    if linea[i] != ";" and FIN_cedula == False:
                        del_cedula= del_cedula + linea[i]
                    else:
                        FIN_cedula= True
                    i= i + 1
                if del_cedula != cedula:
                    guardar= guardar + linea
                linea= archivo.readline()
        with open(archivo_origen, "w") as archivo:
            archivo.write(guardar)
            print("Se ha eliminado al conductor correctamente!")


#AGREGAR CONDUCTORES
#E: Recibira el archivo de conductores.txt
#S: Va a agregar nuevos conductores a la plantilla 
#R: No pueden existir 2 conductores con la misma cédula 

def agregar_conductores(archivo):
    print("\nPorfavor ingrese los datos del conductor que desea agregar")
    cedula= input("Cédula del conductor: ")
    
    repetido= detecta_repetidos(archivo, cedula)
    while repetido == True:
        print("\nEsta cédula ya esta registrada, porfavor ingrese otra")
        cedula= input("Cédula del conductor: ")
        repetido= detecta_repetidos(archivo, cedula)
        
    nombre= input("Nombre completo del conductor: ")
    tipo_licencia= input("Tipo de licencia: ")
    vence_licencia= input("Vencimiento de la licencia: ")
    jornada_max= input("Horas máximas de jornada diaria: ")
    incluir=  cedula + ";" + nombre + ";" + tipo_licencia + ";" + vence_licencia + ";" + jornada_max
    with open(archivo, "a") as archivo:
        archivo.write(incluir + "\n" )
    
"""

SECCIÓN DE GESTIÓN DE UNIDADES

"""

#MOSTRAR UNIDADES
#E: Recibe el archivo unidades.txt 
#S: Muestra los contenidos a detalle de este archivo
#R: Solo muestra, no causa ningun tipo de edición al archivo 

def mostrar_unidades(archivo):
    with open(archivo, "r") as archivo:
        linea= archivo.readline()
        while linea != "":
            i= 0
            campo= 1
            placa= ""
            modelo= ""
            año= ""
            empresa= ""
            while i < len(linea):
                if linea[i] != ";":
                    if campo == 1:
                        placa= placa + linea[i]
                    if campo == 2:
                        modelo= modelo + linea[i]
                    if campo == 3:
                        año= año + linea[i]
                    if campo == 4:
                        empresa= empresa + linea[i]
                else:
                    campo= campo + 1
                i= i+1
            print("\n=== DATOS DE LA UNIDAD ===")
            print("Placa de la unidad:", placa)
            print("Descripción del modelo:", modelo)
            print("Año de la unidad:", año)
            print("Empresa operadora:", empresa.strip())
            linea= archivo.readline()
    

#MODIFICAR UNIDADES
#E: Recibe el archivo unidades.txt y el input de la placa a cambiar
#S: Modifica la unidad de la que hayamos ingresado la placa
#R: Solo se puede modificar una placa a la vez y solo aquellas que existan

def modificar_unidades(archivo): #CONSTRUIDA CON APOYO DE LA IA
    archivo_origen= archivo
    print("\nIngrese la placa de la unidad que desea modificar: ")
    placa= input("Placa de la unidad: ")
    if detecta_repetidos(archivo, placa) == False:
        print("ERROR: Esta placa no existe porfavor refierase a (4) Mostrar unidades,\npara ver la lista de unidades registradas y su placa")
    else:
        #Bloque para obtener el modelo que deseamos
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

        #Bloque constructor de nuevos datos
        modelo= input("Seleccione el modelo: ")
        modelo= int(modelo)
        modelo_selecto= save_modelos[modelo - 1]
        new_año= input("Año de la unidad: ")
        new_empresa= input("Empresa Operadora: ")
        nuevos_datos= placa + ";" + modelo_selecto + ";" + new_año + ";" + new_empresa + "\n"

        #Bloque para guardar los nuevos datos
        with open(archivo_origen, "r") as archivo:
            linea= archivo.readline()
            guardar= ""
            while linea != "":
                i= 0
                nueva_unidad= ""
                FIN_placa= False
                while i < len(linea):
                    if linea[i] != ";" and FIN_placa == False:
                        nueva_unidad= nueva_unidad + linea[i]
                    else:
                        FIN_placa= True
                    i= i + 1
                if nueva_unidad != placa:
                    guardar= guardar + linea
                else:
                    guardar= guardar + nuevos_datos
                linea= archivo.readline()

        #Guardamos 
        with open(archivo_origen, "w") as archivo:
            archivo.write(guardar)
            print("Se modifico la unidad de forma exitosa!")

        
#ELIMINAR UNIDADES
#E: Recibe el archivo unidades.txt,y el usuario pone en el input lo que quiere eliminar 
#S: Se elimina la placa de la unidad elegida del archivo 
#R: Se debe de eliminar una placa a la vez y solo las que existen se pueden eliminar 

def eliminar_unidades(archivo):
    archivo_origen= archivo
    print("\nIngrese la placa de la unidad que desea eliminar: ")
    placa= input("Placa de la unidad: ")
    if detecta_repetidos(archivo, placa) == False:
        print("ERROR: Esta placa no existe porfavor refierase a (4) Mostrar unidades,\npara ver la lista de unidades registradas y su placa")
    else:
        with open(archivo, "r") as archivo:
            linea= archivo.readline()
            guardar= ""
            while linea != "":
                i= 0
                placa_actual= ""
                FIN_placa= False
                while i < len(linea):
                    if linea[i] != ";" and FIN_placa == False:
                        placa_actual= placa_actual + linea[i]
                    else:
                        FIN_placa= True
                    i= i + 1
                if placa_actual != placa:
                    guardar= guardar + linea
                linea= archivo.readline()
        with open(archivo_origen, "w") as archivo:
            archivo.write(guardar)
            print("Se elimino la unidad de forma exitosa!")

    
#AGREGAR UNIDADES
#E: Recibe el archvio de unidades.txt, dentro de la función se llama a modelos.txt
#S: Guarda los datos solicitados en unidades.txt
#R: Solo se pueden elegir los modelos ya existentes

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
    
"""

SECCIÓN DE GESTIÓN DE MODELOS

"""

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
        print("ERROR: Este modelo no existe porfavor refierase a (4) Mostrar modelos,\npara ver la lista de modelos registrados")
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
            print("Se modifico el modelo de forma exitosa!")

            
#ELIMINAR MODELOS
#E: Recibe el archivo a analizar y el input de modelo que queremos eliminar 
#S: Se elimina el modelo especificado y queda todo lo demás
#R: Solo puede borrar una opción a la vez

def eliminar_modelo(archivo):
    archivo_origen= archivo
    print("\nIngrese el modelo que desea eliminar")
    modelo= input("Descripción del modelo: ")
    if detecta_repetidos(archivo, modelo) == False:
        print("ERROR: Este modelo no existe porfavor refierase a (4) Mostrar modelos,\npara ver la lista de modelos registrados")
    else:
        if comprobar_asociado("unidades.txt", modelo, 2) == True:
            print("ERROR: No se puede eliminar este modelo porque esta asociado a una unidad")
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
                print ("Se elimino el modelo de forma exitosa!")

        
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
            return
        else:
            print("Esto no es una opción,porfavor escoja un número valido")

#MENÚ ADMINISTRATIVO
#E: Cuando se ingresa 1 en el menú principal
#S: Muestra todas las opciones del menu administrativo
#R: Se limita a las opciones que se muestran en pantalla

def menu_admin():
    while True:
        print("\nIMPORTANTE: Las opciones que funcionan son las siguientes:\n(11) Gestión de modelos de autobús\n(12) Gestión de unidades\n(13) Gestión de conductores")
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
                
            elif opcion_gm == "2":
                archivo= "modelos.txt"
                eliminar_modelo(archivo)

            elif opcion_gm == "3":
                archivo= "modelos.txt"
                modificar_modelos(archivo)

            elif opcion_gm == "4":
                archivo= "modelos.txt"
                mostrar_modelos(archivo)

            elif opcion_gm == "5":
                print("Volviendo...")
                
            else:
                print("Esto no es una opción,porfavor escoja un número valido")
                
        elif opcion == "12":
            print ("\n=== GESTIÓN DE UNIDADES ===")
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
                
            elif opcion_gu == "2":
                archivo= "unidades.txt"
                eliminar_unidades(archivo)

            elif opcion_gu == "3":
                archivo= "unidades.txt"
                modificar_unidades(archivo)

            elif opcion_gu == "4":
                archivo= "unidades.txt"
                mostrar_unidades(archivo)

            elif opcion_gu == "5":
                print("Volviendo...")
                
            else:
                print("Esto no es una opción,porfavor escoja un número valido")

        elif opcion == "13":
            print("\n=== GESTIÓN DE CONDUCTORES ===")
            print("(1) Incluir un conductor")
            print("(2) Eliminar un conductor")
            print("(3) Modificar información de un conductor")
            print("(4) Mostrar a los conductores")
            print("(5) Volver")

            opcion_gc= input("Elija una opción: ")
            if opcion_gc == "1":
                archivo= "conductores.txt"
                agregar_conductores(archivo)
                print("Se ha registrado al conductor correctamente!")
                
            elif opcion_gc == "2":
                archivo= "conductores.txt"
                eliminar_conductores(archivo)

            elif opcion_gc == "3":
                archivo= "conductores.txt"
                modificar_conductores(archivo)

            elif opcion_gc == "4":
                archivo= "conductores.txt"
                mostrar_conductores(archivo)
            
            elif opcion_gc == "5":
                print("Volviendo...")
                
            else:
                print("Esto no es una opción,porfavor escoja un número valido")
            
            
        elif opcion == "18":
            print("Volviendo al menú principal")
            return
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
        print("\nAVISO: Como no se terminaron todas las funcionalidades, opciones de usuario\nes un menú vacío.")
        print("\n(1) Opciones Administrativas")
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
            break
        else:
            print("Opción no valida, porfavor escoja uno de los números disponibles")
#Inicializar menú
menu_principal()

