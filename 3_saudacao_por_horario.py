"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario_str = input('Digite o horário: ')

try:
    horario = int(horario_str)
    manha = -1 < horario < 12
    tarde = 11 < horario < 18
    noite = 18 < horario < 24
    if manha:
        print('Bom dia!')
    elif tarde:
        print('Boa tarde!')
    elif noite:
        print('Boa noite!')
    else:
        print('Este horário não é valido.')
except:
    print('Digite um número.')
  
