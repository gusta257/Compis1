import nodo


id = 0
estructuras = []
structures = {}
class Automata:
    
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
        #print("---------------HAY QUE HACER UNA CONCAT----------")
        #print(estructuras)
        #print("El val 1 es", val1, "y es de largo de",len(val1))
        #print("El val 2 es", val2, "y es de largo de",len(val2))
        if(len(val2)==1 and len(val1)>1):
            #print("CONCATENAR ESTRUCTURA CON NODO")
            # NODO 1 
            id+=1
            nodoI1 = nodo.Nodo(id,'',[])
            self.nodos.append(nodoI1)

            # NODOS ACTUALIZADOS
            #print("ESTE NUM ES",estructuras[-1][1])
            nodoF1 = self.nodos[ estructuras[-1][1]-1 ]  
            nodoIP = self.nodos[ estructuras[-1][0]-1 ]
            nodoF1.set_valor(val2)
            nodoF1.set_transicion(nodoI1.get_id())
            #print("AL NODO",nodoF1.get_id(),"SE LE CONCATENARA EL NODO",nodoI1.get_id(),"CON LA TRANSICION",nodoF1.get_valor())
            #print("SACANDO LAS ESTRUCTURAS",estructuras[-1])
            estructuras.pop()
            estructuras.append((nodoIP.get_id(),nodoI1.get_id()))
            self.estadoInicial = estructuras[0][0]
            self.estadoFinal = estructuras[-1][1]
            #print("LAS ESTRUCTURAS LUEGO DEL PIPE DE 1 Y ESTRUCTURA",estructuras)
            
            # VERIFICAR SI SE HACE ALGO CON LA ESTRUCTURA SI SE APPENDEA ALGO O QUE
        elif(len(val2)>1 and len(val1)==1):
            #print("ENTRAMOS ACA XDDD")
            
            #print("CONCATENAR NODO CON ESTRUCTURA")
            # NODO 1 
            id+=1
            nodoI1 = nodo.Nodo(id,val1,[])
            self.nodos.append(nodoI1)

            # NODOS ACTUALIZADOS
            #print("ESTE NUM ES",estructuras[-1][0])  
            nodoIP = self.nodos[ estructuras[-1][0]-1 ]
            nodoF = self.nodos[ estructuras[-1][1]-1 ]
            nodoI1.set_transicion(nodoIP.get_id())

            #print("AL NODO",nodoI1.get_id(),"SE LE CONCATENARA EL NODO",nodoIP.get_id(),"CON LA TRANSICION",nodoI1.get_valor())
            #print("SACANDO LAS ESTRUCTURAS",estructuras[-1])
            estructuras.pop()
            estructuras.append((nodoI1.get_id(),nodoF.get_id()))
            self.estadoInicial = estructuras[0][0]
            self.estadoFinal = estructuras[-1][1]
            #print("LAS ESTRUCTURAS LUEGO DEL PIPE DE 1 Y ESTRUCTURA",estructuras)
            
            # VERIFICAR SI SE HACE ALGO CON LA ESTRUCTURA SI SE APPENDEA ALGO O QUE


        elif(len(val2)==1 and len(val1)==1):
            #print("IF DE CONCATENACION SI VAL 1 Y 2 SON LEN 1")
            
            #print(estructuras)
            # NODO 1 
            id+=1
            nodoI1 = nodo.Nodo(id,val1,[id+1])
            self.nodos.append(nodoI1)
            # NODO 2
            id+=1
            nodoI = nodo.Nodo(id,val2,[id+1])
            self.nodos.append(nodoI)
            # NODO 3
            id+=1
            nodoF1 = nodo.Nodo(id,'',[])
            self.nodos.append(nodoF1)
            estructuras.append((nodoI1.get_id(),nodoF1.get_id()))
            self.estadoInicial = estructuras[0][0]
            self.estadoFinal = estructuras[-1][1]
            #print("CONCATENO",nodoI1.get_id(),"CON",nodoF1.get_id(),"USANDO",nodoI.get_id())
            #print("-------------LAS ESTRUCTURAS LUEGO DE UN CONCAT---------", estructuras)

        else:
            #print("CUAndo entro acaaaaaaaafjsbd fjlshdfahdflkjahsdfla djf asldkf hadsjfh asldkfjh aslkjdfh asdjlkfh ajsdfh alksdfhfa sdl")
            #print(estructuras[-2][1])
            #print(estructuras[-1][0])
            nodoU1 = self.nodos[ estructuras[-2][1] -1]
            nodoU2 = self.nodos[ estructuras[-1][0] -1]
            nodoU1.set_valor('ε')
            nodoU1.set_transicion(nodoU2.get_id())
            self.estadoInicial = estructuras[0][0]
            self.estadoFinal = estructuras[-1][1]


    def crear_nodosPipe(self,val1,val2,op):
        global id
        global estructuras
        #print("PARA EL PIPE")
        #if(len())
        #print("El val 1 es", val1, "y es de largo de",len(val1))
        #print("El val 2 es", val2, "y es de largo de",len(val2))
        #print(estructuras)
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
            #print("LAS ESTRUCTURAS LUEGO DEL PIPE DE 1 Y 1",estructuras)
            self.estadoInicial = estructuras[0][0]
            self.estadoFinal = estructuras[-1][1]

        elif( (len(val1) == 1 and len(val2) > 1) and op =='|' ):
            #print("IF DONDE EL PRIMER VALOR ES 1 LETRA Y EL SEGUNDO UNA ESTRUCTURA")
            #print(estructuras)
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
            nodoIP = nodo.Nodo(id,'ε',[nodoI1.get_id(), self.nodos[estructuras[-1][0]-1].get_id() ])
            self.nodos.append(nodoIP)
            id+=1
            nodoFP = nodo.Nodo(id,'',[])
            self.nodos.append(nodoFP)

            # NODOS ACTUALIZADOS
            nodoF1.set_valor('ε')
            nodoF1.set_transicion(nodoFP.get_id())
            nodoF2 = self.nodos[ estructuras[-1][1]-1 ] 
            nodoF2.set_valor('ε')
            nodoF2.set_transicion(nodoFP.get_id())
            #print("NODOS CREADOS",nodoIP.get_id(),"Y", nodoFP.get_id())
            #print("SACANDO LAS ESTRUCTURAS",estructuras[-1])
            estructuras.pop()
            estructuras.append((nodoIP.get_id(),nodoFP.get_id()))
            #print("LAS ESTRUCTURAS LUEGO DEL PIPE DE 1 Y ESTRUCTURA",estructuras)




        elif(  (len(val1) > 1 and len(val2) == 1) and op =='|'):
            #print("IF DONDE EL PRIMER VALOR ES UNA ESTRUCTURA Y EL SEGUNDO 1 LETRA ")
            #print(estructuras)
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
            nodoIP = nodo.Nodo(id,'ε',[nodoI1.get_id(), self.nodos[estructuras[-1][0]-1].get_id() ])
            self.nodos.append(nodoIP)
            id+=1
            nodoFP = nodo.Nodo(id,'',[])
            self.nodos.append(nodoFP)

            # NODOS ACTUALIZADOS
            nodoF1.set_valor('ε')
            nodoF1.set_transicion(nodoFP.get_id())
            nodoF2 = self.nodos[ estructuras[-1][1]-1 ] 
            nodoF2.set_valor('ε')
            nodoF2.set_transicion(nodoFP.get_id())

            #print("NODOS CREADOS",nodoIP.get_id(),"Y", nodoFP.get_id())
            #print("SACANDO LAS ESTRUCTURAS",estructuras[-1])
            estructuras.pop()
            estructuras.append((nodoIP.get_id(),nodoFP.get_id()))
            #print("LAS ESTRUCTURAS LUEGO DEL PIPE DE 1 Y ESTRUCTURA",estructuras)

        else:
            #print("ENTRO AL IF DE PIPE DONDE ES PIPE DE ESTRUCTURAS ")
            # NODOS OPERACION
            id+=1
            nodoIP = nodo.Nodo(id,'ε',[estructuras[-2][0],estructuras[-1][0]])
            self.nodos.append(nodoIP)
            id+=1
            nodoFP = nodo.Nodo(id,'',[])
            self.nodos.append(nodoFP)

            # NODOS ACTUALIZADOS
            #print("LOS NODOS A UNIR LUEGO DEL PIPE SON:")
            nodoF1 = self.nodos[ estructuras[-2][1]-1 ]  
            nodoF2 = self.nodos[ estructuras[-1][1]-1 ] 
            #print(nodoF1.get_id(),"Y",nodoF2.get_id())

            nodoF1.set_valor('ε')
            nodoF1.set_transicion(nodoFP.get_id())
            nodoF2.set_valor('ε')
            nodoF2.set_transicion(nodoFP.get_id())
            #print("CONCATENO",nodoF1.get_id(),"CON",nodoFP.get_id())
            #print("CONCATENO",nodoF2.get_id(),"CON",nodoFP.get_id())

            #print("CONCATENO",nodoIP.get_id(),"CON", self.nodos[estructuras[-2][0]-1].get_id() )
            #print("CONCATENO",nodoIP.get_id(),"CON",self.nodos[estructuras[-1][0]-1].get_id() )
            #print("SACANDO LAS ESTRUCTURAS",estructuras[-1],"y",estructuras[-2])
            estructuras.pop()
            estructuras.pop()

            estructuras.append((nodoIP.get_id(),nodoFP.get_id()))
            self.estadoInicial = estructuras[0][0]
            self.estadoFinal = estructuras[-1][1]
            #print("LAS ESTRUCTURAS LUEGO DEL PIPE",estructuras)
            

    def crear_nodosStar(self,val1,op):
        global id
        #print("HACIENDO EL ASTERISCO")
        #print("El val 1 es", val1, "y es de largo de",len(val1))
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
            self.estadoInicial = estructuras[0][0]
            self.estadoFinal = estructuras[-1][1]
            #print("LAS ESTRUCTURAS LUEGO DEL ASTERISCO DE ESTRUCTURA Y *",estructuras)
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
            #print("SACANDO LA ESTRUCTURA",estructuras[-1])
            estructuras.pop()
            estructuras.append((nodoIS.get_id(),nodoFS.get_id()))
            self.estadoInicial = estructuras[0][0]
            self.estadoFinal = estructuras[-1][1]

            #print("LAS ESTRUCTURAS LUEGO DEL ASTERISCO DE ESTRUCTURA Y *",estructuras)
            
            
            
