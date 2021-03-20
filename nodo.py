# CLASE NODO LA CUAL SERA LA FORMA DE CONSTRUCCION DE THOMPSON 
# CONTANDO CON SU ID EL VALOR QUE POSEE SU TRANSICION Y A DONDE VA
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

    def set_valor(self, val):
        self.valor = val
