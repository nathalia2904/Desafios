# Faça um programa que leia um número inteiro qualquer
# e mostre na tela a sua tabuada
# Exemplo:
# Você digitou o número : 10
# --------------- Tabuada do 10 ------------------
# 10 X 0 = 0
# 10 X 1 = 10
# E assim sucessivamente....
numero = int(input('digite um numero :')) 
print(f'-' * 30)
print(f'tabuada do numero {numero}')
print(f'-' *30)

for i in range(11):
    print(f'{numero} x {i} ={numero * i}')
