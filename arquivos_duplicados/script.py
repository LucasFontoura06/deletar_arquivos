import os
import requests

from tkinter import *

caminho_arquivo = 'C:\\Users\\Usuario\\Downloads\\'

def indentificarArquivos(arquivos):
    print("ARQUIVOS NA PASTA:")
    arquivos = os.listdir(caminho_arquivo)
    for arquivo in arquivos:
        if os.path.isfile(os.path.join(caminho_arquivo, arquivo)):
            nome_arquivo = os.path.basename(arquivo)
            print("-- " + nome_arquivo)
    print("_"*60)   

def deletarArquivosDuplicados():
    print('OS ARQUIVOS FORAM DELETADOS COM SUCESSO!')
    for filename in os.listdir(caminho_arquivo):
        for i in range(1, 101):
            if  f'({i})' in filename:
                file_path = os.path.join(caminho_arquivo, filename)
                os.remove(file_path)
                # print("O arquivo", filename, "foi excluído com sucesso.")
                print("OS ARQUIVOS FORAM DELETADOS COM SUCESSO!")

def janelaFinal(janela02):
    janela_final = Tk()
    janela_final.title("Deletar Arquivos Duplicados!")
    janela_final.geometry("520x200")

    texto_final = Label(janela_final, text="Os Arquivos Foram Deletados Com Sucesso!", font=("Arial", 15))
    texto_final.place(x=60, y=20)

    botao_finalizar = Button(janela_final, text="Finalizar", font=("Arial", 15), command=janela_final.destroy)
    botao_finalizar.place(x=200, y=90)

    texto_criador = Label(janela_final, text=" © Criado por Lucas Fontora Righi Fontes")
    texto_criador.place(x=150, y=160)

    janela02.destroy()


    janela_final.mainloop()

def abrirJanela02(janela01):
    janela02 = Tk()
    janela02.title("Deletar Arquivos Duplicados!")
    janela02.geometry("520x200")

    texto_orientacao_final = Label(janela02, text="Você tem certeza? Esta ação não pode ser desfeita!", font=("Arial", 15))
    texto_orientacao_final.place(x=30, y=20)

    botao_sim02 = Button(janela02, text="Sim", font=("Arial", 15), command=lambda: (deletarArquivosDuplicados(), janelaFinal(janela02)))
    botao_sim02.place(x=170, y=80)

    botao_nao02 = Button(janela02, text="Não", font=("Arial", 15), command=janela01.destroy)
    botao_nao02.place(x=290, y=80)

    janela01.destroy()

    janela02.mainloop()
    

def abrirJanela01(janela_principal):
    janela01 = Tk()
    janela01.title("Deletar Arquivos Duplicados!")
    janela01.geometry("520x200")

    texto_orientacao = Label(janela01, text="DESEJA DELETAR OS ARQUIVOS DUPLICADOS?", font=("Arial", 15))
    texto_orientacao.place(x=25, y=10)

    botao_sim = Button(janela01, text="Sim", font=("Arial", 15), command=lambda: abrirJanela02(janela01))
    botao_sim.place(x=160, y=70)

    botao_nao = Button(janela01, text="Não", font=("Arial", 15), command=janela01.destroy)
    botao_nao.place(x=280, y=70)

    janela_principal.destroy()

    janela01.mainloop()

def janelaInicial():
    janela_principal = Tk()
    janela_principal.title("Deletar Arquivos Duplicados!")
    janela_principal.geometry("520x200")

    texto_orientacao01 = Label(janela_principal, text="Seja Bem Vindo!", font=("Arial", 15))
    texto_orientacao01.place(x=180, y=10)

    texto_orientacao02 = Label(janela_principal, text="Este programa irá deletar os arquivos duplicados na pasta Dowloads do seu computador.")
    texto_orientacao02.place(x=30, y=70)

    texto_orientacao02 = Label(janela_principal, text="Clique no botão se deseja continuar.")
    texto_orientacao02.place(x=165, y=100)

    botao_continuar = Button(janela_principal, text="Continuar", font=("Arial", 15), command=lambda: abrirJanela01(janela_principal))
    botao_continuar.place(x=210, y=140)

    

    janela_principal.mainloop()

def main():
    janelaInicial()
    # abrirJanela01()
    # abrirJanela02()
    # janelaFinal()

main()
