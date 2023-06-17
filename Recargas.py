import os #SIRVE PARA USAR EL "os.system("cls")" QUE ES PARA LIMPIAR PANTRALLA
recargas = [[],[],[],[]] #EN ESTE ARREGLO VACÍO SE ALMACENARAN LOS MONTOS REGISTRADOS DE CADA COMPAÑIA+

#TUPLA(ARREGLO QUE NO SE PUEDE MODIFICAR) DEL MENÚ PRINCIPAL
menuPrincipal = ("1.- Recarga","2.- Reporte de recargas", "3.- Salir")

#TUPLA(ARREGLO QUE NO SE PUEDE MODIFICAR) DE LAS COMPAÑIASDISPONIBLE
companias = ("1.- Telcel", "2.- Movistar", "3.- Unefon", "4.- AT&T")

#TUPLA(ARREGLO QUE NO SE PUEDE MODIFICAR) DE LOS MONTOS DISPONIBLES
montos = (10, 20, 50, 100, 150, 200, 500)



def mostrar_menu(menus): #definimos(def) la función para imprimir cada una de las opciones del menú principal y colocamos un parametro (arreglo)
    for opcion in menus:#Para "opcion" en el parametro (menuPrincipal) es decir opcion va tomar cada uno de los parametros de "menuPrincipal"
        print (opcion) #Y por último se imprime cada uno de los parametros que tomó "opcion"


def validar(mensaje):#definimos(def) la función para validar el "mensaje"(parametro) de entrada para elegir opcion del menú principal
    bandera = True #Variable de control para tomar una desición o tambien es como un parámetro la iniciamos en "True"
    while bandera: #Mientras la bandera sea "True" hacer:
        try:#Intenta hacer:
            valor = int(input(mensaje)) #Se lee el "mensaje" de entrada que sea de tipo entero
            bandera = False #Si el dato ingresado es entero la variable de control se rompe y no se vuelve a repetir que nos pida otra opción
        except:#Si no se ingreso un entero se muestra el siguiente mensaje con "print("")"
            print ("\nSolamente se admiten números enteros".center(50," "))
    return valor #Con "return" retornamos o regresamos a la asignación de valor, es decir para que se le vuelva a dar lectura a la opción deseada del menú principal


def registrar_recarga():
    print ("\nCompañias\n")

    #Se ejecuta la misma operación de la función "mostrar_menu" pero se invoca a la TUPLA "companias" y pues se imprime cada parametro
    mostrar_menu(companias)

    compania = validar("\nElija una compañia (1 a 4): ")
    if compania > 0 and compania < 5:
        print ("\nMontos\n")
        mostrar_menu(montos)
        monto = validar("\nIndique el monto de la recarga: ")
        if monto in montos:
            #Aquí "compania" es el índice inidicado donde se almacena el "monto" pero debemos de restarle un índice para
            #que se almacene en la primera posición del arreglo ya que en los arreglos se comienza desde "0"
            recargas[compania - 1].append(monto) #".append" agrega el "monto" al arreglo "recargas"
            print ("Recarga registrada")
        else:
            print ("\nEl monto ingresado no esta en la lista, ponga uno que este en la lista no sea imbecil")
    else:
        print ("\nOpción no válida")


def mostrar_recargas():
    print ("\nRecargas realizadas")
    #"compania" es el índice del arreglo "recargas"
    for compania in range (0,4):
        print ("\n",companias[compania])
        for recarga in recargas[compania]:
            print (recarga)
        print ("Total: ", sum(recargas[compania]))



eleccion = 1
while eleccion != 3:
    os.system("cls")
    print ("Centro de recargas Ultra".center(20," "))
    mostrar_menu(menuPrincipal)
    eleccion = validar("\nElija una opción (1 a 3): ")
    os.system("cls")


    if eleccion == 1:
        registrar_recarga()


    elif eleccion == 2:
        mostrar_recargas()


    elif eleccion == 3:
        print ("\nHasta luego...")
    else:
        print ("Elija una opción válida (1 a 3)")
    input("\nPresione ENTER para continuar")
