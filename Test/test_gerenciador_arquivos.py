import unittest
import os
import shutil
from unittest.mock import patch, MagicMock
from renomeia_arqs import \
    GerenciadorCSV  # Supondo que seu código esteja em um arquivo chamado gerenciador_arquivos.py


class TestGerenciadorCSV(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Executa uma vez antes de todos os testes. Prepara o ambiente de testes criando um diretório temporário.
        """
        cls.diretorio_teste = "test_downloads"
        os.makedirs(cls.diretorio_teste, exist_ok=True)

    def setUp(self):
        """
        Executa antes de cada teste. Prepara arquivos temporários para renomeação.
        """
        self.gerenciador_csv = GerenciadorCSV(self.diretorio_teste)

        # Cria arquivos temporários CSV
        with open(os.path.join(self.diretorio_teste, "arquivo_atual_1.csv"), "w") as f:
            f.write("dados temporários")
        with open(os.path.join(self.diretorio_teste, "arquivo_atual_2.csv"), "w") as f:
            f.write("dados temporários")

    def tearDown(self):
        """
        Executa após cada teste. Remove todos os arquivos criados para os testes.
        """
        for arquivo in os.listdir(self.diretorio_teste):
            arquivo_caminho = os.path.join(self.diretorio_teste, arquivo)
            if os.path.isfile(arquivo_caminho):
                os.remove(arquivo_caminho)

    @classmethod
    def tearDownClass(cls):
        """
        Executa uma vez após todos os testes. Remove o diretório de testes criado.
        """
        shutil.rmtree(cls.diretorio_teste)

    def test_renomear_arquivo(self):
        """
        Testa se um arquivo CSV é renomeado corretamente.
        """
        self.gerenciador_csv.renomear_arquivo("arquivo_atual_1.csv", "arquivo_novo_1.csv")
        self.assertTrue(os.path.exists(os.path.join(self.diretorio_teste, "arquivo_novo_1.csv")))
        self.assertFalse(os.path.exists(os.path.join(self.diretorio_teste, "arquivo_atual_1.csv")))

    def test_renomear_arquivo_inexistente(self):
        """
        Testa o comportamento quando tenta renomear um arquivo que não existe.
        """
        with patch('builtins.print') as mocked_print:
            self.gerenciador_csv.renomear_arquivo("arquivo_inexistente.csv", "arquivo_novo.csv")
            mocked_print.assert_called_with('Arquivo não encontrado: arquivo_inexistente.csv')

    def test_renomear_arquivos_em_lote(self):
        """
        Testa a renomeação de vários arquivos em lote.
        """
        arquivos_para_renomear = [
            ("arquivo_atual_1.csv", "arquivo_novo_1.csv"),
            ("arquivo_atual_2.csv", "arquivo_novo_2.csv"),
        ]
        self.gerenciador_csv.renomear_arquivos(arquivos_para_renomear)

        # Verifica se os arquivos foram renomeados
        self.assertTrue(os.path.exists(os.path.join(self.diretorio_teste, "arquivo_novo_1.csv")))
        self.assertTrue(os.path.exists(os.path.join(self.diretorio_teste, "arquivo_novo_2.csv")))

    def test_listar_arquivos_csv(self):
        """
        Testa se a listagem de arquivos CSV no diretório está correta.
        """
        arquivos_csv = self.gerenciador_csv.listar_arquivos_csv()
        self.assertIn("arquivo_atual_1.csv", arquivos_csv)
        self.assertIn("arquivo_atual_2.csv", arquivos_csv)


if __name__ == "__main__":
    unittest.main()
