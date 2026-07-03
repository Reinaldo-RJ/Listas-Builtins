def remover_duplicados(lista):
    lista_limpa = []
    
    for elemento in lista:
       if elemento not in lista_limpa:
            lista_limpa.append(elemento)
            
    return lista_limpa


entrada = [4, 2, 7, 2, 9, 4, 1, 7]
saida = remover_duplicados(entrada)

print(saida)

print(remover_duplicados([1, 1, 1, 1]))
print(remover_duplicados([5, 3, 5, 2, 3]))