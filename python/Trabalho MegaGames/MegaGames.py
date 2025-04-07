#UMC - CRUD
#Nomes: Ana Caroline Suzart da Silva / Guilherme Pereira de Sousa Santos/Sophia Luna da Silva Rocha 
#RGM: 11242101001 / 11242502182 / 11242502182 DATA: 02/12/2024

import os
import time
import textwrap
from tkinter import *

# Função para criar mensagens formatadas com bordas
def criar_mensagem(texto, largura=60):
    borda_superior = '╔' + '═' * (largura + 2) + '╗'
    borda_inferior = '╚' + '═' * (largura + 2) + '╝'
    texto_formatado = textwrap.fill(texto, largura)
    linhas = texto_formatado.split('\n')
    linhas_com_margem = [f'║ {linha.ljust(largura)} ║' for linha in linhas]
    return '\n'.join([borda_superior] + linhas_com_margem + [borda_inferior])

# Função para checar o produto na lista (por código)
def chk_mat(matricula, Lista):
    for i, db in enumerate(Lista):
        if db[0] == matricula:
            return i
    return None  # Retorna None se o produto não for encontrado

# Função para carregar dados de um arquivo de texto Loja
def Load_Txt(filename, Lista):
    with open(filename, 'r') as Dados:
        for i in Dados:
            Lista.append(i.rstrip().split(","))
    return Lista

# Função para salvar dados em um arquivo de texto Loja
def Save_Txt(Lista, filename):
    with open(filename, "w") as RT:
        for dados in Lista:
            RT.write(f"{dados[0]},{dados[1]},{dados[2]},{dados[3]},{dados[4]}\n")

# Função para transferir produto entre a loja e o estoque
def transferir_produto(codigo, quantidade, origem, destino):
    # Verificar se o código do produto existe em ambos os locais
    index_origem = chk_mat(codigo, origem)
    index_destino = chk_mat(codigo, destino)
    
    if index_origem is None:
        print("Produto não encontrado no local de origem.")
        return False
    if index_destino is None:
        print("Produto não encontrado no local de destino.")
        return False
    
    # Verificar se há quantidade suficiente no local de origem
    estoque_origem = int(origem[index_origem][2])  # Quantidade no local de origem
    
    if estoque_origem < quantidade:
        print("Quantidade insuficiente no local de origem.")
        return False
    
    # Atualizar a quantidade nos dois locais
    origem[index_origem][2] = str(estoque_origem - quantidade)
    
    # Atualizar a quantidade no local de destino
    estoque_destino = int(destino[index_destino][2])  # Quantidade no local de destino
    destino[index_destino][2] = str(estoque_destino + quantidade)
    
    print(f"Transferência de {quantidade} unidades do produto {codigo} realizada com sucesso!")
    return True


