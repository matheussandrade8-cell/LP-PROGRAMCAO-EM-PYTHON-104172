import os
os.system("cls")


def verificar_login(login):
    nome=login
    return nome
def verificar_senha(senha):
    certificado=senha
    return certificado

login=input("digite o login:")
senha=input("digite a senha:")

verificarcao=verificar_login(login)
rv=verificar_senha(senha)
print(f"sua vefificação é {verificarcao} e sua senha é {rv}")