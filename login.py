from auth import authenticate

username = input("Digite o nome de usuário: ")
password = input("Digite a senha: ")
token = input("Digite o token: ")


tk = authenticate(username, password)

if tk:
    print("Autenticação bem sucedida. Seu token é:", token)
else:
    print("Nome de usuário ou senha inválidos.")
