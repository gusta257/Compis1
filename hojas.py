class Hojas:
    def __init__(self, id, padreID, valor, iDImportante, hijos=[]):
        self.id = id
        self.padreID = padreID
        self.valor = valor
        self.hijos = hijos
        self.iDImportante = iDImportante
    
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_iDImportante(self):
        return self.iDImportante

    def set_iDImportante(self, id):
        self.iDImportante = id

    def get_padreID(self):
        return self.padreID

    def set_padreID(self, padreId):
        self.padreID = padreId   
    
    def get_valor(self):
        return self.valor

    def set_valor(self, val):
        self.valor = val
    
    def get_hijos(self):
        return self.hijos

    def set_hijos(self, hijos):
        self.hijos.append(hijos)   

