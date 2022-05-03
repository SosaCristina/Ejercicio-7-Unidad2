class ViajeroFrecuente:
    __num_viajero= 0
    __dni= ""
    __nombre=""
    __apellido=""
    __millas_acum= int

    def __init__(self, n_v, doc, nom, apell, mill):
        self.__num_viajero = n_v
        self.__dni = doc
        self.__nombre=nom
        self.__apellido=apell
        self.__millas_acum= int (mill)



    def getnum_viajero(self):
        return self.__num_viajero

    def getmillas_acum(self):
        return self.__millas_acum

    def getnombre (self):
        return self.__nombre
    def getapellido(self):
        return self.__apellido

    def mostrar (self):
        print ("Numero de viajero:{} - Nombre y apellido:{} {} - Cantidad de millas:{}".format(self.getnum_viajero(),self.getnombre(), self.getapellido(),self.getmillas_acum()))



    def __rgt__(self, otro):
     return (self.__millas_acum())


    def __radd__(self, otro):
        self.__millas_acum=otro + self.__millas_acum


    def __rsub__(self, otro):
        self.__millas_acum=self.__millas_acum - otro

    def __str__(self):
        return "%s %s %s %s %d"% (self.__num_viajero, self.__dni, self.__nombre, self.__apellido,self.__millas_acum)