# Função principal que gerencia o sistema
def main():
    L1 = []  # Lista da loja
    E1 = []  # Lista de estoque

    # Carregar os dados das listas L1 e E1
    L1 = Load_Txt("L1.txt", L1)
    E1 = Load_Txt("E1.txt", E1)

    os.system("cls")
    while True:
        
        os.system("cls")
        print(criar_mensagem("Mega Games - Sistema Operacional", 50))
        Menu = input(criar_mensagem('''Entre com a opção desejada:                      
[1] Loja                                           
[2] Estoque                                        
[3] Sair
''', 50))

        if Menu not in ["1","2","3"]:
            input("Opção inválida - pressione enter para voltar ao menu ")
            continue

        # Menu Loja
        if Menu == "1":
            opt1 = input(criar_mensagem('''Loja MegaGame Estoque                                                        
Escolha uma das opções:                                                                           

[1] Consultar Produto:                                                     
[2] Atualizar Produto:                           
[3] Adicionar Produto:                                
[4] Remover Produto:                                                                 
[5] Relatorio Produtos:                                      
[6] Transferir Produto:                                        
[7] Voltar ao Menu:                                  
[8] Salvar/Sair           

''', 50))

            if opt1 not in ["1", "2", "3", "4", "5", "6", "7","8"]:
                input("Opção inválida - pressione enter para voltar ao menu ")
                continue

            elif opt1 == "1":  # Consultar Produto
                
                os.system("cls")
                print(criar_mensagem("Produtos Disponíveis - Loja", 50))
                for db in L1:
                    print(f"Código: {db[0]}, Nome: {db[1]}, Quantidade: {db[2]}, Valor Atacado: R${db[3]}, Valor Final: R${db[4]}")
                input("Pressione enter para continuar...")

            elif opt1 == "2":  # Atualizar Produto
                codigo = input("Digite o código do produto a ser atualizado: ")
                index = chk_mat(codigo, L1)

                if index is not None:
                    print("Produto encontrado:", L1[index])
                    Nm = input("Digite o novo nome do produto: ")
                    Qt = input("Digite a nova quantidade do produto: ")
                    Vala = float(input("Digite o novo valor de atacado do produto: "))
                    Vall = float(input("Digite o novo valor final do produto: "))
                    L1[index] = [codigo, Nm, Qt, Vala, Vall]
                    print("Produto atualizado com sucesso!")
                    Save_Txt(E1, "L1.txt")
                else:
                    print("Produto não encontrado.")
                time.sleep(1)

            elif opt1 == "3":  # Adicionar Produto
                Cod = input("Entre com o código do produto: ")
                if chk_mat(Cod, L1) is not None:
                        print(f"Erro: O código {Cod} já existe na loja!")
                        input("Pressione enter para continuar...")
                else:     
                    Nm = input("Entre com o nome do produto: ")
                    Qt = input("Entre com a quantidade do produto: ")
                    Vala = float(input("Entre com o valor de atacado do produto: "))
                    Vall = float(input("Entre com o valor final do produto: "))
                    L1.append([Cod, Nm, Qt, Vala, Vall])
                    print("Registro adicionado com sucesso!")
                    Save_Txt(L1, "L1.txt")
                    time.sleep(1)
                    continue

            elif opt1 == "4":  # Remover Produto
                codigo = input("Digite o código do produto a ser removido: ")
                index = chk_mat(codigo, L1)
                if index is not None:
                    L1.pop(index)
                    print("Produto removido com sucesso!")
                    Save_Txt(E1, "L1.txt")
                else:
                    print("Produto não encontrado.")
                time.sleep(1)

            elif opt1 == "5":  # Relatório de Produtos
                os.system("cls")
                print(criar_mensagem("Relatório de Produtos - Loja", 50))
                for db in L1:
                    print(f"Código: {db[0]}, Nome: {db[1]}, Quantidade: {db[2]}, Valor Atacado: R${db[3]}, Valor Final: R${db[4]}")
                input("Pressione enter para continuar...")

            elif opt1 == "6":  # Transferencia do Produto:
                os.system("cls")
                print(criar_mensagem("Transferir Produto - Loja", 50))
                codigo = input("Digite o código do produto: ")
                quantidade = int(input("Digite a quantidade a ser transferida: "))
    
                destino = input('Deseja transferir para o (1) Loja ou (2) Estoque? ')
    
                if destino == "1":
                    transferir_produto(codigo, quantidade, L1, E1)
                elif destino == "2":
                    transferir_produto(codigo, quantidade, E1, L1)
                    Save_Txt(E1, "L1.txt")
                else:
                    print("Opção inválida.")
                input("Pressione enter para continuar...")

            elif opt1 == "7": # Retornar ao Menu
                continue

            elif opt1 == "8": # Finalizar Programa
                Save_Txt(L1, "L1.txt")  # Salvar alterações no arquivo L1
                break

        elif Menu == "2":
            opt = input(criar_mensagem('''Estoque MegaGame                                                         
Escolha uma das opções:                                                                           

[1] Consultar Produto:                                                     
[2] Atualizar Produto:                           
[3] Adicionar Produto:                                
[4] Remover Produto:                                                                 
[5] Relatorio Produtos:                          
[6] Transferir Produto:                                                                 
[7] Voltar ao Menu:                                  
[8] Salvar/Sair           

''', 50))

            if opt not in ["1", "2", "3", "4", "5", "6", "7","8"]:
                input("Opção inválida - pressione enter para voltar ao menu ")
                continue

            elif opt == "1":  # Consultar Produto no Estoque
                os.system("cls")
                print(criar_mensagem("Produtos Disponíveis - Estoque", 50))
                for db in E1:
                    print(f"Código: {db[0]}, Nome: {db[1]}, Quantidade: {db[2]}, Valor Atacado: R${db[3]}, Valor Final: R${db[4]}")
                input("Pressione enter para continuar...")

            elif opt == "2":  # Atualizar Produto no Estoque
                codigo = input("Digite o código do produto a ser atualizado: ")
                index = chk_mat(codigo, E1)
                if index is not None:
                    print("Produto encontrado:", E1[index])
                    Nm = input("Digite o novo nome do produto: ")
                    Qt = input("Digite a nova quantidade do produto: ")
                    Vala = float(input("Digite o novo valor de atacado do produto: "))
                    Vall = float(input("Digite o novo valor final do produto: "))
                    E1[index] = [codigo, Nm, Qt, Vala, Vall]
                    print("Produto atualizado com sucesso!")
                    Save_Txt(E1, "E1.txt")
                else:
                    print("Produto não encontrado.")
                time.sleep(1)

            elif opt == "3":  # Adicionar Produto no Estoque
                Cod = input("Entre com o código do produto: ")
                if chk_mat(Cod, E1) is not None:
                        print(f"Erro: O código {Cod} já existe na loja!")
                        input("Pressione enter para continuar...")
                else:     
                    Nm = input("Entre com o nome do produto: ")
                    Qt = input("Entre com a quantidade do produto: ")
                    Vala = float(input("Entre com o valor de atacado do produto: "))
                    Vall = float(input("Entre com o valor final do produto: "))
                    E1.append([Cod, Nm, Qt, Vala, Vall])
                    print("Registro adicionado com sucesso!")
                    Save_Txt(E1, "E1.txt")
                    time.sleep(1)
                    continue
                    
            elif opt == "4":  # Remover Produto do Estoque
                codigo = input("Digite o código do produto a ser removido: ")
                index = chk_mat(codigo, E1)
                if index is not None:
                    E1.pop(index)
                    print("Produto removido com sucesso!")
                    Save_Txt(E1, "E1.txt")
                else:
                    print("Produto não encontrado.")
                time.sleep(1)
                
            elif opt == "5":  # Relatório de Produtos no Estoque
                os.system("cls")
                print(criar_mensagem("Relatório de Produtos - Estoque", 50))
                for db in E1:
                    print(f"Código: {db[0]}, Nome: {db[1]}, Quantidade: {db[2]}, Valor Atacado: R${db[3]}, Valor Final: R${db[4]}")
                input("Pressione enter para continuar...")
                Save_Txt(E1, "E1.txt")
            elif opt == "6":  # Transferencia do Produto:
                os.system("cls")
                print(criar_mensagem("Transferir Produto - Estoque", 50))
                codigo = input("Digite o código do produto: ")
                quantidade = int(input("Digite a quantidade a ser transferida: "))
    
                destino = input('Deseja transferir para o (1) Loja ou (2) Estoque? ')
    
                if destino == "1":
                    transferir_produto(codigo, quantidade, E1, L1)
                elif destino == "2":
                    transferir_produto(codigo, quantidade, L1, E1)
                    Save_Txt(E1, "E1.txt")
                else:
                    print("Opção inválida.")
                input("Pressione enter para continuar...")
            elif opt == "7":  # Voltar ao Menu
                continue

            elif opt == "8":  # Sair
                Save_Txt(E1, "E1.txt")  # Salvar alterações no arquivo E1
                break
        
        if Menu == "3":
                break

if __name__ == "__main__":
    main()


