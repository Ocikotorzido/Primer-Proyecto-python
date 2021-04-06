import string
import os
os.system("cls")

def rutinvalido():
    print("rut invalido")  
    
#variables
busqueda2=0
rea=0
reb=0
rec=0
red=0
ta=0
valorA=0
valorB=0
valorC=0
valorD=0
totalA=0
totalB=0
totalC=0
totalD=0
ad=0
af=0
ag=0
ah=0
aj=0
ak=0
al=0
an=0
ab=0
persona=[]
o=0
s=0
d=0
p=0
per=0
depa =[ ["     ", "A ", "B", "C", "D",], #Creación: Se le asigna un nombre a la matriz y luego se abren corchetes '[]'
        ["piso1", " ", " ", " ", " ",], #Dentro de los primeros corchetes deben llenar con 2 o mas listas internas
        ["piso2", " ", " ", " ", " ",], #o para que sea considerada una matriz.
        ["piso3",  " ", " ", " ", " ",],
        ["piso4", " ", " ", " ", " ",],
        ["piso5",  " ", " ", " ", " ",],
        ["piso6",  " ", " ", " ", " ",],
        ["piso7",  " ", " ", " ", " ",],
        ["piso8", " ", " ", " ", " ",],
        ["piso9",  " ", " ", " ", " ",],
        ["piso10",  " ", " ", " ", " ",]
        
        ]
def letras():
    print ("\nHabitacion: A = 1 ")  #Las filas y columnas que estarían asignadas a '0' las llené con letras y números para que sea mas
    print ("            B = 2")    #fácil el guiarse dentro de la matriz.
    print ("            C = 3")
    print ("            D = 4")
    
    print ("Por favor, escribir con la asignación numérica.")
var=0

