itens_do_cardapio = ['pastel', 'pizza', 'coxinha']

# Acrescenta o refrigerante à lista existente
itens_do_cardapio.append('refrigerante')

pedido = input("O que você quer comer hoje? ")

if pedido in itens_do_cardapio:
    print(f"Saindo um(a) {pedido}!")
else:
    print(f"{pedido} não está no cardápio, que tal você pedir {itens_do_cardapio}?")

# Remove a pizza da lista
itens_do_cardapio.remove("pizza")

print(itens_do_cardapio)

# Sua lista inicial
cardapio = ['pizza', 'pastel', 'coxinha']

# Inserindo 'refrigerante' na primeira posição (índice 0)
cardapio.insert(0, 'refrigerante')

# Inserindo 'suco' na terceira posição (índice 2)
cardapio.insert(2, 'suco')

# Resultado esperados
print(cardapio)
