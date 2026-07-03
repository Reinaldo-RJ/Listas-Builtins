def maior_sequencia_crescente(lista):

    if not lista:
        return []
    
    maior_seq = [lista[0]]
    seq_atual = [lista[0]]

    for i in range(1, len(lista)):
        
        if lista[i] > lista[i - 1]:
            seq_atual.append(lista[i])
        else:
            
            if len(seq_atual) > len(maior_seq):
                maior_seq = seq_atual[:] 
            
            seq_atual = [lista[i]]
   
    if len(seq_atual) > len(maior_seq):
        maior_seq = seq_atual
    return maior_seq

numeros = [3, 5, 7, 2, 4, 6, 8, 1, 9]
resultado = maior_sequencia_crescente(numeros)
print(resultado)

print(maior_sequencia_crescente([1, 2, 3, 4]))
print(maior_sequencia_crescente([5, 4, 3, 2]))
print(maior_sequencia_crescente([1, 3, 5, 2, 4, 6]))