from ClaseViajeroFrecuente import ViajeroFrecuente
import csv

class Manejador:
    __lista=[]
    def __init__(self):
        self.__lista=[]


    def TestLista (self):
        archivo=open("ListaViajero.csv")
        reader=csv.reader(archivo,delimiter=";")
        for fila in reader:
            num_viajero= int(fila[0])
            dni= fila[1]
            nombre=fila[2]
            apellido=fila[3]
            millas_acum= fila[4]
            unViajero=ViajeroFrecuente(num_viajero,dni,nombre,apellido,millas_acum)
            self.__lista.append(unViajero)
            print(unViajero)

        archivo.close()

    def buscar (self, numero):
        indice=int
        indice=0

        while indice < len(self.__lista) and (numero!=self.__lista[indice].getnum_viajero()):
            indice+=1
        if (indice<len(self.__lista)):
            return indice
        else:
            print("Numero de viajero incorrecto")

    def mayor (self):
        max=0
        indice=0
        for i in range (len(self.__lista)):
           if (self.__lista[i].getmillas_acum()>=max):
               max=self.__lista[i].getmillas_acum()
               indice=i
        for j in range(len(self.__lista)):
           if j <= indice:
               if self.__lista[j].getmillas_acum()==max:
                   self.__lista[j].mostrar()





    def acumular (self, indice):
        unViajero = self.__lista[indice]
        mill=int (input("Ingresar cantidad de millas"))
        mill + unViajero
        print("Total Millas, actualizada con acumulacion:{}".format(unViajero.getmillas_acum()))

    def canjear (self, indice):
        unViajero = self.__lista[indice]
        mill= int (input("Ingresar cantidad de millas a canjear"))
        mill - unViajero
        print("Total Millas, actualizada con canje:{}".format(unViajero.getmillas_acum()))


    def __str__(self):
        s=""
        for lista in self.__lista:
            s+=str(lista) + "\n"
        return s


