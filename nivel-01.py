produtos = []

while True:
    nome = input("Digite o nome do produto (ou 'sair' para encerrar): ")

    if nome.lower() == "sair":
        break

    preco = float(input("Digite o preço do produto: R$ "))

    produtos.append([nome, preco])

if len(produtos) > 0:

    soma_precos = 0
    mais_de_100 = 0

    produto_mais_caro = produtos[0][0]
    maior_preco = produtos[0][1]

    for produto in produtos:
        nome = produto[0]
        preco = produto[1]

        soma_precos += preco

        if preco > 100:
            mais_de_100 += 1

        if preco > maior_preco:
            maior_preco = preco
            produto_mais_caro = nome

    media = soma_precos / len(produtos)

    print(f"Total de produtos cadastrados: {len(produtos)}")
    print(f"Produto mais caro: {produto_mais_caro} (R$ {maior_preco:.2f})")
    print(f"Média dos preços: R$ {media:.2f}")
    print(f"Produtos acima de R$100: {mais_de_100}")

else:
    print("Nenhum produto foi cadastrado.")