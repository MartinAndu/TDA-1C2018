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

def kmp(S,W):
    np = 0
    j = 0
    k = 0
    T = kmp_tabla(W) #complejidad O(n)
    lenS = len(S)
    lenW = len(W)
    P = [0]*len(S)
    while j < lenS: #complejidad O(n)
        if W[k] == S[j]:
            j = j + 1
            k = k + 1
            if k == lenW:
                np = np + 1
                k = T[k]
        else:
            k = T[k]
            if k < 0:
                j = j + 1
                k = k + 1
    return (P, np)

def es_rotacion_ineficiente(S,W):
    if len(S) != len(W):
        return False
    for k in range(len(W)):
        str_tmp = W[k:] + W[:k]
        (P, np) = kmp(S, str_tmp)
        if P[0] == 0:
            return True

    return False

def es_rotacion_eficiente(S,W):
    if len(S) != len(W):
        return False
    str_tmp = W + W
    (P, np) = kmp(S, str_tmp)
    if P[0] == 0:
        return True
    return False


W = "DABRAABRACA"
S = "ABRACADABRA"
print(es_rotacion_eficiente(S,W))
print(es_rotacion_ineficiente(S,W))


W = "DABRAABRACA1"
S = "ABRACADABRA3"
print(es_rotacion_eficiente(S,W))
print(es_rotacion_ineficiente(S,W))
