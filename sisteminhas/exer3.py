dicionario = {"milimetro": 1, 'centimitro':2, 'decimetro':3, 'metro':4, 'decâmetro':5, 'hectômetro':6, 'quilômetro':71}


def mensagem():
    
    '''
    FUNÇAÕ PARA PRINTAR A MENSAGEM INICIAL
    
    '''

    msg = '''

    Digite [1] - Jogar
    Digite [2] - Para dois para SAIR

    '''

    resposta = int(input(msg))
    return resposta

def Enviar_e_mensagem_De_Medidas():
    
    
    '''
    FUNÇAÕ PARA PRINTAR O QUE O USUARIO PODE ESCOLHER
    
    '''
    
    
    
    msg = '''

    Digite [1] - milimetro
    Digite [2] - centimetro
    Digite [3] - decimetro
    Digite [4] - metro
    Digite [5] - decametro
    Digite [6] - hectometro
    Digite [7] - quilômetro


    '''

    resposta = int(input(msg))
    return resposta 



def percorrerMedidadas(num_inicial:int , num_final:int, valor):

    if num_inicial > num_final :
        
        for i in range(num_inicial , num_final , -1):
            valor *= 10
            
    elif num_inicial < num_final :
        
        for j in range(num_inicial, num_final, 1):
            valor /=10
            
    return valor

 
def pedir_valor():
    valor = int(input("Qual será o valor?: "))
    return valor



def menu():
    
    while True:
        
        escolha = mensagem()
        
        if escolha == 2:
            print("Você saiu...")
            break
                
        print('Escolha sua media inicial: ')
        medida_inicial = Enviar_e_mensagem_De_Medidas()
        medida_final = Enviar_e_mensagem_De_Medidas()
        valor = pedir_valor()
        resposta = percorrerMedidadas(medida_inicial, medida_final, valor)
        print(f"Seu resultado convertido ficará em : {resposta}")
        


menu()    
        
    
    



