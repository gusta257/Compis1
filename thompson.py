import nodo


id = 0
estructuras = []
class Thompson:
    
    def __init__(self):
        self.estadoInicial = None
        self.estadoFinal = None
        self.estados = []
        self.funcionTransicion = {}
        self.simbolos = []
        self.ids = []
        self.nodos = []
    
    def get_nodos(self):
        return self.nodos

    def crear_nodosCat(self,val1,val2,op):
        global id
        global estructuras
        print("HAY QUE HACER UNA CONCAT")
        print(estructuras)
        print("El val 1 es", val1, "y es de largo de",len(val1))
        print("El val 2 es", val2, "y es de largo de",len(val2))
        if(len(val2)==1):
            # NODO 1 
            id+=1
            nodoI1 = nodo.Nodo(id,'',[])
            self.nodos.append(nodoI1)

            # NODOS ACTUALIZADOS
            print("ESTE NUM ES",estructuras[-1][1])
            nodoF1 = self.nodos[ estructuras[-1][1] ]  

            nodoF1.set_valor(val2)
            nodoF1.set_transicion(nodoI1.get_id())





    def crear_nodosPipe(self,val1,val2,op):
        global id
        global estructuras

        #if(len())
        #print("El val 1 es", val1, "y es de largo de",len(val1))
        #print("El val 2 es", val2, "y es de largo de",len(val2))
        if(len(val1) == 1 and len(val2) == 1 and op =='|'):
            # NODO 1 
            id+=1
            nodoI1 = nodo.Nodo(id,val1,[id+1])
            self.nodos.append(nodoI1)
            # NODO 2
            id+=1
            nodoF1 = nodo.Nodo(id,'',[])
            self.nodos.append(nodoF1)

            # NODO 3
            id+=1
            nodoI2 = nodo.Nodo(id,val2,[id+1])
            self.nodos.append(nodoI2)
            # NODO 4
            id+=1
            nodoF2 = nodo.Nodo(id,'',[])
            self.nodos.append(nodoF2)

            # NODOS OPERACION
            id+=1
            nodoIP = nodo.Nodo(id,'ε',[nodoI1.get_id(),nodoI2.get_id()])
            self.nodos.append(nodoIP)
            id+=1
            nodoFP = nodo.Nodo(id,'',[])
            self.nodos.append(nodoFP)

            # NODOS ACTUALIZADOS
            nodoF1.set_valor('ε')
            nodoF1.set_transicion(nodoFP.get_id())
            nodoF2.set_valor('ε')
            nodoF2.set_transicion(nodoFP.get_id())
            

            estructuras.append((nodoIP.get_id(),nodoFP.get_id()))
        elif( (len(val1) == 1 and len(val2) == 2) and op =='|' ):
            print("hola")
            print(estructuras)
            # NODO 1 
            id+=1
            nodoI1 = nodo.Nodo(id,val1,[id+1])
            self.nodos.append(nodoI1)
            # NODO 2
            id+=1
            nodoF1 = nodo.Nodo(id,'',[])
            self.nodos.append(nodoF1)

            # NODOS OPERACION
            id+=1
            nodoIP = nodo.Nodo(id,'ε',[nodoI1.get_id(), self.nodos[estructuras[0][0]-1].get_id() ])
            self.nodos.append(nodoIP)
            id+=1
            nodoFP = nodo.Nodo(id,'',[])
            self.nodos.append(nodoFP)

            # NODOS ACTUALIZADOS
            nodoF1.set_valor('ε')
            nodoF1.set_transicion(nodoFP.get_id())
            nodoF2 = self.nodos[ estructuras[0][1]-1 ] 
            nodoF2.set_valor('ε')
            nodoF2.set_transicion(nodoFP.get_id())


        elif(  (len(val1) == 2 and len(val2) == 1) and op =='|'):
            print("Alo")
            print(estructuras)
            # NODO 1 
            id+=1
            nodoI1 = nodo.Nodo(id,val2,[id+1])
            self.nodos.append(nodoI1)
            # NODO 2
            id+=1
            nodoF1 = nodo.Nodo(id,'',[])
            self.nodos.append(nodoF1)

            # NODOS OPERACION
            id+=1
            nodoIP = nodo.Nodo(id,'ε',[nodoI1.get_id(), self.nodos[estructuras[0][0]-1].get_id() ])
            self.nodos.append(nodoIP)
            id+=1
            nodoFP = nodo.Nodo(id,'',[])
            self.nodos.append(nodoFP)

            # NODOS ACTUALIZADOS
            nodoF1.set_valor('ε')
            nodoF1.set_transicion(nodoFP.get_id())
            nodoF2 = self.nodos[ estructuras[0][1]-1 ] 
            nodoF2.set_valor('ε')
            nodoF2.set_transicion(nodoFP.get_id())

        else:

            # NODOS OPERACION
            id+=1
            nodoIP = nodo.Nodo(id,'ε',[estructuras[0][0],estructuras[1][0]])
            self.nodos.append(nodoIP)
            id+=1
            nodoFP = nodo.Nodo(id,'',[])
            self.nodos.append(nodoFP)

            # NODOS ACTUALIZADOS
            nodoF1 = self.nodos[ estructuras[0][1]-1 ]  
            nodoF2 = self.nodos[ estructuras[1][1]-1 ] 
            nodoF1.set_valor('ε')
            nodoF1.set_transicion(nodoFP.get_id())
            nodoF2.set_valor('ε')
            nodoF2.set_transicion(nodoFP.get_id())
            estructuras.append((nodoIP.get_id(),nodoFP.get_id()))
            

    def crear_nodosStar(self,val1,op):
        global id
        print("El val 1 es", val1, "y es de largo de",len(val1))
        # IF PARA CASO BASE DE * POR EJEMPLO A* O B* O (A*|B)
        if(len(val1) == 1 and op =='*'):
            # NODO 1 
            id+=1
            nodoI1 = nodo.Nodo(id,val1,[id+1])
            self.nodos.append(nodoI1)
            # NODO 2
            id+=1
            nodoF1 = nodo.Nodo(id,'',[])
            self.nodos.append(nodoF1)

            # NODOS OPERACION
            id+=1
            nodoIS = nodo.Nodo(id,'ε',[nodoI1.get_id()])
            self.nodos.append(nodoIS)
            id+=1
            nodoFS = nodo.Nodo(id,'',[])
            self.nodos.append(nodoFS)

            # NODOS ACTUALIZADOS
            nodoF1.set_valor('ε')
            nodoF1.set_transicion(nodoFS.get_id())
            nodoF1.set_transicion(nodoI1.get_id())
            nodoIS.set_transicion(nodoFS.get_id())

            estructuras.append((nodoIS.get_id(),nodoFS.get_id()))
        # ELSE POR SI SERA OPERACION * SOBRE UNA ESTRUCTURA COMO (A|B)* O ((A|B)|(C|D))*
        else:

            # NODOS OPERACION
            id+=1
            nodoIS = nodo.Nodo(id,'ε',[estructuras[-1][0]])
            self.nodos.append(nodoIS)
            id+=1
            nodoFS = nodo.Nodo(id,'',[])
            self.nodos.append(nodoFS)

            # NODOS ACTUALIZADOS
            nodoF1 = self.nodos[ estructuras[-1][1]-1 ]  
            nodoF1.set_valor('ε')
            nodoF1.set_transicion(nodoFS.get_id())
            nodoF1.set_transicion(self.nodos[estructuras[-1][0]-1].get_id())
            nodoIS.set_transicion(nodoFS.get_id())
            
            #estructuras.append((nodoIS.get_id(),nodoFS.get_id()))
            
