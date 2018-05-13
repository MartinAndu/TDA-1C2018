'''
Complejidad: O(n)
'''

def kmp_tabla(W):
    pos = 1
    cnd = 0

    tamanio = len(W)
    T = [0] * (tamanio + 1)
    T[0] = -1

    while pos < tamanio:
        if W[pos] == W[cnd]:
            T[pos] = T[cnd]
            pos = pos + 1
            cnd = cnd + 1
        else:
            T[pos] = cnd
            while cnd >= 0 and W[pos] != W[cnd]:
                cnd = T[cnd]
            pos = pos + 1
            cnd = cnd + 1
    T[pos] = cnd

    return T

def kmp(S, W):
    if (len(S) != len(W)):
        print(S + " no es una rotacion de " + W)
    elif _kmp(S, W, len(S), len(W)):
        print (S + " es una rotacion de " + W)
    else:
        print(S + " no es una rotacion de " + W)

'''
 Este procediiento muestra por pantalla si 2 cadenas (S,W) de longitud n son
 rotaciones entre si.
 Complejidad: O(n)
 '''
def kmp_n(S, W):
    if (len(S) != len(W)):
        print(S + " no es una rotacion de " + W)
    elif es_rotacion(S, W, len(S)):
        print (S + " es una rotacion de " + W)
    else:
        print(S + " no es una rotacion de " + W)

'''
 Este procediiento muestra por pantalla si 2 cadenas (S,W) de longitud n son
 rotaciones entre si.
 Complejidad: O(n + n^2)=O(n^2)
'''
def _kmp(S, W, lenS, lenW):
    np = 0
    j = 0
    k = 0
    T = kmp_tabla(W) # complejidad O(n)
    rotacion = False
    while j < lenS and not rotacion: # complejidad O(n)
        if W[k] == S[j]:
            j = j + 1
            k = k + 1
            if k == lenW:
                np = np + 1
                k = T[k]
            str_tmp = W[k:] + W[:k]
            if (kmp_comp(str_tmp, S, lenS)): #complejidad O(n)
                rotacion = True
        else:
            k = T[k]
            if k < 0:
                j = j + 1
                k = k + 1
    return rotacion

''' Esta funcion toma como parametros 2 cadenas (S,W) de longitud n
    y devuelve True sin son rotaciones entre si. False caso contrario
    Complejidad algoritmica: O(2n)=O(n)
'''
def es_rotacion(S, W, length):
    np = 0
    j = 0
    k = 0
    T = kmp_tabla(W)
    while j < 2*length: #complejidad O(2n)=O(n)
        flag = False
        if j >= length:
            if W[k] == S[j - length ]:
                flag = True
        else:
            if W[k] == S[j]:
                flag = True
        if flag:
            j = j + 1
            k = k + 1
            if k == length:
                np = np + 1
                k = 0
        else:
            k = T[k]
            if k < 0:
                j = j + 1
                k = k + 1
    return np > 0

''' Esta funcion toma como parametros 2 cadenas (S,W) de longitud n
    y devuelve True sin son iguales. False caso contrario
    Complejidad algoritmica: O(2n)=O(n)
'''
def kmp_comp(S, W, length):
    np = 0
    j = 0
    k = 0
    T = kmp_tabla(W) #complejidad O(n)
    while j < length: #complejidad O(n)
        if W[k] == S[j]:
            j = j + 1
            k = k + 1
            if k == length:
                np = np + 1
                k = T[k]
        else:
            k = T[k]
            if k < 0:
                j = j + 1
                k = k + 1
    return np > 0

# Busca W en S
W = "DABRAABRACA"
S = "ABRACADABRA"
kmp(S,W)


W = "DABRAABRACA1"
S = "ABRACADABRA3"
kmp(S, W)

print(kmp_comp('AS', 'AS', len('AS')))

s = 'ABC'
s1 = 'BCA'

W = "DABRAABRACA"
S = "ABRACADABRA"
kmp_n(S, W)

W = "DABRAABRACA1"
S = "ABRACADABRA3"
kmp_n(S, W)