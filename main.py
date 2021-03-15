import thompson, AFD, arbol
from graphviz import Digraph

r = input("ingrese la expresion regular: ")
rAFD = r
def precedence(op):
    if (op == '*'):
        return 3
    if (op == '.'):
        return 2
    if (op == '|'):
        return 1
    return 0

def arreglar2(r):
    i = 0
    expr = ''
    cont = 0 
    while i < len(r):
        if (r[i] == '|'):
            cont = 0
        elif(r[i] == '('):
            if (cont == 1):
                expr = expr + '.'
                cont = 0;
        elif(r[i] == ')' or r[i] == '*'):
            pass
        else:
            cont = cont + 1
        if(cont == 2):
            expr = expr+'.'+r[i]
            cont = 1
        else:
            expr = expr + r[i]
        i += 1
    return expr


def arreglar1(r):
    #ε
    i = 0
    expr = ''
    par = []
    sub = ''
    resta = []
    while i <len(r):
        if(r[i] =='('):
            par.append(i)
        if r[i] == '+':
            
            if(r[i-1] == ')'):

                sub = r[par.pop():i]
                
                expr = expr + '*' + sub
            else:
                expr = expr + '*' + r[i-1]
        elif r[i] == '?':
            if(r[i-1] == ')'):
    
                sub = r[par.pop():i]
                subl = len(sub)-1
                expr = expr[:-subl]
                expr = expr + sub
                expr = expr  +  '|' + 'ε)'
            else:
                letra = expr[-1]
                expr = expr[:-1]
                expr = expr + '(' + letra + '|' + 'ε)'
        else:
            expr = expr + r[i]
        i+=1

    return expr
'''
r = arreglar1(r)
r = arreglar2(r)
print("Nueva expresion regular:",r)
clase = thompson.Automata()
claseAFD = AFD.AutomataFD()


values = []
ops = []
i = 0 
nodos = []
while i < len(r):
    if r[i] == '(':
        ops.append(r[i])
    elif r[i].isalpha() or r[i].isdigit():
        values.append(r[i])
    elif r[i] == ')':
        while len(ops) != 0 and ops[-1] != '(':
            op = ops.pop()
            if op != '*':
                val2 = values.pop()
                val1 = values.pop()
                temp = val1+op+val2
                nodos.append(temp)
                if(op == '|'):
                    clase.crear_nodosPipe(val1,val2,op)
                elif(op == '.'):
                    clase.crear_nodosCat(val1,val2,op)
                values.append(temp)
        ops.pop()
    else:
        if(r[i] != '*'):
            while (len(ops) != 0 and precedence(ops[-1]) >= precedence(r[i])):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                temp = val1+op+val2
                nodos.append(temp)
                if(op == '|'):
                    clase.crear_nodosPipe(val1,val2,op)
                elif(op == '.'):
                    clase.crear_nodosCat(val1,val2,op)
                values.append(temp)
            ops.append(r[i])
        else:
            #print("Entro al else")
            val1 = values.pop()
            op = r[i]
            temp = val1+op
            #print('*------------ESTRELLA-------------*')
            clase.crear_nodosStar(val1,op)
            nodos.append(temp)
            values.append(temp)
            #values.append(applyOp(val1, val2, op))
    i+=1
while len(ops) != 0:
    #print("entre aca")
    val2 = values.pop()
    val1 = values.pop()
    op = ops.pop()
    temp = val1+op+val2
    nodos.append(temp)
    if(op == '|'):
        clase.crear_nodosPipe(val1,val2,op)
    elif(op == '.'):
        clase.crear_nodosCat(val1,val2,op)
    else:
        print("MMM ESTRELLA?")
    values.append(temp)

print(ops)
#print(values[-1])
print(nodos)
#-------------------------------------PROCESO DATOS---------------------------------------------------------------------------------
f = Digraph('finite_state_machine', filename='fsm.gv')
f.attr(rankdir='LR', size='8,5')

f.attr('node', shape='doublecircle')
f.node(str(clase.get_nodos()[-1].get_id()))

estados = []
simbolos = []
inicio = []
aceptacion = []
transiciones = []

inicio.append(str(clase.estadoInicial))
aceptacion.append(str(clase.estadoFinal))


for i in clase.get_nodos():
    
    estados.append(i.get_id())

    if(str(i.get_valor()) != "ε" and str(i.get_valor()) != ""):
        simbolos.append(i.get_valor())

    f.attr('node', shape='circle')
    largo = len(i.get_transision())
    if(largo == 0 ):
        pass
        #print(( i.get_id(), "FINAL"))
        
    elif (largo > 1):
        for j in i.get_transision():
        #    print( ( i.get_id(),i.get_valor() ) , j )
            transiciones.append(( str(i.get_id()),str(i.get_valor()), str(j)))
            f.edge(str(i.get_id()), str(j), label= str(i.get_valor()))
    else:
        #print(( i.get_id(),i.get_valor() ) , i.get_transision()[0] )

        transiciones.append(( str(i.get_id()),str(i.get_valor()), str(i.get_transision()[0])))

        f.edge(str(i.get_id()), str(i.get_transision()[0]), label=str(i.get_valor()))

resT = [] 
for i in simbolos: 
    if i not in resT: 
        resT.append(i) 
simbolos = resT

print("*----------------AUTOMATA AFN-------------------------------*")
print("Estados",estados)
print("Simbolos",simbolos)
print("Inicio",inicio)
print("Aceptacion",aceptacion)
print("Transiciones",transiciones)
#f.view()


#-------------------------------------PROCESO DATOS---------------------------------------------------------------------------------
automata, valoresF = claseAFD.afn(inicio,transiciones,simbolos)
#print('')
#print("VALORESf",valoresF)
#print('')
#for i in automata:
#    print("automata",i)
#print('')
llave = []
aceptacionA = []
for i in automata:
    for j in i[2]:
        
        if(j == aceptacion[0]):
            #print("LA J ES",j,"Y LA ACPTACION",aceptacion[0])
            llave.append(i[2])

resT = [] 
for i in llave: 
    if i not in resT: 
        resT.append(i) 
llave = resT

for i in llave:
    print(i)

nuevoDic = {}
contador = 0
nuevosValores = valoresF.copy()
for i in nuevosValores:
    nuevoDic[tuple(i)] = contador
    contador +=1
for item in automata:
    item[0]= str(nuevoDic.get(tuple(item[0])))
    item[2]= str(nuevoDic.get(tuple(item[2])))

for item in llave:
    aceptacionA.append(str(nuevoDic.get(tuple(item))))

fa = Digraph('finite_state_machine', filename='fsam.gv')
fa.attr(rankdir='LR', size='8,5')
for i in aceptacionA:

    fa.attr('node', shape='doublecircle')
    fa.node(i)

estadosA = []
simbolosA = []

resT = [] 
for i in automata: 
    if i not in resT: 
        resT.append(i) 
automata = resT
#print(automata)
for i in automata:
    estadosA.append(i[0])
    estadosA.append(i[2])
    fa.attr('node', shape='circle')
    fa.edge(str(i[0]), str(i[2]), label=str(i[1]))

resT = [] 
for i in estadosA: 
    if i not in resT: 
        resT.append(i) 
estadosA = resT
inicioA = [automata[0][0]]
print("*------------------AUTOMATA AFD-----------------------------*")
print("Estados",estadosA)
print("Simbolos",simbolos)
print("Inicio",inicioA)
print("Aceptacion",aceptacionA)
print("Transiciones",automata)
#fa.view()
print("*------------------AUTOMATA AFD DIRECTO-----------------------------*")
'''
claseAFDD = arbol.Arbol()
values = []
ops = []
i = 0 
nodos = []
rAFD = "("+rAFD+")#"
rAFD = arreglar1(rAFD)
rAFD = arreglar2(rAFD)
print("EL R DEL AFD ES",rAFD)
r = rAFD

