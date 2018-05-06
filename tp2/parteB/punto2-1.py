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
    np = 0
    j = 0
    k = 0
    T = kmp_tabla(W)
    tamanio = len(S)
    rotacion = False
    while j < tamanio and not rotacion:
        if W[k] == S[j]:
            j = j + 1
            k = k + 1
            if k == tamanio:
                np = np + 1
                k = T[k]
            str_tmp = W[k:] + W[:k]
            if (str_tmp == S):
                rotacion = True
        else:
            k = T[k]
            if k < 0:
                j = j + 1
                k = k + 1
    if rotacion:
        print(W + " es una rotacion ciclica de " + S)
    else:
        print(W + " no es una rotacion ciclica de " + S)

# Busca W en S
W = "DABRAABRACA"
S = "ABRACADABRA"
#kmp(S, W)
kmp_tabla("")