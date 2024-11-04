#Calculadora imc


def pedirDados():
    dado = float(input("Digite aqui: "))
    return dado 


def calculo(peso, altura):
    
    imc = peso / (altura * altura)
    
    print(imc)
    
    if imc < 18.5:
        situacao = "Baixo Peso"
    elif imc >= 18.5 and imc <=24.99:
        situacao = "Normal"
    elif imc >= 25 and imc < 29.99:
        situacao = "Sobrepeso"
    else:
        situacao = "Obesidade"
        
    return situacao



def imc():
    
    
    print("Digite seu peso: ")
    peso = pedirDados()
    print("Digite sua altura (ex: 1.80): ")
    altura = pedirDados()
    
    resultado = calculo(peso, altura)
    
    print(resultado)
  
  



def menu():
    while True:
        print('''
        
        
        Digite [1] - Calcular o imc
        Digite [2] - Para dois para SAIR
        
        
        ''')
        valor = int(input("Digite um número : "))
        if valor == 1:
            imc()
        else:
            break


menu()