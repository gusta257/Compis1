import nodo


id = 0
estructuras = []

class AutomataFD:
    
    def __init__(self):
        self.estadoInicial = None
    
    def mov(self,statesMov, letraM,transM):
        moveA = []
        arrayNUEVO = statesMov.copy()
        stacker = []
        for vMov in arrayNUEVO:
            for bM in transM:
                if(bM[0] == vMov and bM[1] ==letraM):
                    #arrayNUEVO.append(bM[2])
                    moveA.append(bM[2])
        #print("*"*150)
        #print("EL ARRAR",arrayNUEVO)
        #print("EL MOVE",moveA)
        #print("*"*150)

        return moveA
        
    def cerraduraE(self, estadosCerradura,trans):
        cerradura = []
        nuevoArray = estadosCerradura.copy()
        visitados = []
        ##print("EL NUEVO ARRAY ES", nuevoArray)
        for qE in nuevoArray:
            for x in trans:
                if(x[0] == qE and x[1] =='ε' and (x[2] not in visitados)):
                    ##print("APPENDENADO",x[2])
                    visitados.append(x[2])
                    nuevoArray.append(x[2])
        res = [] 
        for i in nuevoArray: 
            if i not in res: 
                res.append(i) 
        cerradura = res
        return cerradura

    def afn(self, inicio,trans,sim):

        elementos = []
        transicionesNuevas = []
        dstates = []
        inicial = self.cerraduraE(inicio,trans)
        #print("*"*150)
        #print("LA INICIAL", inicial)
        dstates.append(inicial)
        elementos.append(inicial)

        for q in dstates:
            for c in sim:
                movea = self.mov(q,c,trans)
                #print("EL MOV DE",q,"CON",c,"ES", movea)
                U = self.cerraduraE(movea,trans)
                #print("LA U", U)

                if(U not in dstates and len(U) >= 1):
                    dstates.append(U)
                    elementos.append(U)
                if(len(U) >= 1):
                    transicionesNuevas.append( [q,c,U]  )

        return transicionesNuevas, elementos
## SE DEBE DE ARREGLAR LO DEL LOOP INFINITO DE EPSILONSCLS

        
    
    