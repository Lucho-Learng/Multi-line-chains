#lISTAS>>>UN VALOR DE LISTA PUEDE CONTENER OTROS VALORES DENTRO. INTRODUCELO EN EL TERMINAL INTERACTIVO...
SPAM= ['Vida', 'El Universo', 'Todo', 42]
SPAM[0]
SPAM[1]
SPAM[2]
SPAM[3]
print(SPAM)

#INDICES>>> INTRODUCIR ANIMALES EN EL TERMINAL INTERACTIVO PARA ALMACENAR UNA LISTA EN LA VARIABLE ANIMALES
animales = ['águila', 'alce', 'antílope', 'alberto']
print(animales)
animales[0]
print(animales[0])
animales[1]
print(animales[1])
animales[2] 
print(animales[2])
animales[3]
print(animales[3])
y = (animales[0] + animales[3])
print(y)


#INDICES>>> CAMBIANDO L0S VALORES DE LOS ELEMENTOS DE UNA LISTA CON ASIGNACION POR INDICE.
Animales = ['AGUILA', 'ALCE', 'ANTILOPE', 'lOUIS']
print(Animales)
Animales[3] = 'LoBo'
print(Animales)


#EL OPERADOR (in) ME DICE SI UN VALOR ESTA EN LA LISTA O NO... [(CON UN VALOR LOGICO (True o False))]
animals = ['águila', 'alce', 'antílope', 'Andrea']

'antílope' in animals == True
print('antílope' in animals)

'atún' in animals == False
print('atún' in animals)


#LISTAS DE LISTAS>>> LAS LISTAS PUEDEN CONTENER OTROS VALORES, INCLUYENDO OTRAS LISTAS.
Comestibles = ['Huevos', 'Leche', 'Sopa', 'Manzanas', 'Pan']
Tareas = ['Limpiar', 'Cortar el césped', 'Ir al supermercado']
PastelesFavoritos = ['Manzana', 'Zarzamora']
ListasDeListas = [Comestibles, Tareas, PastelesFavoritos]
print(ListasDeListas)
# ListasDeListas[1][2] OBTENGO UN ELEMENTO DENTRO DE UNA LISTA DE LISTAS
print(ListasDeListas[1][2])


#LISTAS>>> CONCATENACION DE LISTAS.
LIST = [1, 2, 3, 4] + ['MANZANAS', 'NARANJAS'] + ['ALICIA', 'JHON']
print(LIST)


#LISTAS>>> ELIMINANDO ELEMENTOS DE LISTAS CON SENTENCIAS (del)
span = [2, 4, 6, 8, 10]
print(span)
del span[1]
print(span)
del span[2]
print(span)
#[2, 6, 8, 10]


#METODOS DE>>> CADENA
'Hello World'.lower() #ME DEVUELVE EL TEXTO EN (minúsculas).
print('Hello World'.lower())
#'hello world'

'HeLlo WoRLd'.upper() #ME DEVUELVE EL TEXTO EN (MAYÚSCULAS).
print('HeLlo WoRLd'.upper())
#'HELLO WORLD'


# METODOS DE LISTA>>> reverse() y append()
spam = [1, 2, 3, 4, 5, 6, 'miau', 'guau']
print(spam)
spam.reverse()
print(spam)
['guau', 'miau', 6, 5, 4, 3, 2, 1]


# EL METODO MAS COMUN APPEND>>>ESTE METODO AÑADE EL VALOR QUE PASA COMO ARGUMENTO AL FINAL DE LA LISTA.
eggs = []
eggs.append('hovercraft')
print(eggs)
eggs.append('eels')
print(eggs)
eggs.append(42)
print(eggs)


#LISTA>>>EL METODO DE LISTA split()LARGA LINEA DE CODIGO, PERO SOLO ES UNA SIMPLE SENTENCIA DE ASIGNACION.
#EL METODO SPLIT() DEVUELVE UNA LISTA EN LA Q CADA PALABRA EN LA CADENA ES UN ELEMENTO APARTE.
#LA SEPARACION OCURRE EN CUALQUIER LUGAR DONDE HAYA UN ESPACIO EN LA CADENA.
Palabras = ' HORMIGAS BABUINO TEJON MURCIELAGO OSO CASTOR CAMELLO GATO ALMEJA COBRA PANTERA COYOTE CUERVO CIERVO PERRO BURRO PATO AGUILA HURON ZORRO RANA CABRA GANSO HALCON LEON LAGARTO LLAMA TOPO MONO ALCE RATON MULA SALAMANDRA NUTRIA BUHO PANDA LORO PALOMA PITON CONEJO CARNERO RATA CUERVO RINOCERONTE SALMON TIBURON FOCA OVEJA MOFETA  PEREZOSO SERPIENTE ARAÑA CIGÜEÑA CISNE TIGRE SAPO TRUCHA PAVO TORTUGA COMADREJA BALLENA LOBO WOMBAT CEBRA'.split() 
print(Palabras)  


print('Ingresa una oración')
Oracion = input()
Oracion.split()
