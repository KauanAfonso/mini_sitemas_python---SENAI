produtos = [
    ["Arroz" , "Feijão" , "Macarrão"],
    [0, 10,8 ]
]


# # for i in range(len(produtos)):
# #     print("Produto" , i)
# #     for j in produtos:
# #         print("Quantidade" , j)
    
# # for i in range(len(produtos)):
# #     for j in range(len(produtos[i])):
# #       print(f"linha {i} e coluna {j}, {produtos[i][j]}")
      
# for i ,linha in enumerate(produtos):
#     for j, elemento in enumerate(linha):
#         print(f"linha {i} , {j} e elemento {elemento}")
        
#         if elemento == "Macarrão":
#             produtos[i + 1][j] = 500

# print(produtos)
    
# # print(produtos)


# def adicionar_produto():
    
#     nome = input("Qual é produto? ")
#     quantidade = int(input("Qual a quantidade de estoque ? "))
    
#     produtos[0].append((nome))
#     produtos[1].append((quantidade))
    
    
#     return "Adicionados com suceso !"


# print(adicionar_produto())
# print(produtos)


def remover_produto (produtos):
    
    contador_produto_na_lista = 0
    
    for i , linha in enumerate(produtos):
       print(f"linha {i}: {linha}")
       
    nome = input("Qual produto você quer remover? ")
    quantidade = int(input("Qual quantidade você removerá? "))
    
    for i ,linha in enumerate(produtos):
        for j, elemento in enumerate(linha):      
            if elemento == nome:
                estoque = produtos[i + 1][j]
                contador_produto_na_lista += 1
                if estoque >= quantidade:
                    produtos[i + 1][j] = estoque - quantidade
                    print("Estoque atualizado")
                    break
                else:
                    print("não possui estoque suficiente !")
            else:
                continue
   
    if contador_produto_na_lista == 0:
        print("PRODUTO NÃO ENCONTRADO")

    print(produtos)
 
remover_produto(produtos)

def altera_quantidade_produto():