usuario = {}

print('''          Bem vindo ao cadastro !
-----------------Cadastro-----------------''')

usuario["Nome"] = input("Diga seu nome: ")
usuario["Login"] = input("Declare um usuario: ")
usuario["Senha"] = input("Declare uma senha: ")

produtos = {
    "1": ["Shampoo de piolho",20.00],
    "2": ["Pente fino" , 15.00],
    "3" : ["Permetrina", 31.69],
    "4" : ["Spray de piolho", 40.00],
}

print('''--------Olá ! Bem-vindo ao nosso mercado.--------
    Para acessar os produtos, preciso que você me informe:''')

login = input("Usuario: ")
senha = input("Senha: ")

carrinho = []
total = 0

if usuario["Login"] == login and usuario["Senha"] == senha:
    produto1 = input(f'''{produtos}
Diga o código do produto: ''')

    if produto1:
        carrinho.append(produtos[produto1][0])
        total += produtos[produto1][1]
        print(f"Você tem em seu carrinho o item: {carrinho} com o valor de R${total}")
    comprar = input('''Deseja comprar mais alguma coisa?
Sim / Não : ''')

    if comprar == "Sim":
        produto2 = input(f'''{produtos}
Diga o código do produto: ''')
    if produto2:
        carrinho.append(produtos[produto2][0])
        total += produtos[produto2][1]
        print(f"Você tem em seu carrinho o item: {carrinho} com o valor de R${total}")
    comprar = input('''Deseja comprar mais alguma coisa?
Sim / Não : ''')

    if comprar == "Sim".lower:
        produto3 = input(f'''{produtos}
Diga o código do produto: ''')
    if produto3:
        carrinho.append(produtos[produto3][0])
        total += produtos[produto3][1]
        print(f"Você tem em seu carrinho o item: {carrinho} com o valor de R${total}")

        print(f'''Infelizmente teremos que fechar o seu carrinho, ficamos sem produtos...''')

        print("Qual a forma de pagamento?")
        pagamento = input(f'''Qual a formade pagamento?
Crédito ou Débito: ''')
        print(f'''Seu pagamento será feito em {pagamento}, sendo o valor de {total} e seus produtos são {carrinho}''')

    elif comprar == 'Não'.lower:
        print("Qual a forma de pagamento?")
        pagamento = input(f'''Qual a formade pagamento?
Crédito ou Débito: ''')
        print(f'''Seu pagamento será feito em {pagamento}, sendo o valor de {total} e seus produtos são {carrinho}''')
    