# Faça um código que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = float(input('digite o seu salario atual :'))
aumento = salario * 0.15
novo_salario = salario + aumento
print(f'o seu salario atual é {salario:.2f} com aumento de 15% seu novo salario sera de R${novo_salario:.2f}')
# Exemplo de Resultado: O Seu salário atual é de R$1500,00 com o aumento de 15% seu novo salário será de R$1725,00