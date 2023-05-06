from Viajero import ViajeroFrecuente 
from GestorViajeros import GestorViajeros as GV
from menu import MenuOpciones as Menu
def test():
    print('PUNTO 1\n')
    gestor = GV()
    gestor.leerArchivo()
    print(gestor)
    print('\nPUNTO 2')
    menu= Menu()
    menu.opciones(gestor)

if __name__ == '__main__':
    test()