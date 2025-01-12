from cryptography.fernet import Fernet

# Gerar chave de criptografia
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

# Carregar chave existente
def carregar_chave():
    with open("chave.key", "rb") as chave_file:
        return chave_file.read()

# Criptografar arquivo
def criptografar_arquivo(nome_arquivo):
    chave = carregar_chave()
    fernet = Fernet(chave)

    with open(nome_arquivo, "rb") as file:
        dados = file.read()

    dados_criptografados = fernet.encrypt(dados)

    with open(nome_arquivo, "wb") as file:
        file.write(dados_criptografados)

# Descriptografar arquivo
def descriptografar_arquivo(nome_arquivo):
    chave = carregar_chave()
    fernet = Fernet(chave)

    with open(nome_arquivo, "rb") as file:
        dados_criptografados = file.read()

    dados = fernet.decrypt(dados_criptografados)

    with open(nome_arquivo, "wb") as file:
        file.write(dados)

# Teste
if __name__ == "__main__":
    gerar_chave()  # Gera uma nova chave e salva no arquivo chave.key
    arquivo = "teste.txt"

    # Criptografar
    criptografar_arquivo(arquivo)
    print(f"{arquivo} foi criptografado.")

    # Descriptografar
    descriptografar_arquivo(arquivo)
    print(f"{arquivo} foi descriptografado.")
