from ClaseViajeroFrecuente import ViajeroFrecuente
import csv
from ManejadorViajero import Manejador

if __name__=="__main__":

    objeto=Manejador()
    objeto.TestLista()
    print("COMPARAR LA CANTIDAD DE MILLAS ACUMULADAS")
    objeto.mayor()

    print("________________________________________________________")

    print("ACUMULAR MILLAS")
    print ("Ingrese numero de viajero que desee acumular millas")
    numero=int (input())
    indice = objeto.buscar(numero)
    objeto.acumular(indice)

    print("________________________________________________________")

    print("CANJEAR MILLAS")
    print ("Ingrese numero de viajero que desee canjear millas")
    num=int (input())
    indice= objeto.buscar(num)
    objeto.canjear(indice)
