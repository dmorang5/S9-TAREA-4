class Cola:
    def __init__(self, tamano):
        self.cola = []
        self.tope = 0
        self.size = tamano

    def empty(self):
        return self.tope == 0

    def push(self,tamaño):
        if self.size > self.tope:
            for x in range (tamaño):
                dato = input('Ingrese un dato a la listaa: ')
                self.cola.append(dato)
                self.tope += 1
        else:
            print('Lista Llena\n')

    def pop(self):
        if len(self.cola) != 0:
            self.cola.pop(0)
            self.tope -= 1
            print(f'Mostrando lista nueva: {self.cola}\n')
        else:
            print('Lista vacia\n')

    def longitud(self):
        print(f'La longitud de la Lista es: {len(self.cola)}\n')

    def show(self):
        if self.empty():
            print("Lista vacia")
        else:
            print("Mostrando la lista según como se ingresó: {}" .format(self.cola))                   
            for tope in range(self.tope):
                print("[{}]".format(self.cola[tope]))
            print("Mostrando la lista según la definición de cola: {}" .format(self.cola))   

    def buscar(self):
        if len(self.cola) != 0:
            pos = input('Ingrese el elemento para retornar una posicion: ')
            if pos in self.cola:
                print(f'Posicion: {self.cola.index(pos)}')
            else:
                print(f'Imprimiendo Elmento de la posicion -1: {self.cola[-1]}\n')
        else:
            print('Lista vacia\n')