class Registro():
    __Temperatura=0.0
    __Humedad=0
    __PresionAtmosferica=0.0
    
    def __init__(self,Temperatura,Humedad,PresionAtmosferica):
        self.__Temperatura=Temperatura
        self.__Humedad=Humedad
        self.__PresionAtmosferica=PresionAtmosferica
        
    def maxMin(self):
        max_temp = max(lista[1][1])
        pos = lista.i(max_temp)
        print(pos)
        min_temp = min(lista[1][1])
        pmin = lista.i(min_temp)
        print(pmin)
        print("La temperatura maxima es: {}, la temperatura minima es: {} ", format(lista[pos][pos]),format(lista[pmin][pmin]) )
    
    def tempPromedio(self):
        acum=0
        acum+=self.__Temperatura
        prom=acum/30
        print(prom)
        
    def listado(self,lista,dia):
        listaDia=[]
        for dia in range(dia):
            for h in range(0,horas):
                listaDia.append(self.__Temperatura,self.__Humedad,self.__PresionAtmosferica)
            
        
import csv
if __name__ == '__main__':
    
    arch=open("Reg.csv")
    reader=csv.reader(arch,delimiter=';')
   
    dias=3
    horas=3

    lista = [[0] * horas for dias in range(dias)]
    for d in range(0,dias):
        for h in range(0,horas):
            for fila in reader:
                Temperatura=fila[2]
                Humedad=fila[3]
                PresionAtmosferica=fila[4]
                unMes=Registro(Temperatura, Humedad, PresionAtmosferica)
                lista[d][h].append(unMes)
                print(lista)
            
    
    arch.close()    

    numviajero=int(input("Ingrese Numero de Viajero: "))
    opcion = input("Ingrese la opcion: ")
    
    menu = """
        ***MENU***
        [1] Mostrar para cada variable el día y hora de menor y mayor valor
        [2] Temperatura promedio mensual por cada hora
        [3] listar los valores de las tres variables para cada hora del día dado
        [0] SALIR
        """
    print(menu)
        
    if (opcion=='1'):
        print("accion 1")

    elif (opcion=='2'):
        print("accion 2")
        millas = int(input("Ingrese cantidad de millas a acumular: "))
        lista[numviajero-1].acumularMillas(millas)
    elif (opcion=='3'):
        print("accion 3")
        canje = int(input("Ingrese cantidad de millas a canjear: "))
        lista[numviajero-1].canjearMillas(canje)
    elif (opcion=='0'):
        print("accion 0")