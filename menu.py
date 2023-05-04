from Viajero import ViajeroFrecuente 
from GestorViajeros import GestorViajeros

class MenuOpciones:
    __opcion= int
    def _init_(self):
        self.__opcion = 4

    def opciones(self, listaV):
        while self.__opcion!=0:
            print("\nMenu de opciones:")
            print("1 - Consultar Cantidad de Millas")
            print("2 - Acumular Millas")
            print("3 - Canjear Millas")
            print("0 - Salir\n")
            self.__opcion = int(input("Seleccione una opcion: "))
            if self.__opcion == 1:
                print('\nInciso a')
                viajero=listaV.buscarViajero(int(input('Ingrese numero de viajero frecuente: ')))
                if viajero!=None:
                    print(viajero.cantidadMillas())
                else:
                    print('El viajero no se encontro')
            elif self.__opcion == 2:
                print('\nInciso b')
                viajero=listaV.buscarViajero(int(input('Ingrese numero de viajero frecuente: ')))
                if viajero!=None:
                    print(viajero.acumularMillas(int(input('Ingrese cantidad de millas a acumular: '))))
                else:
                    print('El viajero no se encontro')
            elif self.__opcion == 3:
                print('\nInciso c')
                viajero=listaV.buscarViajero(int(input('Ingrese numero de viajero frecuente: ')))
                if viajero!=None:
                    cant=int(input('Ingrese cantidad de millas a canjear: '))
                    if cant<=viajero.cantidadMillas():
                        print('Nueva cantidad de millas acumuladas: %s'%viajero.canjearMillas(cant))
                    else:
                        print('Las millas no son suficientes para realizar el canje')
                else:
                    print('El viajero no se encontro')
            
            else:
                print('Ha salido con exito')
        