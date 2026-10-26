# Correção das variáveis
itens_de_comida_do_cardapio = ['pizza', 'bolo', 'salgado', 'hamburguer']
itens_de_bebida_do_cardapio = ['suco', 'refrigerante', 'agua', 'cafe']

# 1. Pegar os dois primeiros itens de comida ('pizza' e 'bolo')
primeiros_comida = itens_de_comida_do_cardapio[0:2]
print(primeiros_comida)  # Saída: ['pizza', 'bolo']

# 2. Pegar do segundo elemento em diante das bebidas ('refrigerante', 'agua', 'cafe')
bebidas_a_partir_do_segundo = itens_de_bebida_do_cardapio[1:]
print(bebidas_a_partir_do_segundo)  # Saída: ['refrigerante', 'agua', 'cafe']

# 3. Pegar os dois últimos itens de comida usando índices negativos ('salgado', 'hamburguer')
ultimos_comida = itens_de_comida_do_cardapio[-2:]
print(ultimos_comida)  # Saída: ['salgado', 'hamburguer']


# Somando as duas listas para juntar todos os itens
cardapio_completo = itens_de_comida_do_cardapio + itens_de_bebida_do_cardapio

print(cardapio_completo)
