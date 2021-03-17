import hojas
id = 0
idImp = 0
class Arbol:
    def __init__(self):
        self.raiz = None
        self.nodoFinal = None
        self.nodos = []
        self.estructuras = []
        self.importantValues = []

    def get_nodos(self):
        return self.nodos
    def get_importantValues(self):
        return self.importantValues

    def crearHojasPipe(self, val1, val2, op):
        ##print("---------------HAY QUE HACER UNA PIPE----------")
        ##print("EL VALOR 1 ES",val1,"DE LEN", len(val1))
        ##print("EL VALOR 1 ES",val2,"DE LEN", len(val2))
        ##print("ESTRUCTURAS",self.estructuras)
        global id
        global idImp

        if(len(val1) == 1 and len(val2) == 1 and op =='|'):
            #print("IF DE PIPE DE UNA LETRA CON OTRA LETRA")
            # NODO 1 
            id+=1
            
            #(id, padreID, valor, hijos)
            if(val1 != "ε"):
                idImp+=1
                hoja1 = hojas.Hojas(id,'',val1,idImp,[])
                self.importantValues.append((hoja1,idImp,id))
            else:
                hoja1 = hojas.Hojas(id,'',val1,'',[])

            
            self.nodos.append(hoja1)
            
            ##print("SE CREO UN IMPORTANT VALUE")
            # NODO 2
            id+=1
            if(val2 != "ε"):
                idImp+=1
                hoja2 = hojas.Hojas(id,'',val2,idImp,[])
                self.importantValues.append((hoja2,idImp,id))
            else:
                hoja2 = hojas.Hojas(id,'',val2,'',[])

            self.nodos.append(hoja2)
            ##print("SE CREO UN IMPORTANT VALUE")
        
            # NODO 3
            id+=1
            
            ##print("EL ID DEL HIJO 1 ES",hoja1.get_id())
            ##print("EL ID DEL HIJO 2 ES",hoja2.get_id())

            hoja3 = hojas.Hojas(id,'',op,'', [hoja1,hoja2] )
            self.nodos.append(hoja3)

            hoja1.set_padreID(hoja3)
            hoja2.set_padreID(hoja3)

            ##print("EL ID DEL PAPA ES",hoja3.get_id())

            self.estructuras.append(hoja3.get_id())
            self.nodoFinal = self.estructuras[-1]
            ##print("LAS ESTRUCTURAS LUEGO DEL ASTERISCO PIPE DE LETRA Y LETRA",self.estructuras)


        elif( (len(val1) == 1 and len(val2) > 1) and op =='|' ):
            print("IF DONDE EL PRIMER VALOR ES 1 LETRA Y EL SEGUNDO UNA ESTRUCTURA")
            #print("*"*500)

        elif(  (len(val1) > 1 and len(val2) == 1) and op =='|'):
            print("IF DONDE EL PRIMER VALOR ES UNA ESTRUCTURA Y EL SEGUNDO 1 LETRA ")
            #print("*"*500)
    
        else:
            print("ENTRO AL IF DE PIPE DONDE ES PIPE DE ESTRUCTURAS ")
            print(self.estructuras)
            hojaH2 = self.nodos[self.estructuras[-1]-1]
            hojaH1 = self.nodos[self.estructuras[-2]-1]

            # NODO 1 
            id+=1
            #(id, padreID, valor, hijos)
            hoja1 = hojas.Hojas(id,'',op,'',[hojaH1,hojaH2])
            hojaH2.set_padreID(hoja1)
            hojaH1.set_padreID(hoja1)
            self.nodos.append(hoja1)



    def crear_nodosStar(self,val1,op):
        global id
        global idImp
        ##print("---------------HAY QUE HACER UNA ASTERISCO----------")
        ##print("El val 1 es", val1, "y es de largo de",len(val1))

        if(len(val1) == 1 and op =='*'):
            #print("IF DONDE EL VAL ES 1")
            id+=1
            if(val1 != "ε"):
                idImp+=1
                hoja1 = hojas.Hojas(id,'',val1,idImp,[])
                self.importantValues.append((hoja1,idImp,id))
            else:
                hoja1 = hojas.Hojas(id,'',val1,'',[])
            self.nodos.append(hoja1)
            ##print("SE CREO UN IMPORTANT VALUE")

            id+=1
            hoja2 = hojas.Hojas(id,'',op,'',[])
            self.nodos.append(hoja2)
            ##print("EL ID DEL HIJO",hoja1.get_id(),"SU PAPA SERA",hoja2.get_id())
            ##print("EL ID DEL PAPA",hoja2.get_id(),"SU HIJO SERA",hoja1.get_id())

            hoja1.set_padreID(hoja2)
            hoja2.set_hijos(hoja1)

            self.estructuras.append(hoja2.get_id())

            
        else:
            #print("STAR DE UNA OPERACION")

            # NODOS ACTUALIZADOS
            hojaH = self.nodos[-1]  
            
            # NODOS OPERACION
            id+=1
            hoja1 = hojas.Hojas(id,'',op,'',[])
            self.nodos.append(hoja1)

            ##print("EL ID DEL HIJO",hojaH.get_id(),"SU PAPA SERA",hoja1.get_id())
            ##print("EL ID DEL PAPA",hoja1.get_id(),"SU HIJO SERA",hojaH.get_id())

            hojaH.set_padreID(hoja1)
            hoja1.set_hijos(hojaH)

            
            
            ####print("SACANDO LA ESTRUCTURA",estructuras[-1])
            self.estructuras.pop()
            self.estructuras.append(hoja1.get_id())

            self.estadoFinal = self.estructuras[-1]

            ##print("LAS ESTRUCTURAS LUEGO DEL ASTERISCO DE ESTRUCTURA Y *",self.estructuras)


    def crear_nodosCat(self,val1,val2,op):
        global id
        global idImp
        #print("---------------HAY QUE HACER UNA CONCAT----------")
        ###print(estructuras)
        #print("El val 1 es", val1, "y es de largo de",len(val1))
        #print("El val 2 es", val2, "y es de largo de",len(val2))
        if(len(val2)==1 and len(val1)>1):
            #print("CONCATENAR ESTRUCTURA CON NODO")
            # NODOS OPERACION
            hojaH1 = self.nodos[-1]
            id+=1
            ##print("EL ID DEL HIJO1",hojaH1.get_id())
            if(val2 != "ε"):
                idImp+=1
                hojaH2 = hojas.Hojas(id,'',val2,idImp,[])
                self.importantValues.append((hojaH2,idImp,id))
            else:
                hojaH2 = hojas.Hojas(id,'',val2,'',[])
            ##print("SE CREO UN IMPORTANT VALUE")
            self.nodos.append(hojaH2)

            id+=1
            hoja2 = hojas.Hojas(id,'',op,'',[])
            self.nodos.append(hoja2)
            

            hojaH1.set_padreID(hoja2)
            hojaH2.set_padreID(hoja2)
            hijos = []
            hijos.append(hojaH1)
            hijos.append(hojaH2)
            for i in hijos:
                hoja2.set_hijos(i)

            #print("ESTRUCTURAS CONCAT EST NODO", self.estructuras)
            self.estructuras.pop()
            self.estructuras.append(hoja2.get_id())



            ##print("LAS ESTRUCTURAS LUEGO DEL PIPE DE 1 Y ESTRUCTURA",self.estructuras)
        elif(len(val2)>1 and len(val1)==1):
            print("CONCATENAR NODO CON ESTRUCTURA")
            #print("*"*500)
            
        elif(len(val2)==1 and len(val1)==1):
            print("IF DE CONCATENACION SI VAL 1 Y 2 SON LEN 1")
            id+=1
            ##print("EL ID DEL HIJO1",hojaH1.get_id())
            if(val1 != "ε"):
                idImp+=1
                hojaH1 = hojas.Hojas(id,'',val1,idImp,[])
                self.importantValues.append((hojaH1,idImp,id))
            else:
                hojaH1 = hojas.Hojas(id,'',val1,'',[])
            ##print("SE CREO UN IMPORTANT VALUE")
            self.nodos.append(hojaH1)

            id+=1
            ##print("EL ID DEL HIJO1",hojaH1.get_id())
            if(val2 != "ε"):
                idImp+=1
                hojaH2 = hojas.Hojas(id,'',val2,idImp,[])
                self.importantValues.append((hojaH2,idImp,id))
            else:
                hojaH2 = hojas.Hojas(id,'',val2,'',[])
            ##print("SE CREO UN IMPORTANT VALUE")
            self.nodos.append(hojaH2)

            id+=1
            hoja2 = hojas.Hojas(id,'',op,'',[])
            self.nodos.append(hoja2)
            hojaH1.set_padreID(hoja2)
            hojaH2.set_padreID(hoja2)
            hijos = []
            hijos.append(hojaH1)
            hijos.append(hojaH2)
            for i in hijos:
                hoja2.set_hijos(i)

            #print("ESTRUCTURAS CONCAT EST NODO", self.estructuras)
            #if(len(self.estructuras) >= 1):
            #    self.estructuras.pop()
            self.estructuras.append(hoja2.get_id())

            #print("*"*500)
        else:
            #print("CONCAT DE ESTRUCTURA CON ESTRUCTURA")
            hojaH2 = self.nodos[self.estructuras[-1]-1]
            hojaH1 = self.nodos[self.estructuras[-2]-1]
            id+=1
            hoja2 = hojas.Hojas(id,'',op,'',[])
            self.nodos.append(hoja2)
            hojaH1.set_padreID(hoja2)
            hojaH2.set_padreID(hoja2)
            hijos = []
            hijos.append(hojaH1)
            hijos.append(hojaH2)
            for i in hijos:
                hoja2.set_hijos(i)

            #print("ESTRUCTURAS CONCAT EST NODO", self.estructuras)
            self.estructuras.pop()
            self.estructuras.append(hoja2.get_id())
            


    