#Objetivo: Evaluacion Parcial
#Nombre: MONTALVO ROJAS, Jose Luis
#Fecha: 13/04/2025

usuario ="MONTALVO"
contraseña = 72944788
menu1=0
#######################################################
while(True):
    usuarioI=str(input("INGRESE UN USUARIO: "))
    contraseñaI=int(input("INGRESE SU CONTRASEÑA: "))
    if(usuarioI.upper() == usuario and contraseñaI == contraseña):
        break
    print("#########INGRESE NUEVAMENTE SUS ACCESOS#########")

while(True):
    menu1 =int(input("""
    *****MENÚ DE OPCIONES*****
    [1]. AUTENTICARSE
    [2]. REGISTRAR DONACIONES
    [3]. CALCULADORA
    [4]. REPORTE TOTAL
    [5]. SALIR DEL PROGRAMA.
        """))
    sc="A" or "B" or "C" or "D"
    if(menu1 == 2):
        while(True):
            seccion=str(input("INGRESE SECCION A/B/C/D: "))
            if(seccion.upper() == sc):
                break
            else:    
                print("SECCION INCORRECTA")
        while(True):
            cantAlu=int(input("INGRESE LA CANTIDAD DE ALUMNOS: "))
            if(cantAlu > 0):
                break
            print("###########  ERROR  ##########")
        i=0
        l=0
        masc=0
        fem=0
        mayEdad=0
        menEdad=0
        montototalAlu=0
        while(i<cantAlu):
            i=i+1
            apAlum=str(input("ingrese apellido del alumno: "))
            while(True):
                dniALum=int(input("INGRESE NUMERO DE DNI: "))
                if(dniALum > 0 ):
                    break
                print("Faltan digitos en el DNI")
            while(True):
                sex=str(input("Ingresar Género (M/F) de alumno "))
                if(sex.upper() == "M" or "F"):
                    if(sex.upper()== "M"):
                        masc=masc+1
                    else:
                        fem=fem+1
                    break
                print("Error ingresar correcta mente el genero M/F")
            while(True):
                len=str(input("¿Usa lentes? (1=SI / 0=NO) de alumno"))
                if(len == "1" or "0"):
                    if(len=="1"):
                        l=l+1
                    break
                print(" ingrese correctamente") 
            while(True):
                edad=int(input("ingresar edad de alumno: "))
                if(edad >13 and edad <=18):
                    if(edad >= 18):
                        mayEdad=mayEdad+1
                    else:    
                        menEdad=menEdad+1
                    break
                print("ingrese edades  correctas ")
            while(True):
                montoAlu=int(input("ingreso monto del alumano: "))
                if(montoAlu > 0):
                    montototalAlu=montototalAlu + montoAlu
                    break
                print("ingrese numero correctos ")


    if(menu1==3):
        while(True):
            menu = str(input("""
            ======== BIENVENIDO AL SUB MENU DE CALCULADORA ========
[A] SUMA DE DOS NUMEROS
[B] RESTA DE DOS NUMEROS
[C] MULTIPLICACION DE DOS NUMEROS
[D] DIVISION DE DOS NUMEROS
[E] MÓDULO DE DOS NUMEROS
                
                """))
            
            if(menu == "A" ):
                respuesta=0    
                while(True):
                    numsuma1 =int(input("ingresar primer numero: "))
                    if(numsuma1 > 0):
                        break
                    print("\tERROR DE USUARIO....Ingrese numero valido:  ")
                while(True):
                    numsuma2 =int(input("ingresar segundo numero: "))
                    if(numsuma2 > 0):
                        break
                    print("\tERROR DE USUARIO....Ingrese numero valido:  ")
                                    
                respuesta= numsuma1+numsuma2
                print("LA RESPUESTA ES : ",respuesta)      
            

            if(menu == "B"):
                while(True):
                    numsuma1 =int(input("ingresar primer numero: "))
                    if(numsuma1 > 0):
                        break
                    print("\tERROR DE USUARIO....Ingrese nota valida:  ")
                while(True):
                    numsuma2 =int(input("ingresar primer numero: "))
                    if(numsuma2 > 0):
                        break
                    print("\tERROR DE USUARIO....Ingrese nota valida:  ")
                respuesta=numsuma1-numsuma2
                print("LA RESPUESTA ES : ",respuesta)

            elif(menu == "C"):
                respuesta=0    
                while(True):
                    numsuma1 =int(input("ingresar primer numero: "))
                    if(numsuma1 > 0):
                        break
                    print("\tERROR DE USUARIO....Ingrese numero valido:  ")
                while(True):
                    numsuma2 =int(input("ingresar SEGUNDO numero: "))
                    if(numsuma2 > 0):
                        break
                    print("\tERROR DE USUARIO....Ingrese numero valido:  ")
                                    
                respuesta= numsuma1*numsuma2
                print("LA RESPUESTA ES : ",respuesta) 
            
            elif(menu == "D"):
                while(True):
                    numsuma1 =int(input("ingresar primer numero: "))
                    if(numsuma1 > 0):
                        break
                    print("\tERROR DE USUARIO....Ingrese nota valida:  ")
                    if(numsuma1 == 0):
                        print("ERROR NO SE PUEDE DIVIDIR ENTRE CERO")
                while(True):
                    numsuma2 =int(input("ingresar primer numero: "))
                    if(numsuma2 > 0):
                        break
                    print("\tERROR DE USUARIO....Ingrese nota valida:  ")
                    if(numsuma2 == 0):
                        print("ERROR NO SE PUEDE DIVIDIR ENTRE CERO")
                respuesta=numsuma1/numsuma2
                print("LA RESPUESTA ES : ",respuesta)
            elif(menu == "E"):    
                respuesta=0    
                while(True):
                    numsuma1 =int(input("ingresar primer numero: "))
                    if(numsuma1 > 0):
                        break
                    print("\tERROR DE USUARIO....Ingrese numero valido:  ")
                while(True):
                    numsuma2 =int(input("ingresar SEGUNDO numero: "))
                    if(numsuma2 > 0):
                        break
                    print("\tERROR DE USUARIO....Ingrese numero valido:  ")
                respuesta=numsuma1%numsuma2
                print("LA RESPUESTA ES : ",respuesta)
            break 
        break
    if(menu1==4):   
        print("lentessi: ",l , "\nhombre ",masc,"\nmujeres ",fem, "\nmayor de edad",mayEdad, "\nmenor edad ",menEdad, "\nmonto",montototalAlu)