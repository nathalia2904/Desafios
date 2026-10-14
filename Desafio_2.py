# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor:
# Exemplo:
# Você digitou o número : 10
# O sucessor dele é o número : 11
# O antecessor dele é o número : 9
numero = float(input('digite um numero :')) 
sucessor = numero + 1
antecessor = numero - 1
print(f'o numero que voce escolheu foi{numero:.2f} o sucessor dele e {sucessor:.2f} e o anrecessor dele e {antecessor:.2f}')