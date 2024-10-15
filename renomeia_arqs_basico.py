import os
import shutil

# Caminho da pasta de Downloads (substitua conforme necessário)
pasta_downloads = os.path.expanduser("~/Downloads")

# Tupla com os pares (Nome Atual, Nome Novo)
arquivos_para_renomear = [
    ("arquivo_atual_1.csv", "arquivo_novo_1.csv"),
    ("arquivo_atual_2.csv", "arquivo_novo_2.csv"),
    ("arquivo_atual_3.csv", "arquivo_novo_3.csv"),
]

# Renomear arquivos
for nome_atual, nome_novo in arquivos_para_renomear:
    caminho_atual = os.path.join(pasta_downloads, nome_atual)
    caminho_novo = os.path.join(pasta_downloads, nome_novo)

    # Verifica se o arquivo existe antes de renomear
    if os.path.exists(caminho_atual):
        shutil.move(caminho_atual, caminho_novo)
        print(f'Arquivo renomeado: {nome_atual} -> {nome_novo}')
    else:
        print(f'Arquivo não encontrado: {nome_atual}')

print("Processo de renomeação concluído.")
