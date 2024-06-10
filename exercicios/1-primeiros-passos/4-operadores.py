ano_nascimento = 1989
ano_formatura = 2010

# Considerando que as variáveis acima correspondem a 'Gerlaine', descubra a idade dela no ano da sua formatura
  
hoje = ano_formatura
nascimento = ano_nascimento
hoje - nascimento
f'Gerlaine tem {hoje - nascimento} de idade'

# Escreva expressões comparativas usando os operadores relacionais >, <= e ==. Imprima na tela as respostas
hoje <= nascimento
ano_formatura > ano_nascimento

print (hoje > ano_nascimento)
print (hoje <= ano_nascimento)
print (hoje == ano_nascimento)

# Crie expressões comparativas mais complexas utilizando operadores lógicos and, or e not. Imprima na tela as respostas

hoje > ano_nascimento and hoje == nascimento
hoje <= ano_formatura or ano_nascimento > hoje