from tkinter import *
from tkinter.filedialog import askopenfilename
import time
import re

class estructura_gramatica:
    def __init__ (self,nombre,noTerm,Term,inicio,producciones):
        self.nombre = nombre
        self.noTerm = noTerm
        self.Term = Term
        self.inicio = inicio
        self.producciones = producciones

class produccion:
    def __init__ (self,noTerminal,expresion):
        self.noTerminal = noTerminal
        self.expresion = expresion


listaGramaticas = []

listaProduciones = []

listaNoTerminales = ""
listaTerminales = ""

produccionAceptada = False




def bienvenida():
    print("------------------------------------Proyecto 2---------------------------------")
    print("-----------------------Juan José López Pérez // 201908075----------------------")
    print("--------------Lenguajes Formales y de Programación // Sección: B- -------------")
    print("-------------------------------------------------------------------------------")
    time.sleep(4)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n5")
    time.sleep(1)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n4")
    time.sleep(1)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n3")
    time.sleep(1)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n2")
    time.sleep(1)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n1")
    time.sleep(1)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nBienvenido!")


def main():
    while True:

        print("-------------------------------------------------------------------------------")
        print("1. Cargar Archivo")
        print("2. Visualizar Información general de la gramática")
        print("3. Generar autómata de pila equivalente")
        print("4. Generar reporte de recorrido")
        print("5. Generar reporte en tabla")
        print("6. Salir")
        print("-------------------------------------------------------------------------------\n")
        
        menu = input(">>")
        print("\n\n\n\n")
        if menu == "1":
            print("------------------------------------ Opción 1 ---------------------------------")
            cargar_archivo()

        elif menu == "2":
            print("------------------------------------ Opción 2 ---------------------------------")
            #visualizar_info()
            
        elif menu == "3":
            print("------------------------------------ Opción 3 ---------------------------------")
            #generar_automata()

        elif menu == "4":
            print("------------------------------------ Opción 4 ---------------------------------")
            #generar_reporte()

        elif menu == "5":
            print("------------------------------------ Opción 5 ---------------------------------")
            #generar_tabla()
            

        elif menu == "6":
            exit()

        else:
            print("Escoge una opción válida\n\n")

archivo = ""


def cargar_archivo():
    global archivo
  
  
    archivo_cargado = ""
    caracteres = ""

    #root = Tk()
    #root.withdraw()
    #root.update()
    #ruta = askopenfilename()
    #print("La ruta seleccionada fue: ")
    #print(ruta +"\n\n")

    ruta = "C:\\Users\\JuanJo\\Desktop\\Nuevo\\Lab_IPC2\\Lab_Lenguajes\\Proyectos\\Proyecto 2\\prueba.glc"
    

    with open(ruta, mode='r', encoding="utf-8") as archivo:
        for linea in archivo.readlines():
            archivo_cargado = archivo_cargado + linea

    #caracteres = list(archivo_cargado)
    #print(caracteres)
    espacioArray = []
    espacioArray = espacioArray + re.split(r'\*',archivo_cargado)
    
    #re.split('\n|,|;|->|\s|*',archivo_cargado)



    print('----------------separando segmentos--------------------')
    print(espacioArray)

    for gramatica in espacioArray:

        clasificar_gram(gramatica)

    gramaticas_Registradas()



def clasificar_gram(gramatica):
    global produccionAceptada, listaNoTerminales, listaTerminales, estructura

    nombre = ""
    noTerm = ""
    Term = ""
    inicio = ""
    #producciones =""

    listaProducciones = []

    estructura = estructura_gramatica(nombre,noTerm,Term,inicio,listaProducciones)
    
    datosArray = []
    datosArray = datosArray + re.split('\n|;', gramatica)

    print('------------------------------------')
    print(datosArray)

    if datosArray[0] == "":
        datosArray.pop(0)
    elif datosArray[len(datosArray)-1] == "":
        datosArray.pop(len(datosArray)-1)
    

    for i in range (0,len(datosArray)):

        if datosArray[i] == "":
            datosArray.pop(i)
            

    for i in range (0,len(datosArray)):

        print(str(i)+"//"+str(datosArray[i]))       
            

    for i in range (0,len(datosArray)):
        
        if i == 0:

            estructura.nombre = datosArray[i]

        elif i == 1:

            estructura.noTerm = datosArray[i]
            listaNoTerminales += datosArray[i]

        elif i == 2:

            estructura.Term = datosArray[i]
            listaTerminales += datosArray[i]

        elif i == 3:

            estructura.inicio = datosArray[i]

        else:
            
            noTerminal = ""
            expresion = ""
            
            prod = produccion(noTerminal, expresion)

            #ultimoTerminal = ""

            produccionArray = []

            produccionArray = produccionArray + re.split("->| ",datosArray[i])

            print("----------produccion---------")

            print(produccionArray)

            print("-----------------------------")

            for i in range (0,len(produccionArray)):

                print(str(i)+"//"+str(produccionArray[i]))    

            for i in range (0,len(produccionArray)):
                if produccionArray[i] == "":
                    produccionArray.pop(i)

            for i in range (0,len(produccionArray)):

                if i == 0:
                    for caracter in listaNoTerminales:
                        if produccionArray[i] == caracter:
                            prod.noTerminal = produccionArray[i]

                else:

                    if len(produccionArray)-1 == 3:

                        produccionAceptada = True

                        prod.expresion += produccionArray[i]

                    else:

                        prod.expresion += produccionArray[i]

                
            
            estructura.producciones.append(prod)

    if produccionAceptada == True: 
        listaGramaticas.append(estructura)
        produccionAceptada = False

    
    print("----------Lista Producciones---------")

    for t in estructura.producciones:

        print(str(t.noTerminal) +"->"+ str(t.expresion))
        listaNoTerminales = ""
        listaTerminales = ""


    print("-----------------------------")
    listaNoTerminales = ""
    listaTerminales = ""
    


def gramaticas_Registradas():

    print("----------Lista Gramáticas---------")

    for t in listaGramaticas:

        print(str(t.nombre))
        print("{"+ str(t.noTerm)+ "}")
        
        print("{"+ str(t.Term)+ "}")

        print(str(t.inicio))

        for x in t.producciones:

            print(str(x.noTerminal) +"->"+ str(x.expresion))

        



    print("-----------------------------")


#def reconocerProduccion(dato):
#    global produccionAceptada, estructura

   
        





#bienvenida()
main()