print("=== CADASTRO DE USUÁRIO ===") # Imprime um título para o cadastro de usuário

nome = input("Digite seu nome: ") # Solicita ao usuário que digite seu nome e armazena na variável nome
sobrenome = input("Digite seu sobrenome: ") # Solicita ao usuário que digite seu sobrenome e armazena na variável sobrenome
cidade = input("Digite a cidade onde você mora: ") # Solicita ao usuário que digite a cidade onde mora e armazena na variável cidade
estado = input("Digite o estado onde você mora: ") # Solicita ao usuário que digite o estado onde mora e armazena na variável estado
profissao = input("Digite sua profissão: ") # Solicita ao usuário que digite sua profissão e armazena na variável profissao
idade = int(input("Digite sua idade: ")) # Solicita ao usuário que digite sua idade, converte para inteiro e armazena na variável idade
altura = float(input("Digite sua altura (em metros): ")) # Solicita ao usuário que digite sua altura, converte para float e armazena na variável altura
peso = float(input("Digite seu peso (em kg): ")) # Solicita ao usuário que digite seu peso, converte para float e armazena na variável peso

print("=== DADOS CADASTRAIS ===")  # Imprime um título para os dados cadastrais
print(f"Nome: {nome}") # Imprime o nome do usuário
print(f"Sobrenome: {sobrenome}") # Imprime o sobrenome do usuário
print(f"Cidade: {cidade}") # Imprime a cidade onde o usuário mora
print(f"Estado: {estado}") # Imprime o estado onde o usuário mora
print(f"Profissão: {profissao}") # Imprime a profissão do usuário
print(f"Idade: {idade} anos") # Imprime a idade do usuário
print(f"Altura: {altura} m") # Imprime a altura do usuário
print(f"Peso: {peso} kg") # Imprime o peso do usuário

"""
print (f"Nome: {nome}") # Imprime o nome do usuário
print (type(nome)) # Imprime o tipo da variável nome
print (f"Sobrenome: {sobrenome}") # Imprime o sobrenome do usuário
print (type(sobrenome)) # Imprime o tipo da variável sobrenome
print (f"Cidade: {cidade}") # Imprime a cidade onde o usuário mora
print (type(cidade)) # Imprime o tipo da variável cidade
print (f"Estado: {estado}") # Imprime o estado onde o usuário mora
print (type(estado)) # Imprime o tipo da variável estado
print (f"Profissão: {profissao}") # Imprime a profissão do usuário
print (type(profissao)) # Imprime o tipo da variável profissão
print (f"Idade: {idade} anos") # Imprime a idade do usuário
print (type(idade)) # Imprime o tipo da variável idade
print (f"Altura: {altura}") # Imprime a altura do usuário
print (type(altura)) # Imprime o tipo da variável altura
print (f"Peso: {peso}") # Imprime o peso do usuário
print (type(peso)) # Imprime o tipo da variável peso
"""
