import random as r

contas = [

]




print(contas[1].index(0))

for i in contas:
    for j in i:
        print(j)
        
        
        
def mensagem_inicial():
    
    msg = '''
    
    Digite [1] - Logar
    Digite [2] - Criar Conta
    Digite [3] - Para dois para SAIR
    
    '''

    escolha = int(input(msg))
    
    return escolha




def mensagem_escolher_acao():
    
    msg = '''
    
    Digite [1] - Depositar
    Digite [2] - Sacar
    Digite [3] - Verificar Saldo
    Digite [4] - Para dois para SAIR
    

    '''

    escolha = int(input(msg))
    
    return escolha
    



def abrir_conta():

    num_conta = r.randint(1000, 9999)
    print(f"Sua conta é {num_conta} ")
    senha = input("Digite sua senha: ")
    
    lista = []
    saldo = 0
    
    lista.append(num_conta)
    lista.append(senha)
    lista.append(saldo)
    
    
    contas.append(lista)
    


def pedir_valor():
    
    valor = float(input("Digite o aqui: "))
    
    return valor







def login(conta,senha):
    

    contador = 0
    
    for i in contas:
        for j in i:
            if j == conta or j == senha:
                contador+=1
    
    return contador #Se contador for igual a 2 é porque ele logou corretamente
            
    
    
def depositar(conta):
        
    valor = pedir_valor()
    posicao = 0
    
    for i in range(len(contas)):
        if contas[i][0] == conta:
            posicao = i
            break
    
    contas[posicao][2] += valor
    
    
    return contas[posicao][2]
    
    

def saque(conta):
             
    
    valor = pedir_valor()
    posicao = 0
    
    for i in range(len(contas)):
        if contas[i][0] == conta:
            posicao = i
            break
    
   
    
    if valor <= contas[posicao][2]: 
        contas[posicao][2] -= valor
    else:
        print("VOCE NÂO TEM SALDO PARA SACAR !!")
    
    return contas[posicao][2]


def verificar_saldo(conta):
    
    for i in range(len(contas)):
        if contas[i][0] == conta:
            posicao = i
            break
                

    saldo = contas[posicao][2] 
    
    print(f"Seu saldo e de: {saldo}")
    
    


def menu():
    while True:
        escolha = mensagem_inicial()
        if escolha == 1:
            conta = int(input("Digite sua conta: "))
            senha = input ("Digite sua senha: ")         
            contador_login = login(conta, senha)
            if contador_login == 2:
                while True:
                    escolha = mensagem_escolher_acao()
                    if escolha == 1 :
                        depositar(conta)
                        print(contas)
                    elif escolha == 2:
                        saque(conta)
                    elif escolha == 3:
                        verificar_saldo(conta)
                    else:
                        print("Log out...")
            else:
                print("Credenciais inválidas")
        elif escolha == 2:
            abrir_conta()
        else:
            print("Você saiu ...")
            break
            
    
    
# def verificar_saldo():

menu()
