import thompson
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
#print(ops)
#print(values[-1])
#print(values)

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

    '''
    print("El valor 1:",val1)
    print("La operacion:", op)
    print("El valor 2:",val2)
    print("El temp:",temp)
    #clase.crear_nodos(val1,val2)
    print('*-----------FIN--------------*')
    '''
    values.append(temp)
    #values.append(applyOp(val1, val2, op))
    
print("NODOS",nodos)
#print(ops)
#print(values[-1])
print("VALUES",values)

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


print("*-----------------------------------------------*")
print("Estados",estados)
print("Simbolos",simbolos)
print("Inicio",inicio)
print("Aceptacion",aceptacion)
print("Transiciones",transiciones)

# ID ES EL NUMERO DEL NODO
# VALOR ES LA LETRA O EPSILON
# TRANSICION ES EL ID DEL NODO A DONDE VA

#f.view()
def mov(statesMov, letraM,transM):
    moveA = []

    arrayNUEVO = statesMov.copy()
    for vMov in arrayNUEVO:
        for bM in transM:
            if(bM[0] == vMov and bM[1] ==letraM):
                arrayNUEVO.append(bM[2])
                moveA.append(bM[2])

    return moveA

def cerraduraE(estadosCerradura,trans):
    cerradura = []
    #print("Last transiciones son", trans)
    nuevoArray = estadosCerradura.copy()
    for qE in nuevoArray:
        for x in trans:
            if(x[0] == qE and x[1] =='ε'):
                nuevoArray.append(x[2])
                #cerraduraE(s,trans)
                #print(s)
    res = [] 
    for i in nuevoArray: 
        if i not in res: 
            res.append(i) 
    
    cerradura = res
   # print("La cerradura epsilon es",cerradura)
    return cerradura

def afn(inicio,trans,sim):
    prueba = []
    transicionesNuevas = []
    dstates = []
    inicial = cerraduraE(inicio,trans)
    inicial.pop(0)
    dstates.append(inicial)
    prueba.append(inicial)
    numero = 0
    numero2 = 1
    for q in dstates:
        for c in sim:
            movea = mov(q,c,trans)
            U = cerraduraE(movea,transiciones)

            if(U not in dstates and len(U) >= 1):

                numero +=1
                dstates.append(U)
                prueba.append(U)
            if(len(U) >= 1):
                transicionesNuevas.append( [q,c,U]  )

        numero2+=1


    return transicionesNuevas, prueba
    
print('\n')
automata, valoresF = afn(inicio,transiciones,simbolos)
nuevoDic = {}
contador = 0
nuevosValores = valoresF.copy()
for i in nuevosValores:
    nuevoDic[tuple(i)] = contador
    contador +=1
for item in automata:
    item[0]= str(nuevoDic.get(tuple(item[0])))
    item[2]= str(nuevoDic.get(tuple(item[2])))

fa = Digraph('finite_state_machine', filename='fsam.gv')
fa.attr(rankdir='LR', size='8,5')


for i in automata:

    fa.attr('node', shape='circle')
    fa.edge(str(i[0]), str(i[2]), label=str(i[1]))

fa.view()

'''

print("*"*100)
print('\n')
t = cerraduraE(inicio,transiciones)
t.pop(0)
print("S0 es",t)
print('\n')

movea = mov(t,"a",transiciones)
print("EL MOVE DE S0 con A es",movea)
print("LA PINCHE T ES",t)
t1 = cerraduraE(movea,transiciones)
print("S1, La cerradura epsilon de MOVE (S0,A) es",t1)
print('\n')
moveb = mov(t,"b",transiciones)
print("EL MOVE DE S0 con b es",moveb)
t2 = cerraduraE(moveb,transiciones)
print("S2, La cerradura epsilon de MOVE (S0,B) es",t2)
print('\n')

movea1 = mov(t1,"a",transiciones)
print("EL MOVE DE S1 con A es",movea1)
t3 = cerraduraE(movea1,transiciones)
print("IGUAL A S1, La cerradura epsilon de MOVE (S1,A) es",t3)
print('\n')
moveb1 = mov(t1,"b",transiciones)
print("EL MOVE DE S1 con b es",moveb1)
t4 = cerraduraE(moveb1,transiciones)
print("La cerradura epsilon de MOVE (S1,B) es",t4)
print('\n')

movea2 = mov(t2,"a",transiciones)
print("EL MOVE DE S2 con A es",movea2)
t5 = cerraduraE(movea2,transiciones)
print("La cerradura epsilon de MOVE (S2,A) es",t5)
print('\n')
moveb2 = mov(t2,"b",transiciones)
print("EL MOVE DE S2 con b es",moveb2)
t6 = cerraduraE(moveb2,transiciones)
print("La cerradura epsilon de MOVE (S2,B) es",t6)
'''