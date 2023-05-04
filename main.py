from Viajero import ViajeroFrecuente 
from GestorViajeros import GestorViajeros as GV
from menu import MenuOpciones as Menu
def test():
    print('PUNTO 1\n')
    gestor = GV()
    gestor.leerArchivo()
    print(gestor)
    print('\nPUNTO 21')
    menu= Menu()
    menu.opciones(gestor)
    print('\nPUNTO 3\n')
    gestor.obtenerMemoria()

if __name__ == '__main__':
    test()