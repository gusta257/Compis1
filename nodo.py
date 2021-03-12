class Nodo:
    def __init__(self, id, valor, transiciones = []):
        self. id = id
        self.valor = valor
        self.transiciones = transiciones
    
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_transision(self):
        return self.transiciones

    def set_transicion(self, transiciones):
        self.transiciones.append(transiciones)   
    
    def get_valor(self):
        return self.valor
    def set_valor(self, valor):
        self.valor = valor
'''
nodo1 = Nodo(1, 'a', [2,3])

print(nodo1)
print(nodo1.get_id())
print(nodo1.get_valor())
print(nodo1.get_transision())
'''