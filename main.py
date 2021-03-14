import thompson, AFD
from graphviz import Digraph

r = input("ingrese la expresion regular: ")

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

r = arreglar1(r)
r = arreglar2(r)
print("Nueva expresion regular:",r)
clase = thompson.Automata()
claseAFD = AFD.AutomataFD()

#def metodo_pipe():
     # crear 
#w = input("ingrese la cadena")
values = []
ops = []
i = 0 
nodos = []
puedeSer = []
while i < len(r):
    #print(r[i])
    
    if r[i] == '(':
        #print("Parentesis abre")
        ops.append(r[i])
    elif r[i].isalpha() or r[i].isdigit():
        #print("letra",r[i])
        values.append(r[i])
    elif r[i] == ')':
        #print('Parentesis cierra')
        while len(ops) != 0 and ops[-1] != '(':
            #print("operacion en parentesis",ops)
            #print("valores en parentesis",values)
            op = ops.pop()
            if op != '*':
                val2 = values.pop()
                val1 = values.pop()
                temp = val1+op+val2
                nodos.append(temp)
                '''
                print("El valor 1:",val1)
                print("La operacion:", op)
                print("El valor 2:",val2)
                print("El temp:",temp)
                print('*-------------------------*')
                '''
                if(op == '|'):
                    clase.crear_nodosPipe(val1,val2,op)
                elif(op == '.'):
                    clase.crear_nodosCat(val1,val2,op)
                
                #puedeSer.append(temp)
                values.append(temp)
        ops.pop()
    else:
        #print("operacion agregada",r[i])
        #print("operaciones al agregar",r[i],":",ops)
        #print("valores al agregar",values)
        if(r[i] != '*'):
            while (len(ops) != 0 and precedence(ops[-1]) >= precedence(r[i])):
                #print(values)
                #print(ops)
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                temp = val1+op+val2
                nodos.append(temp)
                if(op == '|'):
                    clase.crear_nodosPipe(val1,val2,op)
                elif(op == '.'):
                    clase.crear_nodosCat(val1,val2,op)
                '''
                print("El valor 1:",val1)
                print("La operacion:", op)
                print("El valor 2:",val2)
                print("El temp:",temp)
                print('*------------ACA------------*')
                '''
                values.append(temp)
                #values.append(applyOp(val1, val2, op))
            ops.append(r[i])
        else:
            #print("Entro al else")
            val1 = values.pop()
            op = r[i]
            temp = val1+op
            #print(values)
            #print(ops)
            #val2 = values.pop()
            #val1 = values.pop()
            #op = ops.pop()
            #temp = val1+op+val2
            '''
            print("El valor 1:",val1)
            print("La operacion:", op)
            print("El temp:",temp)
            print('*------------ESTRELLA-------------*')
            '''
            clase.crear_nodosStar(val1,op)
            nodos.append(temp)
            values.append(temp)
            #values.append(applyOp(val1, val2, op))
    i+=1
#print('*---------------------------------------------------------------*')


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
print(values)
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
f.view()


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
fa.view()

