import os

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
    print('DELETANDO OS ARQUIVOS!')
    for filename in os.listdir(caminho_arquivo):
        for i in range(1, 101):
            if  f'({i})' in filename:
                file_path = os.path.join(caminho_arquivo, filename)
                os.remove(file_path)
                print("O arquivo", filename, "foi excluído com sucesso.")
            
def main():
    indentificarArquivos(caminho_arquivo)
    deletarArquivosDuplicados()
    
main()
