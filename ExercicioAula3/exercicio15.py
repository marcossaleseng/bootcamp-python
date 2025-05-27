"""Objetivo: Processar itens de uma lista até encontrar um valor específico que indica a parada. Processar até o usuário inserir informações corretas"""
itens = [1, 2,3, "parar", 4,5]

i = 0
while i < len(itens):
    if itens[i] == "parar":
        print("Critério de parada encontrado")
        break
    #processar o item
    print(f"Processando o item: {itens[i]}")
    i += 1

