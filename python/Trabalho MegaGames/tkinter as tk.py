import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Função para carregar dados de um arquivo de texto (L1.txt ou E1.txt)
def Load_Txt(filename, Lista):
    with open(filename, 'r') as Dados:
        for i in Dados:
            Lista.append(i.rstrip().split(","))
    return Lista

# Função para salvar dados em um arquivo de texto (L1.txt ou E1.txt)
def Save_Txt(Lista, filename):
    with open(filename, "w") as RT:
        for dados in Lista:
            RT.write(f"{dados[0]},{dados[1]},{dados[2]},{dados[3]},{dados[4]}\n")

# Função para consultar e exibir produtos na mesma janela
def consultar_produto(lista):
    # Limpar a janela
    for widget in root.winfo_children():
        widget.destroy()

    # Criar os botões de navegação
    tk.Button(root, text="Voltar ao Menu", command=menu_inicial).grid(row=0, column=0, pady=10, padx=10)

    # Exibir consulta de produtos na janela
    consulta = "\n".join([f"Código: {p[0]}, Nome: {p[1]}, Quantidade: {p[2]}, Valor Atacado: R${p[3]}, Valor Final: R${p[4]}" for p in lista])
    if not consulta:
        consulta = "Nenhum produto encontrado!"

    # Criar um widget Text para mostrar a consulta
    text_area = tk.Text(root, height=20, width=110)
    text_area.insert(tk.END, consulta)
    text_area.config(state=tk.DISABLED)  # Tornar o texto somente leitura
    text_area.grid(row=1, column=0, columnspan=3, pady=10, padx=10)

# Função para adicionar produto
def adicionar_produto(lista, codigo_entry, nome_entry, quantidade_entry, valor_atacado_entry, valor_final_entry):
    codigo = codigo_entry.get()
    if any(prod[0] == codigo for prod in lista):
        messagebox.showerror("Erro", f"Produto com código {codigo} já existe!")
        return
    nome = nome_entry.get()
    quantidade = quantidade_entry.get()
    valor_atacado = valor_atacado_entry.get()
    valor_final = valor_final_entry.get()
    
    # Adicionar produto à lista
    lista.append([codigo, nome, quantidade, valor_atacado, valor_final])
    Save_Txt(lista, "L1.txt")
    messagebox.showinfo("Produto Adicionado", "Produto adicionado com sucesso!")

# Função para alterar produto
def alterar_produto(lista, codigo_entry, nome_entry, quantidade_entry, valor_atacado_entry, valor_final_entry):
    codigo = codigo_entry.get()
    for prod in lista:
        if prod[0] == codigo:
            nome = nome_entry.get()
            quantidade = quantidade_entry.get()
            valor_atacado = valor_atacado_entry.get()
            valor_final = valor_final_entry.get()
            
            # Atualizar produto
            prod[1], prod[2], prod[3], prod[4] = nome, quantidade, valor_atacado, valor_final
            Save_Txt(lista, "L1.txt")
            messagebox.showinfo("Produto Atualizado", "Produto atualizado com sucesso!")
            return
    messagebox.showerror("Erro", f"Produto com código {codigo} não encontrado!")

# Função para remover produto
def remover_produto(lista, codigo_entry):
    codigo = codigo_entry.get()
    for i, prod in enumerate(lista):
        if prod[0] == codigo:
            del lista[i]
            Save_Txt(lista, "L1.txt")
            messagebox.showinfo("Produto Removido", "Produto removido com sucesso!")
            return
    messagebox.showerror("Erro", f"Produto com código {codigo} não encontrado!")

