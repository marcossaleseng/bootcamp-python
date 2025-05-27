
"""Esse arquivo recebe
nome
salario (separado pelo caractere .)
bônus (separado pelo caractere .)

Esse arquivo vai com o retorno de qual é o kpi de bônus e quantas vezes
o kpi é maior que o salário mensal"""

nome = str(input("Digite seu nome: "))
salario = float(input("Digite seu salario, sendo . o caractere separador"))
bonus = float(input("Digite o seu multiplicador de bônus, sendo . o caractere separador: "))

kpi = 1000 + salario*bonus
print(f"Parabéns {nome}, seu bônus foi de {kpi} que é {kpi/salario} vezes maior que seu salário mensal")
