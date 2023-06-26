ejercicio = int(input("Digite el número del ejercicio que desea ejecutar (1 al 21): "))

while (ejercicio!=0):
    if (ejercicio==1):
        edad = int(input("Digite su edad por favor: "))

        if (edad<18):
            print("Eres menor de edad")
        elif (edad>=18):
            print("Eres mayor de edad")
        ejercicio=0

    elif (ejercicio==2):
        numero = int(input("Digite un número entero positivo: "))
        contador = numero

        while (contador!=0):
            print(contador)
            contador-=1
        ejercicio=0

    elif (ejercicio==3):
        numero2=int(input("Digite un número entero: "))

        if (numero2>0):
            print("El número es positivo")
        elif (numero2==0):
            print("El numero es 0")
        elif (numero2<=0):
            print("El número es negativo")
        ejercicio=0

    elif (ejercicio==4):
        numero3= int(input("Digita un número: "))

        if ((numero3%2)==0):
            print("El número es par")
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
        ejercicio=0

    elif (ejercicio==6):
        examen=int(input("Digite su calificación: "))

        if (examen>=60):
            print("Haz aprobado")
        else:
            print("Haz reprobado")
        ejercicio=0

    elif (ejercicio==7):
        contraseña2="secreto123"
        contra = input("Digite su contraseña: ")

        if (contra!=contraseña2):
            print("Acceso Denegado")
        else:
            print("Acceso concedido")
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
        ejercicio=0

    elif (ejercicio==11):
        mes=int(input("Digita el mes: "))

    else:
        print("Escoje un número del 1 al 21")