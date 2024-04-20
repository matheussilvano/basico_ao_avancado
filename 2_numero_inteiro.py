"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um número inteiro: ')
numero_inteiro = numero.isdigit()
if numero_inteiro:
    str_em_int = int(numero)
    numero_par = str_em_int % 2 == 0
    if numero_par:
            print(f'O número {numero} é par.')
    else:
            print(f'O número {numero} é ímpar.')
else:
    print('O valor informado não é um número inteiro.')
