#UMC - Atividade: Avaliação 01 Algoritmo e Estrutura Condicional
#Nomes: Ana Caroline Suzart da Silva / Sophia Luna da Silva Rocha
#RGM: 11242101001 / 11242101086 DATA: 01/10/2024

import os
import time
import textwrap

#margem do programa com bordas nos prints.
def criar_mensagem(texto, largura=60):
    borda_superior = '╔' + '═' * (largura + 2) + '╗'
    borda_inferior = '╚' + '═' * (largura + 2) + '╝'
    
    texto_formatado = textwrap.fill(texto, largura)
    linhas = texto_formatado.split('\n')
    linhas_com_margem = [f'║ {linha.ljust(largura)} ║' for linha in linhas]
    
    return '\n'.join([borda_superior] + linhas_com_margem + [borda_inferior])

#valores e tipos de hospedagem classic e premium
def calculo_orcamento(tipo_apartamento, quantidade_pessoas, dias_estadia):
    precos = {
        '1': {1: 20.00, 2: 28.00, 3: 35.00, 4: 42.00, 5: 48.00, 6: 53.00},  # Classic
        '2': {1: 25.00, 2: 34.00, 3: 42.00, 4: 50.00, 5: 57.00, 6: 63.00}   # Premium
    }
    #mensagem de erro
    if tipo_apartamento not in precos:
        return "Tipo de apartamento inválido."
    if quantidade_pessoas not in precos[tipo_apartamento]:
        return "Quantidade de pessoas inválida."
    #calculo de valores
    valor_diaria = precos[tipo_apartamento][quantidade_pessoas]
    custo_total = valor_diaria * dias_estadia
    
    return custo_total

def cadastro_usuario():#cadastro do usuario
    os.system("cls")
    print("\033[31mHOTEL MIDNIGHT\033[0;0m")
    print(criar_mensagem("Bem-vindo ao cadastro de usuário!", 50))
    
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    telefone = input("Telefone: ")
    cpf = input("CPF: ")

    print(criar_mensagem(f"Cadastro realizado com sucesso, {nome}!", 50))
    time.sleep(2)  
    return nome, email, senha, telefone, cpf

def login_usuario(email_cadastrado, senha_cadastrada):#login do usuario
    os.system("cls")
    print("\033[31mHOTEL MIDNIGHT\033[0;0m")
    print(criar_mensagem("Por favor, faça login!", 50))
    
    while True:
        email = input("Email: ")
        senha = input("Senha: ")
        
        if email == email_cadastrado and senha == senha_cadastrada:
            print(criar_mensagem("Login bem-sucedido!", 50))
            time.sleep(2)
            break
        else:
            print(criar_mensagem("Email ou senha incorretos. Tente novamente.", 50)) #mensagem de erro caso errar email ou senha
            time.sleep(2) 

def menu(): #menu do orçamento
    os.system("cls")
    print("\033[31mHOTEL MIDNIGHT\033[0;0m")
    nome, email, senha, telefone, cpf = cadastro_usuario()
    
    login_usuario(email, senha)

    while True:
        os.system("cls")
        print("\033[31mHOTEL MIDNIGHT\033[0;0m")
        print(criar_mensagem(f"Muito prazer em te conhecer, {nome}!", 50))
        
        print(criar_mensagem("[1] para Calcular Orçamento [2] para Sair", 50))
        opcao = input("> ")
        
        if opcao == "1":
            calcular_orcamento(nome, telefone, cpf)
        elif opcao == "2":
            print("\033[31mHOTEL MIDNIGHT\033[0;0m")
            input(criar_mensagem("Agradecemos a sua presença, até breve :)", 50)) 
            break
        else:
            print("\033[31mHOTEL MIDNIGHT\033[0;0m")
            input(criar_mensagem("Selecione uma opção válida por favor :(", 50))
            time.sleep(2)

