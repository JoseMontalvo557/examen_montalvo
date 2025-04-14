#Objetivo: Evaluacion Parcial
#Nombre: MONTALVO ROJAS, Jose Luis
#Fecha: 13/04/2025


menu1=0
i=0
fl=0
ml=0
masc=0
fem=0
mayEdad=0
menEdad=0
montototalAlu=0
alunolente=0
montodesc=0
#######################################################
usuario ="MONTALVO"
contraseña = 72944788
while(True):
    usuarioI=str(input("INGRESE UN USUARIO: "))
    contraseñaI=int(input("INGRESE SU CONTRASEÑA: "))
    if(usuarioI.upper() == usuario and int(contraseñaI) == contraseña):
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
    
    
    if(menu1 == 2):
        while(True):
            seccion=str(input("INGRESE SECCION A/B/C/D: "))
            if(seccion.upper() == "A"):
                break
            elif(seccion.upper() == "B"):
                break
            elif(seccion.upper() == "C"):
                break
            elif(seccion.upper() == "D"):
                break
            else:    
                print("SECCION INCORRECTA")
        while(True):
            cantAlu=int(input("INGRESE LA CANTIDAD DE ALUMNOS: "))
            if(cantAlu > 0):
                break
            print("########## ERROR  ##########")
        
        while(i<cantAlu):
            i=i+1
            apAlum=str(input("ingrese apellido del alumno: "))
            while(True):
                dniALum=int(input("INGRESE NUMERO DE DNI: "))
                if (len(str(dniALum)) == 8):
                    break
                else:
                     print("El DNI debe tener 8 dígitos.")
            while(True):
                sex=str(input("Ingresar Género (M/F) de alumno "))
                if(sex.upper() == "M" or "F"):
                    if(sex.upper()== "M"):
                        masc=masc+1
                        while(True):
                            lenT=int(input("¿Usa lentes? (1=SI / 0=NO) de alumno:"))
                            if(lenT == 1):
                                ml=ml+1
                                break
                            elif(lenT == 0):
                                alunolente=alunolente+1
                                break
                            else:
                                print(" ERROR SOLO (1=SI / 0=NO) ")
                    else:
                        fem=fem+1
                        while(True):
                            lenT=int(input("¿Usa lentes? (1=SI / 0=NO) de alumna: "))
                            if(lenT == 1):
                                fl=fl+1
                                break
                            elif(lenT == 0):
                                alunolente=alunolente+1
                                break
                            else:
                                print("ERROR ingrese correctamente")
                    break
                print("Error ingresar correctamente el genero M/F")
            
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
                montoAlu=int(input("ingreso monto del alumno: "))
                print("=================================================")
                if(montoAlu > 0):
                    montototalAlu=montototalAlu + montoAlu
                    if(apAlum.upper() == "MONTALVO"):
                        montodesc=montototalAlu-50
                        montoneto=montodesc
                    else:
                        montoneto=montoAlu
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
        print( 
              "\nDESCRIPCION                                                                MONTO ",
              "\n=================================================================================",                                   
              "\nCantidad de alumnos masculinos:                                      "," |  ",masc,
              "\nCantidad de alumnas femeninas:                                       "," |  ",fem, 
              "\nCantidad de alumnas con lentes:                                      "," |  ",fl, 
              "\nCantidad de alumnos con lentes:                                      "," |  ",ml,
              "\nCantidad de alumnos y alumnas SIN lentes:                            "," |  ",alunolente,
              "\nCantidad de alumnos menores de edad:                                 "," |  ",menEdad, 
              "\nCantidad de alumnos mayores de edad:                                 "," |  ",mayEdad,
              "\nSección ingresada:                                                   "," |  ",seccion,
              "\nMonto Total recaudado:                                               "," |  ",montototalAlu,
              "\nMonto Total recaudado – refrigerio del usuario experto (-50 soles):  "," |  ",montodesc,
              "\nMonto Total recaudado:                                               "," |  ",montoneto
              )
    if(menu1==5):
        break
    