import random as r

def mensagem():
    
    resposta = int(input('''
    
    
    Digite [1] - Jogar
    Digite [2] - Para dois para SAIR
    
    
    '''))
    
    return resposta
    
    
    
def girarODado (nDeLados):
    
    aleatorio = r.randint(1,nDeLados)
    return aleatorio

# def somaTotaldosDados(numeroDoDado):
#     i += numeroDoDado
#     return i 
    

       
def jogo():
    
    try: 
        numDelados = int(input("Digite o número de lados: "))
        vezes = int (input("Quantas vezes jogara o dado? "))
        i = 1
        somador = 0
        
        
        while i <= vezes:
            
            girar_Dado = girarODado(numDelados)
            print(f"O dado caiu em {girar_Dado} ") 
            somador +=girar_Dado
            
            i+=1
            
        print(f"A Soma dos dados é de {somador}")
    except:
        print("Digite corretamente !")
    


def menu():
    
    while True:
        respostaUsuario = mensagem()
        if respostaUsuario == 1:
            jogo()            
        else:
            print('voce saiu...')
            break
   
        

menu()