# Função para exibir o menu de ações do estoque/loja
def menu_estoque_ou_loja():
    # Limpar a janela
    for widget in root.winfo_children():
        widget.destroy()

    # Adicionar logo na nova tela
    logo_img = Image.open("Imagelala.jpg")  # Alterar o caminho da imagem conforme necessário
    logo_img = logo_img.resize((200, 200))
    logo = ImageTk.PhotoImage(logo_img)

    logo_label = tk.Label(root, image=logo)
    logo_label.image = logo
    logo_label.grid(row=0, column=0, columnspan=4, pady=10)

    # Criar os campos de entrada (Entry)
    codigo_label = tk.Label(root, text="Código do Produto:")
    codigo_label.grid(row=1, column=0, pady=5)
    codigo_entry = tk.Entry(root)
    codigo_entry.grid(row=1, column=1, pady=5)

    nome_label = tk.Label(root, text="Nome do Produto:")
    nome_label.grid(row=2, column=0, pady=5)
    nome_entry = tk.Entry(root)
    nome_entry.grid(row=2, column=1, pady=5)

    quantidade_label = tk.Label(root, text="Quantidade do Produto:")
    quantidade_label.grid(row=3, column=0, pady=5)
    quantidade_entry = tk.Entry(root)
    quantidade_entry.grid(row=3, column=1, pady=5)

    valor_atacado_label = tk.Label(root, text="Valor Atacado do Produto:")
    valor_atacado_label.grid(row=4, column=0, pady=5)
    valor_atacado_entry = tk.Entry(root)
    valor_atacado_entry.grid(row=4, column=1, pady=5)

    valor_final_label = tk.Label(root, text="Valor Final do Produto:")
    valor_final_label.grid(row=5, column=0, pady=5)
    valor_final_entry = tk.Entry(root)
    valor_final_entry.grid(row=5, column=1, pady=5)

    # Criar os botões de ação
    tk.Button(root, text="Consultar Produto", command=lambda: consultar_produto(L1)).grid(row=6, column=0, pady=5)
    tk.Button(root, text="Adicionar Produto", command=lambda: adicionar_produto(L1, codigo_entry, nome_entry, quantidade_entry, valor_atacado_entry, valor_final_entry)).grid(row=6, column=1, pady=5)
    tk.Button(root, text="Alterar Produto", command=lambda: alterar_produto(L1, codigo_entry, nome_entry, quantidade_entry, valor_atacado_entry, valor_final_entry)).grid(row=6, column=2, pady=5)
    tk.Button(root, text="Remover Produto", command=lambda: remover_produto(L1, codigo_entry)).grid(row=6, column=3, pady=5)
    tk.Button(root, text="Voltar ao Menu", command=menu_inicial).grid(row=7, column=0, pady=10, padx=10)
    tk.Button(root, text="Salvar/Sair", command=salvar_ou_sair).grid(row=7, column=3, pady=10, padx=10)

# Função de salvar ou sair
def salvar_ou_sair():
    Save_Txt(L1, "L1.txt")  # Salva os dados de volta no arquivo L1.txt
    root.quit()

# Função para voltar ao menu inicial
def menu_inicial():
    # Limpar a janela
    for widget in root.winfo_children():
        widget.destroy()

    # Adicionar logo na tela inicial
    logo_img = Image.open("Imagelala.jpg")  # Alterar o caminho da imagem conforme necessário
    logo_img = logo_img.resize((500, 500))
    logo = ImageTk.PhotoImage(logo_img)

    logo_label = tk.Label(root, image=logo)
    logo_label.image = logo
    logo_label.grid(row=0, column=0, columnspan=4, pady=10)

    # Criar os botões do menu inicial
    tk.Button(root, text="Loja", command=menu_estoque_ou_loja).grid(row=1, column=0, pady=10, padx=10)
    tk.Button(root, text="Estoque", command=menu_estoque_ou_loja).grid(row=1, column=1, pady=10, padx=10)
    tk.Button(root, text="Sair/Salvar", command=salvar_ou_sair).grid(row=1, column=2, pady=10, padx=10)

# Carregar os dados do arquivo de texto
L1 = []  # Lista de produtos na loja
E1 = []  # Lista de produtos no estoque
L1 = Load_Txt("L1.txt", L1)
E1 = Load_Txt("E1.txt", E1)

# Criar a janela principal
root = tk.Tk()
root.title("Sistema de Estoque e Loja")

# Definir o tamanho da janela
root.geometry("800x600")

# Exibir o menu inicial
menu_inicial()

# Iniciar o loop da interface gráfica
root.mainloop()
