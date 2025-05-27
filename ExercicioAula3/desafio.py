"""Refatorar o exercício da aula 1, porém usando while"""
nome = 'iniciador'

# verificar nome válido
while True:
    try:
        nome = str(input("Digite seu nome: "))
        if nome.isdigit():
            raise ValueError("Você digitou um número em vez de um nome!")
        elif len(nome) == 0:
            raise ValueError("Você não digitou o nome.")
        elif nome.isspace():
            raise ValueError("Você digitou apenas o espaço.")
        else:
            print("Nome Válido", nome)
            break
    except ValueError as e:
        print(e)

# Validador de salário
salario_valido = False
while not salario_valido:
    try:
        salario = float(input("Digite seu salario, sendo . o caractere separador: "))
        if salario <= 0:
            raise ValueError("Salário deve ser > 0")
        else:
            print("Salario válido")
            salario_valido = True
    except ValueError as e:
        print("Ajeita esse número aí, por favor")

#Validador de bônus
bonus_valido = False
while not bonus_valido:
    try:
        bonus = float(input("Digite o seu multiplicador de bônus, sendo . o caractere separador: "))
        if bonus <= 0:
            raise ValueError("Salário deve ser > 0")
        else:
            print("Salario válido")
            bonus_valido = True
    except ValueError as e:
        print("Ajeita esse número aí, por favor")

kpi = 1000 + salario*bonus
print(f"Parabéns {nome}, seu bônus foi de {kpi} que é {kpi/salario} vezes maior que seu salário mensal")