while i < len(r):
    if r[i] == '(':
        ops.append(r[i])
    elif r[i].isalpha() or r[i].isdigit() or r[i] == '#':
        values.append(r[i])
    elif r[i] == ')':
        while len(ops) != 0 and ops[-1] != '(':
            op = ops.pop()
            if op != '*':
                val2 = values.pop()
                val1 = values.pop()
                temp = val1+op+val2
                nodos.append(temp)
                if(op == '|'):
                    claseAFDD.crearHojasPipe(val1,val2,op)
                    #clase.crear_nodosPipe(val1,val2,op)
                    print("Para el pipe")
                elif(op == '.'):
                    #clase.crear_nodosCat(val1,val2,op)
                    print("Para el concat")
                values.append(temp)
        ops.pop()
    else:
        if(r[i] != '*'):
            while (len(ops) != 0 and precedence(ops[-1]) >= precedence(r[i])):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                temp = val1+op+val2
                nodos.append(temp)
                if(op == '|'):
                    claseAFDD.crearHojasPipe(val1,val2,op)
                    print("Para el pipe")
                elif(op == '.'):
                    claseAFDD.crear_nodosCat(val1,val2,op)
                    print("Para el concat")
                values.append(temp)
            ops.append(r[i])
        else:
            #print("Entro al else")
            val1 = values.pop()
            op = r[i]
            temp = val1+op
            #print('*------------ESTRELLA-------------*')
            claseAFDD.crear_nodosStar(val1,op)
            print("Para la estrella")
            nodos.append(temp)
            values.append(temp)
            #values.append(applyOp(val1, val2, op))
    i+=1
while len(ops) != 0:
    #print("entre aca")
    val2 = values.pop()
    val1 = values.pop()
    op = ops.pop()
    temp = val1+op+val2
    nodos.append(temp)
    if(op == '|'):
        print("Para el pipe")
        claseAFDD.crearHojasPipe(val1,val2,op)
    elif(op == '.'):
        print("Para el concat")
        claseAFDD.crear_nodosCat(val1,val2,op)
    else:
        print("MMM ESTRELLA?")
    values.append(temp)

print(values)
print(nodos)
print(ops)
arboles = claseAFDD.get_nodos()
for i in arboles:
    print("LA HOJA",i.get_id(),i.get_valor(),"ES HIJA DE",i.get_padreID(),"Y ES PADRE DE",i.get_hijos())