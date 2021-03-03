# Integrantes de la elaboracion del proyecto (grupo 2): Sofia Carvajal y Gabriela Ortega.

def pedir_notas():
    global notas
    notas = []
    for i in range(10):
        a = float(input(" Ingrese nota" + str(i + 1) + ":"))
        notas.append(a)
    return notas


def pedir_datos():

    lista = []
    tam = int(input("Ingrese la cantidad de estudiantes que va a inscribir: "))
    for i in range(tam):
        sublista = []
        nombre = input("\nIngrese el nombre del estudiante: ")
        carrera = input("\nIngrese la carrera a la que pertenece el estudiante (en minusculas y nombre completo de la carrera): ")
        semestre = int(input("\nIngrese el numero de semestre que esta cursando el estudiante: "))
        evaluacion = int(input("\nSi tiene desempeño excelente digite 3, si tiene desempeño regular digite  2, si tiene desempeño malo digite el 1: "))
        amonestacion = int(input("\nSi ha ido amonestado digite el 4, si NO ha sido amonestado digite el 5: "))
        promedio = float(input("\nDigite el promedio actual del estudiante: "))
        sublista.append(nombre)
        sublista.append(carrera)
        sublista.append(semestre)
        sublista.append(evaluacion)
        sublista.append(amonestacion)
        sublista.append(promedio)
        sublista.append(pedir_notas())
        lista.append(sublista)
        print("\nLa información del estudiante es: ")
        imprimir(sublista)
        print(" ")
        print("\nLas notas de las aignaturas son:", notas)

    return lista

def imprimir(sublista):

    for i in range(len(sublista) - 1):
        if i == len(sublista) - 2:
            print(sublista[i], end=".")
        else:
            print(sublista[i], end=",")


def cupos():

    global ingenieria, eco_ad, matematicas,escogidos
    for i in range(len(escogidos)):
        if escogidos[i][1] == "ingenieria civil" or escogidos[i][1] == "ingenieria electrica" or escogidos[i][
            1] == "ingenieria mecamica" or escogidos[i][1] == "ingenieria de sistemas" or escogidos[i][
            1] == "ingenieria electronica" or escogidos[i][1] == "ingenieria ambiental" or escogidos[i][1] == "ingenieria industrial":
            ingenieria = ingenieria + 1
        elif escogidos[i][1] == "economia" or escogidos[i][1] == "administracion":
            eco_ad = eco_ad + 1
        elif escogidos[i][1] == "matematicas":
            matematicas = matematicas + 1
    

def escoger_grupo_rector(datos):
    global escogidos, ingenieria, eco_ad, matematicas
    preseleccionados = []
    escogidos = []
    ingenieria = 0
    eco_ad = 0
    matematicas = 0
    cont = 0
    print("Los posibles candidatos son: \n")
    for i in range(len(datos)):
        print(datos[i][0])
        if datos[i][5] >= 4.5 and datos[i][4] == 5 and datos[i][3] == 3 and min(datos[i][6]) >= 3.0:
            escogidos.append(datos[i])
            preseleccionados.append(datos[i][0])
            #print(escogidos)
            cont = cont + 1
    #print(cont)
    #print(escogidos)
    if cont > 0:
        print("\nSe han preleccionado ", cont, " estudiantes: \n")
        for i in range(len(preseleccionados)):
            if i == len(preseleccionados) - 1:
                print(preseleccionados[i], end=".")
            else:
                print(preseleccionados[i], end=", ")
        print(" ")

    else:
        print("\nNo se encontraron estudiantes que cumplan las condiciones\n")
    cupos()

def desempate():
    global finales,escogidos,l_finales
    finales = []
    l_finales = []
    contador = 0
    print("*" * 150)
    print("Esta opcion le permitira desempatar si el numero de cupos es superior a 4")
    print("O la cantidad permitida de cada area\n")
    #print(escogidos)
    if len(escogidos) != 0:
        promedios = []
        for i in range(len(escogidos)):
            lnotas = escogidos[i][6]
            promedio = sacar_promedio(lnotas)
            promedios.append(promedio)
            escogidos[i].append(promedio)
            #print(promedios)
            promedios.sort(reverse=True)
            #print(promedios)

        for i in range(len(promedios)):
            if contador < 4:
                finales.append(promedios[i])
                contador += 1
            else:
                pass
        #print(finales)
        print("El desempate debido a los mejores promedios deja como acompañantes a: ")
        for j in range(len(finales)):
            for i in range(len(escogidos)):
                if escogidos[i][7] == finales[j]:
                    print(escogidos[i][0], end=" / ")
                    print(" ")
                    l_finales.append(escogidos[i])
        #print(l_finales)

    else:
        print("No se puede realizar desempate porque no hay estudiantes escogidos")

def sacar_promedio(lnotas):
    sum = 0.0
    for i in range(len(lnotas)):
        sum = sum + lnotas[i]
    prom = sum / 10
    return prom

def Estudiante_lider():

    global l_finales
    print("*"*150)
    print("\nEl estudiante lider se eligira entre: \n")
    print(l_finales)
    print("\nDe forma que por mejor desempeño y promedio el programa ha elegido a: \n")
    print(l_finales[0][0], "estudiante de ", l_finales[0][1], "con promedio de", l_finales[0][5],"Como la lider del grupo de estudiantes")


def menu():
    print("Selecciona una opcion")
    print("\t1 - Ingresar datos")
    print("\t2 - Grupo del rector")
    print("\t3 - Desempate")
    print("\t4 - Estudiante lider ")
    print("\t5 - Salir")

    opcion = input("Escoge una opcion >> ")
    return opcion


def main():
    global datos
    cadena = "Bienvenidos al grupo del rector de la Escuela Colombiana De Ingeneria".capitalize()
    print(cadena.center(50, "="))
    salir = False

    while not salir:
        opcionMenu = menu()

        if opcionMenu == "1":

            input("Pulsa una tecla para continuar\n")
            datos = pedir_datos()

        elif opcionMenu == "2":
            escoger_grupo_rector(datos)

        elif opcionMenu == "3":
            desempate()

        elif opcionMenu == "4":
            Estudiante_lider()

        elif opcionMenu == "5":
            salir = True

        else:
            print("")
            input("No has pulsado ninguna opcion correcta...\npulsa una tecla para continuar")

    print("----------Gracias por participar----------")


main()
