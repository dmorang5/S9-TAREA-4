import time
class Stack:                
    def __init__(self,tamanio):
        self.pila=[]
        self.tope=0
        self.size=tamanio
    
    def empty(self):
        return self.tope == 0

    def push(self,tamaño):
        if self.tope < self.size:
            for x in range (tamaño):
                dato = input("Ingrese un dato a la lista: ")
                self.pila += [dato]
                self.tope += 1
        else:
            print("La Lista se encuentra Llena")
   
    def pop(self):
        if len(self.pila) != 0:
            self.pila.pop()
            self.tope -= 1
            print(f'Mostrando lista nueva: {self.pila}\n')
        else:
            print('Lista vacia\n')
            
    def longitud(self):
        print(f'La longitud de la lista es: {len(self.pila)}\n')               

    def show(self):
        if self.empty():
            print("Lista vacia")
        else:
            print("Mostrando la lista según como se ingresó: {}" .format(self.pila))                   
            for tope in range(self.tope-1,-1,-1):
                print("[{}]".format(self.pila[tope]))
            print("Mostrando la lista según la definición de pila: {}" .format(self.pila[::-1])) 

    def buscar(self):
        if len(self.pila) != 0:
            pos = input('Ingrese el elemento para retornar una posicion: ')
            if pos in self.pila:
                print(f'Posicion: {self.pila.index(pos)}')
            else:
                print(f'Imprimiendo Elemento de la posicion -1: {self.pila[-1]}\n')
        else:
            print('Lista vacia\n')
