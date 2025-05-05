codigo = int(input("selecione o número do código: "))
valor = float(input("Digite o valor: "))

if codigo == 1:
    dinheiro = valor * 0.9
    print(f"À vista em dinheiro ou Pix recebe 10% de desconto: {dinheiro}")
elif codigo == 2:
    dinheiro = valor * 0.95
    print(f"À vista  no cartão de crédito, recebe 5% de desconto: {dinheiro}")
elif codigo == 3:
    parcelas = valor / 2
    print(f"Em duas vezes, preço normal de etiqueta sem juros: {parcelas}")
elif codigo == 4:
    dinheiro = valor * 1.1
    parcelas = dinheiro / 3
    print(f"Em três vezes, preço normal de etiqueta mais juros de 10%: {parcelas} aumento de {dinheiro}")
else:
    print("código inválido!")