i=0
while True:
    os.system("cls")
    m=("Menu de opciones",
        "1) Comprar departamentos",
        "2) Mostrar departamentos disponibles",
        "3) Ver listado de compradores",
        "4) Reasignar compra",
        "5) Ganancias totales",
        "6) Salir")
    for menu in m:
        print(menu)        
    respuesta=int(input("elija opcion: "))

    while respuesta<1 or respuesta>6:
        print("opcion no valida")
        respuesta=int(input())

    if respuesta==1:
        while True:
            per=per+1
            os.system("cls")
            n=("Los precios de los departamentos son los siguientes","Tipo A 3800 UF","Tipo B 3000 UF","Tipo C 2800 UF","Tipo D 3500 UF")
            for a in n:
                print(a)

            print("------------------------------------------------------------")
            print("a partir del piso 3 el valor de las habitaciones aumenta en 100 UF por piso")
            print("------------------------------------------------------------")

            dicpersona={"rut":0,"nombre":"","edad":0,"piso":0,"tipo":0}
            print("----------------------")
            while True:
                try:
                    rut=int(input("ingrese rut sin guion ni puntos: "))
                    break
                except ValueError:
                    print("ingrese un rut valido")
            print("----------------------")
            nombre=input("ingrese nombre: ")
            print("----------------------")
            while True:
                try:
                    edad=int(input("ingrese edad: "))
                    break
                except ValueError:
                    print("ingrese una edad valida")
            print("----------------------")
            
            dicpersona["rut"]=rut
            dicpersona["nombre"]=nombre
            dicpersona["edad"]=edad

            for matriz in (depa): 
                print (matriz)
            print("----------------------")
            while True:
                try:
                    piso=int(input("Ingrese piso: "))
                    while piso<1 and piso>10:
                        piso=int(input("Error. Ingrese piso valido : "))
                    break
                except ValueError:
                    print("ingrese un piso valido")
            letras()
            print("----------------------")
            while True:
                try:
                    tipo=int(input("Ingrese un tipo de departamento: "))
                    while tipo<1 and tipo>4:
                        tipo=int(input("Error. Ingrese un tipo de departamento valido: "))
                    break
                except ValueError:
                    print("ingrese un tipo valido")
                print("----------------------")
            while depa[piso][tipo]=="xx":
                print("----------------------")
                print("Departamento ya comprado. Eliga otro porfavor")
                while True:
                    try:
                        piso=int(input("Ingrese piso: "))
                        while piso<1 and piso>10:
                            piso=int(input("Error. Ingrese piso valido : "))
                        break
                    except ValueError:
                        print("ingrese un piso valido")
                    letras()
                print("----------------------")
                while True:
                    try:
                        tipo=int(input("Ingrese un tipo de departamento: "))
                        while tipo<1 and tipo>4:                            
                            tipo=int(input("Error. Ingrese un tipo de departamento valido: "))
                        break
                    except ValueError:
                        print("ingrese un tipo valido")
                        print("----------------------")

            if tipo==1:
                p=p+1
            if tipo==2:
                o=o+1
            if tipo==3:
                s=s+1
            if tipo==4:
                d=d+1    
            c="xx"

            if piso==1 or piso==2:
                ad=ad+1
                
                print("piso",piso,"tipo habitacion",tipo)
                if tipo==1:
                    valorA=3800
                    ta=3800
                    totalA=p*valorA
                    rea=rea+0
                if tipo==2:
                    valorB=3000
                    ta=3000
                    totalB=o*valorB
                    reb=reb+0
                if tipo==3:
                    valorC=2800
                    ta=2800
                    totalC=s*valorC
                    rec=rec+0
                if tipo==4:
                    valorD=3500
                    ta=3500
                    totalD=d*valorD
                    red=red+0
                
                
            if piso==3:
                af=af+1
                print("piso",piso,"tipo habitacion",tipo)
                if tipo==1:
                    valorA=3800
                    ta=3800+100
                    totalA=p*valorA
                    
                    rea=rea+100
                if tipo==2:
                    valorB=3000
                    ta=3000+100
                    totalB=o*valorA
                    
                    reb=reb+100
                if tipo==3:
                    valorC=2800
                    ta=2800+100
                    totalC=s*valorA
                    rec=rec+100
                    
                if tipo==4:
                    valorD=3500
                    ta=3500+100
                    totalD=d*valorA
                    red=red+100
                i=valorA+i
            if piso==4:
                ag=ag+1
                print("piso",piso,"tipo habitacion",tipo)
                if tipo==1:
                    valorA=3800
                    ta=3500+200
                    totalA=p*valorA
                    rea=rea+200
                if tipo==2:
                    valorA=3000
                    ta=3000+200
                    totalB=o*valorA
                    reb=reb+200
                if tipo==3:
                    valorA=2800
                    ta=2800+200
                    totalC=s*valorA
                    rec=rec+200
                if tipo==4:
                    valorA=3500
                    ta=3500+200
                    totalD=d*valorA
                    red=red+200
                i=valorA+i
            if piso==5:
                ah=ah+1
                
                print("piso",piso,"tipo habitacion",tipo)
                if tipo==1:
                    valorA=3800
                    ta=3800+300
                    totalA=p*valorA
                    rea=rea+300
                if tipo==2:
                    valorA=3000
                    ta=3000+300
                    totalB=o*valorA
                    reb=reb+300
                if tipo==3:
                    valorA=2800
                    ta=2800+300
                    totalC=s*valorA
                    rec=rec+300
                if tipo==4:
                    valorA=3500
                    ta=3500+300
                    totalD=d*valorA
                    red=red+300
                i=valorA+i
            if piso==6:
                aj=aj+1
                
                print("piso",piso,"tipo habitacion",tipo)
                if tipo==1:
                    valorA=3800
                    ta=3800+400
                    totalA=p*valorA
                    rea=rea+400
                    
                if tipo==2:
                    valorA=3000
                    ta=3000+400
                    totalB=o*valorA
                    reb=reb+400
                if tipo==3:
                    valorA=2800
                    ta=2800+400
                    totalC=s*valorA
                    rec=rec+400
                if tipo==4:
                    valorA=3500
                    ta=3500+400
                    totalD=d*valorA
                    red=red+400
                i=valorA+i
            if piso==7:
                ak=ak+1
                
                print("piso",piso,"tipo habitacion",tipo)
                if tipo==1:
                    valorA=3800
                    ta=3800+500
                    totalA=p*valorA
                    rea=rea+500
                if tipo==2:
                    valorA=3000
                    ta=3000+500
                    totalB=o*valorA
                    reb=reb+500
                if tipo==3:
                    valorA=2800
                    ta=2800+500
                    totalC=s*valorA
                    rec=rec+500
                if tipo==4:
                    valorA=3500
                    ta=3500+500
                    totalD=d*valorA
                    red=red+500
                i=valorA+i
            if piso==8:
                al=al+1
                
                print("piso",piso,"tipo habitacion",tipo)
                if tipo==1:
                    valorA=3800
                    ta=3800+600
                    totalA=p*valorA
                    rea=rea+600
                if tipo==2:
                    valorA=3000
                    ta=3000+600
                    totalB=o*valorA
                    reb=reb+600
                if tipo==3:
                    valorA=2800
                    ta=2800+600
                    totalC=s*valorA
                    rec=rec+600
                if tipo==4:
                    valorA=3500
                    ta=3500+600
                    totalD=d*valorA
                    red=red+600
                i=valorA+i
            if piso==9:
                an=+an+1
                
                print("piso",piso,"tipo habitacion",tipo)
                if tipo==1:
                    valorA=3800
                    ta=3800+700
                    totalA=p*valorA
                    rea=rea+700
                if tipo==2:
                    valorA=3000
                    ta=3000+700
                    totalB=o*valorA
                    reb=reb+700
                if tipo==3:
                    valorA=2800
                    ta=2800+700
                    totalC=s*valorA
                    rec=rec+700
                if tipo==4:
                    valorA=3500
                    ta=3500+700
                    totalD=d*valorA
                    red=red+700
            if piso==10:
                ab=ab+1
            
                print("piso",piso,"tipo habitacion",tipo)
                if tipo==1:
                    valorA=3800
                    
                    ta=3800+800
                    totalA=p*valorA
                    rea=rea+800
                if tipo==2:
                    valorA=3000
                    
                    ta=3000+800
                    totalB=o*valorA
                    reb=reb+800
                if tipo==3:
                    valorA=2800
                    ta=2800+800
                    totalC=s*valorA
                    rec=rec+800
                if tipo==4:
                    valorA=3500
                    
                    ta=3500+800
                    totalD=d*valorA
                    red=red+800

            total=totalA+totalB+totalC+totalD

            dicpersona["piso"]=piso
            dicpersona["tipo"]=tipo
            
            persona.append(dicpersona)

            depa[piso][tipo] = c
        
            print("\n")
            print("-----------------------")
            print("el total es: ",ta,"UF")
            print("-----------------------")
            f=input("presione enter para salir al manu principal ")
            break
    if respuesta==2:
        while True:
            print("departamentos disponibles son")
            for matriz in (depa): #Con éste bucle puedo imprimir la matriz completa en pantalla.
                print (matriz)
            f=input("presione enter para salir al manu principal ")
            break    

    if respuesta==3:
        while True:
            print("Los compradores son")
            for personas in persona:
                print(personas)
            f=input("presione enter para salir al manu principal ")
            break

    if respuesta==4:
        while True:
            try:
                busqueda2=int(input("ingrese rut sin guion ni puntos: "))
                break
            except ValueError:
                print("ingrese un rut valido")
        for personas in persona:
            if personas["rut"]==busqueda2: 
                print("encontrado ", personas["nombre"])
                while True:
                    try:
                        ru=int(input("ingrese nuevo rut sin guion ni puntos: "))
                        break
                    except ValueError:
                        print("ingrese un rut valido")
                personas["rut"]=ru
                    
                pa=input("ingrese nuevo nombre: ")
                personas["nombre"]=pa
                while True:
                    try:
                        ed=int(input("ingrese edad: "))
                        break
                    except ValueError:
                        print("ingrese una edad valida")
                personas["edad"]=ed  
                for personas in persona:
                    print(personas)
                f=input("presione enter para salir")
                break
    if respuesta==5:
        while True:
            gana =[ ["     ", "        Cantidad ", "Total   ", "Recargo por piso",],
                    ["Tipo A 3800 UF ",    p,"  ",totalA,"UF    ",rea  ], 
                    ["Tipo B 3000 UF ",    o,"  ",totalB,"UF    ",reb  ],  
                    ["Tipo C 2800 UF ",    s,"  ",totalC,"UF    ",rec  ], 
                    ["Tipo D 3500 UF ",    d,"  ",totalD,"UF    ",red  ], 
                    ["Total                    ",total,"UF","+ valor recargo",rea+reb+rec+red],
                    ["total ganancias: ", total+rea+reb+rec+red]
            ]
            for aba in (gana): 
                print (aba)
            f=input("presione enter para salir al manu principal ")
            break
    if respuesta==6:
        break
      