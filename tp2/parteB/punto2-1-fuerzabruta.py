def rotacion_fuerza_bruta(S2, S1):
    if len(S1) != len(S2):
        return
    tamanio = len(S1)
    es_rotacion = False
    
    for i in range(tamanio): # Complejidad de este ciclo: O(n)
        s_temp = S2[i:]
        s_temp = s_temp + S2[0:i]
        print("s1_temp: " + s_temp)
        # https://www.quora.com/What-is-the-time-complexity-of-checking-if-two-strings-are-equal-in-Python
        if s_temp == S1: # peor caso O(n)
            es_rotacion = True
            break
            
    if es_rotacion:
        print(S2 + " es una rotacion ciclica de " + S1)
    else:
        print(S2 + " no es una rotacion ciclica de " + S1)
