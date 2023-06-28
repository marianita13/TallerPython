import os
bandera=True

while (bandera==True):
    os.system('cls')
    ejercicio = int(input("Para acabar con el programa digita 0.\nDigite el número del ejercicio que desea ejecutar (1 al 21): "))
    if (ejercicio==0):
        bandera=False

    elif (ejercicio==1):
        edad = int(input("Digite su edad por favor: "))

        if (edad<18):
            print("Eres menor de edad")
        elif (edad>=18):
            print("Eres mayor de edad")
        os.system('pause')
        ejercicio=0

    elif (ejercicio==2):
        numero = int(input("Digite un número entero positivo: "))
        contador = numero

        while (contador!=0):
            print(contador)
            contador-=1
        os.system('pause')
        ejercicio=0

    elif (ejercicio==3):
        numero2=int(input("Digite un número entero: "))

        if (numero2>0):
            print("El número es positivo")
        elif (numero2==0):
            print("El numero es 0")
        elif (numero2<=0):
            print("El número es negativo")
        os.system('pause')
        ejercicio=0

    elif (ejercicio==4):
        numero3= int(input("Digita un número: "))

        if ((numero3%2)==0):
            print("El número es par")
        os.system('pause')
        ejercicio=0

    elif (ejercicio==5):
        contraseña = input("Digite su contraseña: ")
        contador = 0
        contadorNumeros = 0

        for i,item in enumerate(contraseña):
            contador+=1
            if ((item=='0') or (item=="1") or (item=="2") or (item=="3") or (item=="4") or (item=="5") or (item=="6") or (item=="7") or (item=="8") or (item=="9")):
                contadorNumeros+=1
                contador+=1
        print(contador, contadorNumeros)
        if (contador>=8 and contadorNumeros>=1):
            print("Contraseña válida")
        else:
            print("Contraseña invalida")
        os.system('pause')
        ejercicio=0

    elif (ejercicio==6):
        examen=int(input("Digite su calificación: "))

        if (examen>=60):
            print("Haz aprobado")
        else:
            print("Haz reprobado")
        os.system('pause')
        ejercicio=0

    elif (ejercicio==7):
        contraseña2="secreto123"
        contra = input("Digite su contraseña: ")

        if (contra!=contraseña2):
            print("Acceso Denegado")
        else:
            print("Acceso concedido")
        os.system('pause')
        ejercicio=0

    elif (ejercicio==8):
        pais = input("Ingrese un país: ")
        europa = ["alemania", "austria", "portugal", "dinamarca", "francia", "italia"]
        asia = ["afganistan", "catar", "filipinas", "corea del sur", "irak", "yemen"]
        america = ["colombia", "argentina", "brazil", "canada", "estados unidos"]
        oceania = ["australia", "fiyi", "nueva zelanda", "palaos"]
        africa = ["angola", "nigeria", "senegal", "somalia", "uganda"]

        if (pais.lower() in europa):
            print("Continente: Europa")
        elif (pais.lower() in asia):
            print("Continente: Asia")
        elif (pais.lower() in america):
            print("Continente: America")
        elif (pais.lower() in oceania):
            print("Continente: de Oceanía")
        elif (pais.lower() in africa):
            print("Continente: Africa")
        os.system('pause')
        ejercicio=0

    elif (ejercicio==9):
        day = int(input("Digita el día: "))
        month = int(input("Digita el mes (en numeros): "))
        year = int(input("Digita el año: "))

        if ((year%4)==0):
            if (month==2):
                if (day>=1 and day<=29):
                    print("Fecha valida")
                else:
                    print("Fecha invalida")
            else:
                pass
        else:
            if (month==1):
                if (day>=1 and day<=31):
                    print("Fecha valida")
                else:
                    print("Fecha invalida")
            if (month==2):
                if (day>=1 and day<=28):
                    print("Fecha valida")
                else:
                    print("Fecha invalida")
            if (month==3):
                if (day>=1 and day<=31):
                    print("Fecha valida")
                else:
                    print("Fecha invalida")
            if (month==4):
                if (day>=1 and day<=30):
                    print("Fecha valida")
                else:
                    print("Fecha invalida")
            if (month==5):
                if (day>=1 and day<=31):
                    print("Fecha valida")
                else:
                    print("Fecha invalida")
            if (month==6):
                if (day>=1 and day<=30):
                    print("Fecha valida")
                else:
                    print("Fecha invalida")
            if (month==7):
                if (day>=1 and day<=31):
                    print("Fecha valida")
                else:
                    print("Fecha invalida")
            if (month==8):
                if (day>=1 and day<=31):
                    print("Fecha valida")
                else:
                    print("Fecha invalida")
            if (month==9):
                if (day>=1 and day<=30):
                    print("Fecha valida")
                else:
                    print("Fecha invalida")
            if (month==10):
                if (day>=1 and day<=31):
                    print("Fecha valida")
                else:
                    print("Fecha invalida")
            if (month==11):
                if (day>=1 and day<=30):
                    print("Fecha valida")
                else:
                    print("Fecha invalida")
            if (month==12):
                if (day>=1 and day<=31):
                    print("Fecha valida")
                else:
                    print("Fecha invalida")
            elif(month>12 or month<=0):
                print("Fecha invalida")
        os.system('pause')
        ejercicio=0

    elif (ejercicio==10):
        longitud1=int(input("Digita el primer valor: "))
        longitud2=int(input("Digita el segundo valor: "))
        longitud3=int(input("Digita el tercer valor: "))

        if ((longitud1==longitud2) and (longitud2==longitud3)):
            print("Si se puede formar un triangulo")
        elif ((longitud1==0) or (longitud2==0) or (longitud3==0)):
            print("No se puede formar un triangulo")
        elif ((longitud1+longitud2)>longitud3):
            print("Si se puede formar un triangulo")
        elif ((longitud1+longitud3)>longitud2):
            print("Si se puede formar un triangulo")
        elif ((longitud2+longitud3)>longitud1):
            print("Si se puede formar un triangulo")
        else:
            print("No se puede formar un triangulo")
        os.system('pause')
        ejercicio=0

    elif (ejercicio==11):
        mes=(input("Digita el mes: "))

        if ((mes.lower()=="enero") or (mes.lower()=="marzo") or (mes.lower()=="mayo") or (mes.lower()=="julio") or (mes.lower()=="agosto") or (mes.lower()=="octubre") or (mes.lower()=="diciembre")):
            print("Este mes tiene 31 dias")
        elif ((mes.lower()=="abril") or (mes.lower()=="junio") or (mes.lower()=="septiembre") or (mes.lower()=="noviembre")):
            print("Este mes tiene 30 dias")
        elif (mes.lower()=="febrero"):
            print("Este mes solo tiene 28 dias")
        os.system('pause')
        ejercicio=0
    
    elif (ejercicio==12):
        palabra = input("Digite una palabra: ")
        for i in range(len(palabra)):
            print(palabra[i], end='\n')
        os.system('pause')
        ejercicio=0

    elif (ejercicio==13):
        numero4=int(input('Digite un numero: '))

        for i in range(1,11):
            resultado=numero4*i
            print(f'{numero4}x{i} = {resultado}')
        os.system('pause')
        ejercicio=0

    elif (ejercicio==14):
        numeros=[]
        numbers=0
        while (len(numeros)!=50):
            numbers+=1
            if (numbers%2==0):
                numeros.append(numbers)
            else:
                pass
        print(f'Los primeros 50 numeros pares son: {numeros}')
        os.system('pause')
        ejercicio=0

    elif (ejercicio==15):
        frase=input('Digita una frase: ')
        contador2=0

        for i,item in enumerate(frase):
            if (item=='a'):
                contador2 +=1
            else:
                pass
        print(f"La letra 'a' aparece {contador2} veces")
        os.system('pause')
        ejercicio=0

    elif (ejercicio==16):
        sumatoria=0
        numero5=int(input("Digite un numero positivo: "))
        sumatoria+=numero5
        contador3=1

        while(numero5>0):
            numero5=int(input("Digite un numero positivo: "))
            if (numero5>0):
                sumatoria+=numero5
                contador3+=1
            else:
                pass
            print(sumatoria, contador3)
        print(f"El promedio de los numeros ingresados es: {sumatoria/contador3}")
        os.system('pause')
        ejercicio=0

    elif (ejercicio==17):

        sumaDigito = 0
        extNum = 0
        numero6 = int(input("Ingrese un numero entero: "))
        while numero6 != 0:
            extNum = numero6 % 10
            numero6 //= 10
            sumaDigito += extNum
        print("La suma de los digitos es: ",(sumaDigito))
        os.system('pause')
        ejercicio=0

    elif (ejercicio==18):
        isAddStudent=True

        while (isAddStudent==True):
            nombreEmpleado=input("Digite el nombre del empleado: ")
            telefonoEmpleado=input("Digite el telefono del empleado: ")
            apellidosEmpleado=input("Digita los apellidos del empleado: ")
            yearDeIngreso=int(input("Digite el año de ingreso a la empresa: "))
            edadEmpleado=input("Digite la edad del empleado: ")
            isAddStudent=False

        print(f'El empleado {nombreEmpleado} {apellidosEmpleado} lleva {2023-yearDeIngreso} de antiguedad')
        os.system('pause')
        ejercicio=0

    elif (ejercicio==19):
        mesDeConsumo=input("Digite el mes de consumo electrico: ")
        valorKW=int(input("Digite el valor por kilovatio: "))
        totalKW=(int(input("Digite el total de kilovatios consumidos en el mes: ")))
        estrato=int(input("Digite su estrato: "))
        precioTotal=valorKW*totalKW

        print(f'El precio total de la energia electrica del mes de {mesDeConsumo} de estrato {estrato} es de {precioTotal}')
        os.system('pause')
        ejercicio=0

    elif (ejercicio==20):
        menu=0
        listaCampersArtemis=[]
        listaCampersSputnik=[]
        codigosCampers=[]
        while (menu!=3):
            menu=float(input('''1.CREAR GRUPO ARTEMIS:
1.1 Listar campers de Artemis
1.2 Agregar campers de Artemis
1.3 Eliminar campers de Artemis
1.4 Ordenar alfabeticamente en la lista de Artemis
1.5 Buscar camper en la lista de Artemis

2. CREAR GRUPO SPUTNIK:
2.1 Listar campers de Sputnik
2.2 Agregar campers de Sputnik
2.3 Eliminar campers de Sputnik
2.4 Ordenar alfabeticamente en la lista de Sputnik
2.5 Buscar camper en la lista de Sputnik

3. Salir
:'''))
            
            match menu:       
                case 1.1:
                    os.system('clear')
                    if (len(listaCampersArtemis)==0):
                        print("No hay campers registrados en Artemis")
                    else:
                        for numero,nombre in enumerate(listaCampersArtemis,1):
                            print(numero,nombre)
                        print("")
                case 1.2:
                    os.system('clear')
                    nombreCamper=input("Nombre del Camper: ")
                    listaCampersArtemis.append(nombreCamper)
                    for numero,nombre in enumerate(listaCampersArtemis,1):
                        print(numero,nombre)
                    print("")                 
                case 1.3:
                    os.system('clear')
                    eliminar=(input("¿Cual Camper quiere eliminar?: ")).lower()

                    for a in range(len(listaCampersArtemis)):
                        if (eliminar in listaCampersArtemis):
                            listaCampersArtemis.remove(eliminar)
                    for numero,nombre in enumerate(listaCampersArtemis,1):
                        print(numero,nombre)
                    print("")
                case 1.4:
                    os.system('clear')
                    listaCampersArtemis.sort()
                    for numero,nombre in enumerate(listaCampersArtemis,1):
                        print(numero,nombre)
                    print("")
                        
                case 1.5:
                    os.system('clear')
                    busqueda=input("Nombre del Camper que desea encontrar:").lower()
                    for z in range(len(listaCampersArtemis)):
                        if (busqueda in listaCampersArtemis):
                            print(f'{busqueda} si se encuentra en el grupo.')
                            break
                    print("")
                    
                case 2.1:
                    os.system('clear')
                    if (len(listaCampersSputnik)==0):
                        print("No hay campers registrados en Sputnik")
                    else:
                        for numero2,nombre2 in enumerate(listaCampersSputnik,1):
                            print(numero2,nombre2)
                        print("")
                case 2.2:
                    os.system('clear')
                    nombreCamper2=input("Nombre del Camper: ")
                    listaCampersSputnik.append(nombreCamper2)
                    for numero2,nombre2 in enumerate(listaCampersSputnik,1):
                        print(numero2,nombre2)
                    print("")                 
                case 2.3:
                    os.system('clear')
                    eliminar=(input("¿Cual Camper quiere eliminar?: ")).lower()

                    for a in range(len(listaCampersSputnik)):
                        if (eliminar in listaCampersSputnik):
                            listaCampersSputnik.remove(eliminar)
                    for numero2,nombre2 in enumerate(listaCampersSputnik,1):
                        print(numero2,nombre2)
                    print("")
                case 2.4:
                    os.system('clear')
                    listaCampersSputnik.sort()
                    for numero2,nombre2 in enumerate(listaCampersSputnik,1):
                        print(numero2,nombre2)
                    print("")
                        
                case 2.5:
                    os.system('clear')
                    busqueda=input("Nombre del Camper que desea encontrar:").lower()
                    for z in range(len(listaCampersSputnik)):
                        if (busqueda in listaCampersSputnik):
                            print(f'{busqueda} si se encuentra en el grupo.')
                            break
                    print("")
                
                case 3:
                    os.system('clear')
                    print("Gracias por usar nuestros servicios.")
                    break
        ejercicio=0
        
    elif (ejercicio==21):
        cali=[]
        medellin=[]
        bucaramanga=[]
        bogota=[]
        opciones = 0
        while(opciones!=8):
            os.system('clear')
            opciones = int(input('''1.Registro de Equipo.
2. Registro de fecha.
3. Mostrar tabla de estadisticas.
4. Consultar informacion por equipo.
5. Mostrar equipos clasificados a 8vos.
6. Mostrar el listado de jugadores de un equipo.
7. Equipo que mayor cantidad de goles marco por cada grupo.
8. Salir.
Digita una opción: '''))
        
            match opciones:
                case 1:
                    os.system('clear')
                    equipo = 0
                    while (equipo!=1.4):
                        os.system('clear')
                        equipo = float(input("1.1 Registro de jugadores.\n1.2 Registro de cuerpo técnico.\n1.3 Registro de cuerpo medico.\n1.4 Salir\nElije una opción: "))
                        if (equipo==1.1):
                            os.system('clear')
                            nombreEquipo=input("Digite el nombre del equipo: ")
                            banderaG=True
                            while (banderaG==True):
                                grupoEquipo=int(input("1. Cali\n2. Bucaramanga\n3. Medellin\n4. Bogota\nA que grupo pertenece: "))
                                if (grupoEquipo==1):
                                    grupoEquipo="Cali"
                                    banderaG=False
                                elif (grupoEquipo==2):
                                    grupoEquipo="Bucaramanga"
                                    banderaG=False
                                elif (grupoEquipo==3):
                                    grupoEquipo="Medellin"
                                    banderaG=False
                                elif (grupoEquipo==4):
                                    grupoEquipo="Bogota"
                                    banderaG=False
                                else:
                                    print("Digita una opcion del menu")
                            nombreJugador=input("Digite el nombre del jugador: ")
                            nroDorsal=int(input("Digite el numero del dorsal del jugador: "))
                            os.system('clear')
                            banderaP=True
                            while(banderaP==True):
                                posicion=int(input("1. Arquero\n2. Delantero\n3. Mediocampista\n4. Defensa\nDigite la posicion del jugador: "))
                                if (posicion==1):
                                    posicion="Arquero"
                                    banderaP=False
                                elif (posicion==2):
                                    posicion="Delantero"
                                    banderaP=False
                                elif (posicion==3):
                                    posicion="Mediocampista"
                                    banderaP=False
                                elif (posicion==4):
                                    posicion="Defensa"
                                    banderaP=False
                                else:
                                    print("Digita una opcion del menu")
                            edad=int(input("Digite la edad del jugador: "))
                            listaEquipo=[nombreJugador,nroDorsal,posicion,edad]
                                
                            if (grupoEquipo=="cali"):
                                for i,paises in enumerate(cali):
                                    if (nombreEquipo in paises):
                                        print("Este pais ya esta inscrito")
                                        break
                                    else:
                                        cali.append([nombreEquipo])
                                    print(cali)
                                    cali[i].append(listaEquipo)
                                    input()
                                    print('')
                                else:
                                    print("Solo se pueden registrar 4 equipos por grupo")
                            elif (grupoEquipo=="bucaramanga"):
                                if (len(bucaramanga)<4):
                                    bucaramanga.append([nombreEquipo])
                                    bucaramanga.append(listaEquipo)
                                else:
                                    print("Solo se pueden registrar 4 equipos por grupo")
                            elif (grupoEquipo=="medellin"):
                                if (len(medellin)<4):
                                    medellin.append([nombreEquipo])
                                    medellin.append(listaEquipo)
                                else:
                                    print("Solo se pueden registrar 4 equipos por grupo")
                            elif (grupoEquipo=="bogota"):
                                if (len(bogota)<4):
                                    bogota.append([nombreEquipo])
                                    bogota.append(listaEquipo)
                                else:
                                    print("Solo se pueden registrar 4 equipos por grupo")
                        elif (equipo==1.2):
                            os.system('clear')
                            nombreEquipo=input("Digite el nombre del equipo: ")
                            grupoEquipo=input("A que grupo pertenece: ")
                            nombreTecnico=input("Digite el nombre del cuerpo tecnico: ")
                            cargoTecnico=input("Digite el cargo del cuerpo tecnico: ")
                            edadTecnico=int(input("Digite la edad del cuerpo tecnico: "))
                            listaTecnicos=[nombreTecnico,cargoTecnico,edadTecnico]

                            if (grupoEquipo=="cali"):
                                for i,equipo3 in enumerate(cali):
                                    if (grupoEquipo in equipo3):
                                        cali[i].append(listaTecnicos)
                                print(cali)
                                input()
                                print('')

                        elif (equipo==1.3):
                            pass
            ejercicio=0
    else:
        print("Escoje un número del 1 al 21")