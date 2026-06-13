print("FICHA DE CADASTRO SIMPLES:")  # Imprime um título para o cadastro de usuário
print("-" * 33)  # Imprime uma linha de separação usando o operador de multiplicação para repetir o caractere "-" 33 vezes

nome =input("Digite seu nome: ") # Solicita ao usuário que digite seu nome e armazena na variável 'nome'
sobrenome = input("Digite seu sobrenome: ") # Solicita ao usuário que digite seu sobrenome e armazena na variável 'sobrenome'
cidade = input("Qual o nome da sua cidade? ") # Solicita ao usuário que digite o nome da sua cidade e armazena na variável 'cidade'
estado = input("Digite o Estado onde você mora: (ex: SP, CE, RJ, MG) ") # Solicita ao usuário que digite o estado onde mora, fornecendo um exemplo de formato (sigla do estado) e armazena na variável 'estado'
idade = int(input("Digite sua idade: ")) # Solicita ao usuário que digite sua idade, converte a entrada para um número inteiro e armazena na variável 'idade'
telefone = input("Digite seu número de telefone: ") # Solicita ao usuário que digite seu número de telefone e armazena na variável 'telefone'
profissao = input("Qual a sua profissão? ") # Solicita ao usuário que digite sua profissão e armazena na variável 'profissao'
altura = float(input("Qual a sua altura? ")) # Solicita ao usuário que digite sua altura, converte a entrada para um número de ponto flutuante e armazena na variável 'altura'
email = input("Digite seu melhor E-mail: ") # Solicita ao usuário que digite seu e-mail e armazena na variável 'email'
endereco = input("Digite seu endereço completo: ") # Solicita ao usuário que digite seu endereço completo e armazena na variável 'endereco'
hobbies = input("Quais são os seus hobbies? (Digite separando por vírgula) ") # Solicita ao usuário que digite seus hobbies, separados por vírgula, e armazena na variável 'hobbies'

print("\nCADASTRO REALIZADO COM SUCESSO!") # Imprime um título para os dados cadastrados, indicando que as informações a seguir são os dados fornecidos pelo usuário
print("-" * 33)  # Imprime uma linha de separação usando o operador de multiplicação para repetir o caractere "-" 33 vezes

print(f"Nome completo: {nome} {sobrenome}") # Imprime o nome completo do usuário usando f-string para formatar a saída, concatenando o nome e sobrenome com um espaço entre eles
print(f"Cidade: {cidade}") # Imprime a cidade do usuário
print(f"Estado: {estado}") # Imprime o estado onde o usuário mora
print(f"Idade: {idade} anos") # Imprime a idade do usuário usando f-string para formatar a saída, adicionando " anos" para indicar a unidade de medida
print(f"Telefone: {telefone}") # Imprime o número de telefone do usuário
print(f"Profissão: {profissao}") # Imprime a profissão do usuário
print(f"Altura: {altura} m") # Imprime a altura do usuário usando f-string para formatar a saída, adicionando " m" para indicar a unidade de medida
print(f"E-mail: {email}") # Imprime o e-mail do usuário
print(f"Endereço: {endereco}") # Imprime o endereço do usuário
print(f"Hobbies: {hobbies}") # Imprime a lista de hobbies do usuário, mostrando cada hobby separado por vírgula
