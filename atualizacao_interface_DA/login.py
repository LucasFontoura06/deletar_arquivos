import os
import customtkinter
from tkinter import *

# caminho_arquivo = 'C:\\Users\\Usuario\\Downloads\\'
caminho_arquivo = 'C:\\Users\\Administrador\\Downloads\\'

def janela_login():

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    janela_login = customtkinter.CTk()
    janela_login.title("Login")
    janela_login.geometry("500x300")

    def clique():
        print("Fazer Login")
        email = str(email_login.get())
        password = str(senha_login.get())
        if email == "lucas" and password == "123":
            print("Login Confirmado!")
            tela_confirmado = customtkinter.CTkLabel(janela_login, text= "Login Confirmado!", fg_color="green", corner_radius=8, text_color="black")
            tela_confirmado.pack(padx = 10, pady = 10)
            janela_login.destroy()
            janela01()

        else: 
            print('Acesso Negado!')
            tela_negado = customtkinter.CTkLabel(janela_login, text = "Acesso Negado!", fg_color="red", corner_radius=8, text_color="black")
            tela_negado.pack(padx = 10, pady = 10)
            janela_login.after(2000, lambda: tela_negado.destroy())

    texto = customtkinter.CTkLabel(janela_login, text="Fazer Login", font=("Franklin Gothic", 25))
    texto.pack(padx = 10, pady = 30)

    email_login = customtkinter.CTkEntry(janela_login, placeholder_text="E-mail")
    email_login.pack(padx = 10, pady = 10)

    senha_login = customtkinter.CTkEntry(janela_login, placeholder_text="Password", show="*")
    senha_login.pack(padx = 10, pady = 10)

    botao_login = customtkinter.CTkButton(janela_login, text="Login", command=clique)
    botao_login.pack(padx = 10, pady = 10)


    janela_login.mainloop()

def janela01():

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    janela_principal = customtkinter.CTk()
    janela_principal.title("Deletar Arquivos Duplicados!")
    janela_principal.geometry("520x200")

    texto_orientacao01 = customtkinter.CTkLabel(janela_principal, text ="Seja Bem Vindo!", font =("Arial", 15))
    texto_orientacao01.pack(padx = 10, pady = 10)

    texto_orientacao02 = customtkinter.CTkLabel(janela_principal, text ="Este programa irá deletar os arquivos duplicados na pasta Dowloads do seu computador.")
    texto_orientacao02.pack(padx = 10, pady = 10)

    texto_orientacao02 = customtkinter.CTkLabel(janela_principal, text ="Clique no botão se deseja continuar.")
    texto_orientacao02.pack(padx = 10, pady = 5)

    botao_continuar = customtkinter.CTkButton(janela_principal, text ="Continuar", font =("Arial", 15), command= lambda: Janela02(janela_principal))
    botao_continuar.pack(padx = 10, pady = 10)

    

    janela_principal.mainloop()

def Janela02(janela_principal):

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    janela02 = customtkinter.CTk()
    janela02.title("Deletar Arquivos Duplicados!")
    janela02.geometry("520x200")

    texto_orientacao = customtkinter.CTkLabel(janela02, text="DESEJA DELETAR OS ARQUIVOS DUPLICADOS?", font=("Arial", 15))
    texto_orientacao.pack(padx = 10, pady = 10)

    texto_obs = customtkinter.CTkLabel(janela02, text="OBS: Está ação não pode ser desfeita.", font=("Arial", 15))
    texto_obs.pack(padx = 10, pady = 5)

    botao_sim = customtkinter.CTkButton(janela02, text="Sim", font=("Arial", 15), command= lambda: (deletarArquivosDuplicados(), janela_final(janela02)))
    botao_sim.pack(side = "left", padx = 60, pady = 10)

    botao_nao = customtkinter.CTkButton(janela02, text="Não", font=("Arial", 15), command=janela02.destroy)
    botao_nao.pack(side = "right", padx = 60, pady = 10)

    janela_principal.destroy()

    janela02.mainloop()

def janela_final(janela02):

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    janela_final = customtkinter.CTk()
    janela_final.title("Deletar Arquivos Duplicados!")
    janela_final.geometry("520x200")

    texto_final = customtkinter.CTkLabel(janela_final, text="Os Arquivos Foram Deletados Com Sucesso!", font=("Arial", 15))
    texto_final.pack(padx = 10, pady = 10)

    botao_finalizar = customtkinter.CTkButton(janela_final, text="Finalizar", font=("Arial", 15), command=janela_final.destroy)
    botao_finalizar.pack(padx = 10, pady = 20)

    texto_criador = customtkinter.CTkLabel(janela_final, text=" © Criado por Lucas Fontora Righi Fontes")
    texto_criador.pack(padx = 10, pady = 20)

    janela02.destroy()

    janela_final.mainloop()

def deletarArquivosDuplicados():
    for filename in os.listdir(caminho_arquivo):
        for i in range(1, 101):
            if  f'({i})' in filename:
                file_path = os.path.join(caminho_arquivo, filename)
                os.remove(file_path)
                # print("O arquivo", filename, "foi excluído com sucesso.")
                print("OS ARQUIVOS FORAM DELETADOS COM SUCESSO!")

def main():
    janela_login()
    # janela01()
    # Janela02()
    # janela_final()
    

main()