def calcular_orcamento(nome, telefone, cpf):
    while True:
        os.system("cls")
        
        while True:
            try:
                print("\033[31mHOTEL MIDNIGHT\033[0;0m")
                print(criar_mensagem("Quantas pessoas irão com você?\nLembrando que no máximo 5 acompanhantes, caso for somente você digite 0:", 50))
                N2 = int(input("> "))

                if N2 not in [0, 1, 2, 3, 4, 5]:
                    print("\033[31mHOTEL MIDNIGHT\033[0;0m")
                    print(criar_mensagem("Lembrando que o número de acompanhantes deve ser entre 0 e 5!", 50))
                    time.sleep(2)
                else:
                    break
            except ValueError:
                print("\033[31mHOTEL MIDNIGHT\033[0;0m")
                input(criar_mensagem("Entrada inválida! Por favor insira um número válido.", 50))
                time.sleep(2)

        while True:
            try:
                print("\033[31mHOTEL MIDNIGHT\033[0;0m")
                print(criar_mensagem("Quantos dias irá utilizar nossos serviços?", 50))
                dias1 = int(input("> ")) 
                break
            except ValueError:
                print("\033[31mHOTEL MIDNIGHT\033[0;0m")
                print(criar_mensagem("Por favor, insira um número válido para os dias de estadia.", 50))
                time.sleep(2)
        
        while True: #tabela de preços
            print("\033[31mHOTEL MIDNIGHT\033[0;0m")
            print(criar_mensagem('''
            VALOR DA DIÁRIA:                    
 Possuímos dois tipos de acomodações:           
 Pessoas:       |Classic:       |Premium:       
 [1]            |20,00          |25,00          
 [2]            |28,00          |34,00          
 [3]            |35,00          |42,00          
 [4]            |42,00          |50,00          
 [5]            |48,00          |57,00          
 [6]            |53,00          |63,00          

Digite [1] para Classic \nDigite [2] para Premium 
''', 50)) #apos a escolha do tipo de hospedagem o programa ira calcular os dias e quantidade de pessoas de acordo com sua escolha 
            ap1 = input("> ")
            if ap1 not in ["1", "2"]:
                print("\033[31mHOTEL MIDNIGHT\033[0;0m") #mensagem de erro
                input(criar_mensagem("Selecione uma opção válida por favor :(", 50))
                time.sleep(2)
            else:
                break
        
        nomes = [nome] #nome dos acompanhantes
        for i in range(N2):
            nome_pessoa = input(f''' 
       \033[31m"HOTEL MIDNIGHT"\033[0;0m
Qual o nome do acompanhante {i + 1}? 
    ''')
            nomes.append(nome_pessoa)

        os.system("cls") #calculo total
        custo_total = calculo_orcamento(ap1, N2 + 1, dias1)

        if isinstance(custo_total, str):
            print(custo_total)
        else:
            print("\033[31mHOTEL MIDNIGHT\033[0;0m") #resultado do orçamento 
            print(criar_mensagem(f'''                                                            

ORÇAMENTO FINAL                               
                    Tipo de Apartamento:{'Premium' if ap1 == '2' else 'Classic'}
                    Quantidade de Pessoas:{N2 + 1}                              
                    Dias de Estadia:{dias1}                                  
                    Nomes dos Hóspedes:{", ".join(nomes)}\n
                    Telefone:{telefone}
                    CPF:{cpf}\n
                    Total:R${custo_total:.2f}  
    ''', 50))

        print("\033[31mHOTEL MIDNIGHT\033[0;0m")
        print(criar_mensagem('''   
Deseja fazer outro orçamento?
[s] para Sim
Pressione qualquer botão para retornar ao menu principal
     ''', 50)) #retorno ao menu principal
        voltar = input("> ")
        if voltar.lower() != 's':
            print("\033[31mHOTEL MIDNIGHT\033[0;0m  ")
            print(criar_mensagem(f''' 
       \033[31m"HOTEL MIDNIGHT"\033[0;0m
     Obrigado pela preferência, nos vemos em breve :) {nome}      
    ''', 50)) #fim do programa
            break

menu()


