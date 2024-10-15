import os
import shutil


class GerenciadorArquivos:
    def __init__(self, diretorio_base):
        """
        Inicializa o gerenciador de arquivos com o diretório base (onde os arquivos estão localizados).
        """
        self.diretorio_base = diretorio_base

    def renomear_arquivo(self, nome_atual, nome_novo):
        """
        Renomeia um arquivo no diretório base, dado o nome atual e o novo nome.
        """
        caminho_atual = os.path.join(self.diretorio_base, nome_atual)
        caminho_novo = os.path.join(self.diretorio_base, nome_novo)

        if os.path.exists(caminho_atual):
            shutil.move(caminho_atual, caminho_novo)
            print(f'Arquivo renomeado: {nome_atual} -> {nome_novo}')
        else:
            print(f'Arquivo não encontrado: {nome_atual}')

    def renomear_arquivos(self, lista_arquivos):
        """
        Recebe uma lista de tuplas (Nome Atual, Nome Novo) e renomeia os arquivos.
        """
        for nome_atual, nome_novo in lista_arquivos:
            self.renomear_arquivo(nome_atual, nome_novo)
        print("Processo de renomeação concluído.")


class GerenciadorCSV(GerenciadorArquivos):
    def __init__(self, diretorio_base):
        """
        Inicializa o gerenciador de arquivos CSV, herdando da classe GerenciadorArquivos.
        """
        super().__init__(diretorio_base)

    def listar_arquivos_csv(self):
        """
        Lista todos os arquivos CSV no diretório base.
        """
        return [f for f in os.listdir(self.diretorio_base) if f.endswith('.csv')]



if __name__ == "__main__":
    # Caminho da pasta de Downloads (substitua conforme necessário)
    pasta_downloads = os.path.expanduser("~/Downloads")

    # Instancia o gerenciador de arquivos CSV
    gerenciador_csv = GerenciadorCSV(pasta_downloads)

    # Tupla com os pares (Nome Atual, Nome Novo)
    arquivos_para_renomear = [
        ("arquivo_atual_1.csv", "arquivo_novo_1.csv"),
        ("arquivo_atual_2.csv", "arquivo_novo_2.csv"),
        ("arquivo_atual_3.csv", "arquivo_novo_3.csv"),
    ]

    # Renomeia os arquivos
    gerenciador_csv.renomear_arquivos(arquivos_para_renomear)

    # Lista todos os arquivos CSV após a renomeação
    print("Arquivos CSV disponíveis na pasta Downloads:", gerenciador_csv.listar_arquivos_csv())
