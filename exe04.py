alunos = [
    ["Bruno", [10, 8, 9]],
    ["Rafael", [4, 7, 9]],
    ["Carlos", [10, 10, 9]],
]

aprovados = []
recuperacao = []
reprovados = []

for aluno in alunos:
    nome = aluno[0]
    notas = aluno[1]

    media = sum(notas) / len(notas)
    
    media_arredondada = round(media, 1)
    
    dados_aluno = [nome, media_arredondada]
    
    if media_arredondada >= 7:
        aprovados.append(dados_aluno)
        
    elif 5 <= media_arredondada < 7:
        recuperacao.append(dados_aluno)
        
    else:
        reprovados.append(dados_aluno)

print("Aprovados:", aprovados)
print("Recuperação:", recuperacao)
print("Reprovados:", reprovados)