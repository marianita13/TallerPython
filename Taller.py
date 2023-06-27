import os
bandera=True

while (bandera==True):
    os.system('cls')
    ejercicio = int(input("Para acabar con el programa digita 0.\nDigite el número del ejercicio que desea ejecutar (1 al 21): "))
    if (ejercicio==0):
        bandera==False

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

            if (menu==1.1):
                if (len(listaCampersArtemis)==0):
                    print("No hay campers registrados en Artemis")
                else:
                    print(listaCampersArtemis)
                os.system('cls')

            elif (menu==1.2):
                nombreCamper=input("Nombre del Camper: ")
                codigoCamper=input("Codigo del Camper: ")
                listaCampersArtemis.append(nombreCamper)
                os.system('cls')

            elif (menu==1.3):
                eliminar=(input("¿Cual Camper quiere eliminar?: "))

                for a in range(len(listaCampersArtemis)):
                    if (eliminar in listaCampersArtemis):
                        listaCampersArtemis.remove(eliminar)
                os.system('pause')

            elif (menu==1.4):
                listaCampersArtemis.sort()
                print(listaCampersArtemis)

            elif (menu==1.5):
                busqueda=input("Nombre del Camper que desea encontrar:")

    else:
        print("Escoje un número del 1 al 21")