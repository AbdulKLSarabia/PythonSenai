produtos = {
    'banana': {'preco': 2.50, 'quantidade': 10},
    'maça': {'preco': 3.00, 'quantidade': 15},
    'laranja': {'preco': 2.20, 'quantidade': 12}
}

print(f"{'Produto':<10} {'Preço':<10} {'Quantidade':<10}")
print("-" * 35)

for produto, info in produtos.items():
    preco = info['preco']
    quantidade = info['quantidade']
    print(f"{produto:<10} R${preco:.2f} {quantidade:>10}")