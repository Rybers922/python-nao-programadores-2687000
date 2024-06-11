# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
estudante = {}
estudante['nome'] = input('Qual o seu nome?')
estudante['ano_conheceu_linkedin'] = int (input('Quando conheceu o Linkedin'))
estudante['ano_atual'] = int (input('Em qual ano estamos?'))

cursos = input('Quais cursos você já fez no Linkedin Learning? (separe-os com virgula)  ')

estudante['cursos'] = cursos.split(',  ')

# 2. Armazene esses dados em um dicionário
# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.


total_anos = estudante['ano_atual'] - estudante['ano_conheceu_linkedin']
total_cursos = len(estudante['cursos'])

print(f"Oi {estudante['nome']}, desde {estudante['ano_conheceu_linkedin']} você conhece o LinkedIn. Nesses {estudante['ano_atual'] - estudante['ano_conheceu_linkedin']} anos, você realizou {len(estudante['cursos'])} cursos, sendo o primeiro curso '{estudante['cursos'][0]}' e último '{estudante['cursos'][-1]}'.")