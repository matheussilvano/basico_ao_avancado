"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu primeiro nome: ')
letras_no_nome = len(nome)
nome_pequeno = letras_no_nome < 5
nome_normal = 4 < letras_no_nome < 7
if nome_pequeno:
    print(f'{letras_no_nome} letras? Seu nome é curto.')
elif nome_normal:
    print(f'{letras_no_nome} letras, seu nome é normal.')
else:
    print(f'{letras_no_nome} LETRAS?? Seu nome é muito grande')
