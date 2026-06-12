print("=== CADASTRO DE USUÁRIO ===")  # Imprime um título para o cadastro de usuário

nome =input("Digite seu nome: ") # Solicita ao usuário que digite seu nome e armazena na variável 'nome'
sobrenome = input("Digite seu sobrenome: ") # Solicita ao usuário que digite seu sobrenome e armazena na variável 'sobrenome'
idade = int(input("Digite sua idade: ")) # Solicita ao usuário que digite sua idade, converte a entrada para um número inteiro e armazena na variável 'idade'
cidade = input("Qual o nome da sua cidade? ") # Solicita ao usuário que digite o nome da sua cidade e armazena na variável 'cidade'
estado = input("Digite o Estado onde você mora: ") # Solicita ao usuário que digite o estado onde mora e armazena na variável 'estado'
profissao = input("Qual a sua profissão? ") # Solicita ao usuário que digite sua profissão e armazena na variável 'profissao'
altura = float(input("Qual a sua altura? ")) # Solicita ao usuário que digite sua altura, converte a entrada para um número de ponto flutuante e armazena na variável 'altura'
email = input("Digite seu melhor e-mail: ") # Solicita ao usuário que digite seu e-mail e armazena na variável 'email'
hobbies = input("Quais são os seus hobbies? (Digite separando por vírgula) ") # Solicita ao usuário que digite seus hobbies, separados por vírgula, e armazena na variável 'hobbies'

print("\n=== DADOS CADASTRADOS ===") # Imprime um título para os dados cadastrados, indicando que as informações a seguir são os dados fornecidos pelo usuário
# print(f"Nome: {nome}") # Imprime o nome do usuário
# print(f"Sobrenome: {sobrenome}") # Imprime o sobrenome do usuário
print(f"Idade: {idade} anos") # Imprime a idade do usuário usando f-string para formatar a saída, adicionando " anos" para indicar a unidade de medida
print(f"Cidade: {cidade}") # Imprime a cidade do usuário
print(f"Estado: {estado}") # Imprime o estado onde o usuário mora
print(f"Profissão: {profissao}") # Imprime a profissão do usuário
print(f"Altura: {altura} m") # Imprime a altura do usuário usando f-string para formatar a saída, adicionando " m" para indicar a unidade de medida
print(f"E-mail: {email}") # Imprime o e-mail do usuário
print(f"Hobbies: {hobbies}") # Imprime a lista de hobbies do usuário, mostrando cada hobby separado por vírgula
