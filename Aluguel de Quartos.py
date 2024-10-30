usuario = {}

print('''           Bem vindo ao cadastro !
-----------------Cadastro-----------------''')

usuario["Nome"] = input("Diga seu nome: ")
usuario["Login"] = input("Declare um usuario: ")
usuario["Senha"] = input("Declare uma senha: ")

produtos = {
    "1": ["Simples", 100.00],
    "2": ["Duplo" , 150.00],
    "3" : ["Luxo", 250.00]
}

print('''--------Olá ! Bem-vindo.--------
Para acessar os quartos, preciso que você me informe:''')

login = input("Usuario: ")
senha = input("Senha: ")

carrinho = []
total = 0

if usuario["Login"] == login and usuario["Senha"] == senha:
    produto1 = input(f'''{produtos}
Diga o QUARTO desejado: ''')
    dias = int(input('''Quantos dias deseja ficar?
: '''))
    if produto1 == "1":
        carrinho.append(produtos[produto1][0])
        total = dias * (produtos[produto1][1])
        print(f"Você alugou o quarto:{carrinho} com o valor de R${total}")

        pagamento = input(f'''Qual a formade pagamento?
Crédito ou Débito: ''')
        print(f'''Seu pagamento será feito em {pagamento}, sendo o valor de {total} e seu quarto é: {carrinho}''')
    

    if produto1 == "2":
        carrinho.append(produtos[produto1][0])
        total = dias * (produtos[produto1][1])
        print(f"Você alugou o quarto:{carrinho} com o valor de R${total}")

        pagamento = input(f'''Qual a formade pagamento?
Crédito ou Débito: ''')
        print(f'''Seu pagamento será feito em {pagamento}, sendo o valor de {total} e seu quarto é: {carrinho}''')

    if produto1 == "3":
        carrinho.append(produtos[produto1][0])
        total = dias * (produtos[produto1][1])
        print(f"Você alugou o quarto:{carrinho} com o valor de R${total}")

        pagamento = input(f'''Qual a formade pagamento?
Crédito ou Débito: ''')
        print(f'''Seu pagamento será feito em {pagamento}, sendo o valor de {total} e seu quarto é: {carrinho}''')

else:
    print("Sua senha está incorreta")