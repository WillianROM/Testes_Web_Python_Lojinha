from tests.pythonTests.paginas.LoginPage import LoginPage

from pytest import fixture

# ###### Importações para automatizar a web
from selenium import webdriver   # Navegador

# ###### Gerenciador de navegador
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Test_Produtos:
    driver = webdriver

    @fixture(autouse=True)
    def run_before_and_after_tests(self):
        # before_each
        servico = ChromeService(ChromeDriverManager().install())  # Verifica se a versão do Chrome está atualizado
        self.driver = webdriver.Chrome(service=servico)  # Abre o chrome com a versão atualizada

        self.driver.implicitly_wait(5)  # Tempo de espera implicita

        self.driver.maximize_window()  # Deixar o navegador com a tela máxima

        self.driver.get('http://165.227.93.41/lojinha-web/v2/')  # Navegar para a página da Lojinha Web

        yield
        # after_each
        self.driver.quit()

    def test_nao_e_permitido_registrar_produto_com_valor_igual_a_zero(self):
        login_page = LoginPage(self.driver)

        mensagem_apresentada = login_page\
            .informar_o_usuario('admin')\
            .informar_a_senha('admin')\
            .submeter_formulario_de_login()\
            .acessar_formulario_adicao_novo_produto()\
            .informar_nome_do_produto('Notebook Dell Vostro 3510')\
            .informar_valor_do_produto(0)\
            .informar_cores_do_produto('cinza')\
            .submeter_formulario_de_adicao_com_erro()\
            .capturar_mensagem_apresentada()

        assert mensagem_apresentada == 'O valor do produto deve estar entre R$ 0,01 e R$ 7.000,00'

    def test_nao_e_permitido_registrar_produto_com_valor_acima_de_sete_mil(self):
        login_page = LoginPage(self.driver)

        mensagem_apresentada = login_page\
            .informar_o_usuario('admin')\
            .informar_a_senha('admin')\
            .submeter_formulario_de_login()\
            .acessar_formulario_adicao_novo_produto()\
            .informar_nome_do_produto('Notebook Dell Vostro 3510')\
            .informar_valor_do_produto(7000.01)\
            .informar_cores_do_produto('cinza')\
            .submeter_formulario_de_adicao_com_erro()\
            .capturar_mensagem_apresentada()

        assert mensagem_apresentada == 'O valor do produto deve estar entre R$ 0,01 e R$ 7.000,00'

    def test_posso_adicionar_produtos_que_estejam_na_faixa_de_um_centavo_a_sete_mil_reais(self):
        login_page = LoginPage(self.driver)

        mensagem_apresentada = login_page\
            .informar_o_usuario('admin')\
            .informar_a_senha('admin')\
            .submeter_formulario_de_login()\
            .acessar_formulario_adicao_novo_produto()\
            .informar_nome_do_produto('Notebook Dell Vostro 3510')\
            .informar_valor_do_produto(3599.99)\
            .informar_cores_do_produto('cinza')\
            .submeter_formulario_de_adicao_com_sucesso()\
            .capturar_mensagem_apresentada()

        assert mensagem_apresentada == 'Produto adicionado com sucesso'

    def test_posso_adicionar_produtos_com_valor_de_um_centavo(self):
        login_page = LoginPage(self.driver)

        mensagem_apresentada = login_page\
            .informar_o_usuario('admin')\
            .informar_a_senha('admin')\
            .submeter_formulario_de_login()\
            .acessar_formulario_adicao_novo_produto()\
            .informar_nome_do_produto('Notebook Dell Vostro 3510')\
            .informar_valor_do_produto(0.01)\
            .informar_cores_do_produto('cinza')\
            .submeter_formulario_de_adicao_com_sucesso()\
            .capturar_mensagem_apresentada()

        assert mensagem_apresentada == 'Produto adicionado com sucesso'

    def test_posso_adicionar_produtos_com_valor_de_sete_mil_reais(self):
        login_page = LoginPage(self.driver)

        mensagem_apresentada = login_page\
            .informar_o_usuario('admin')\
            .informar_a_senha('admin')\
            .submeter_formulario_de_login()\
            .acessar_formulario_adicao_novo_produto()\
            .informar_nome_do_produto('Notebook Dell Vostro 3510')\
            .informar_valor_do_produto(7000.00)\
            .informar_cores_do_produto('cinza')\
            .submeter_formulario_de_adicao_com_sucesso()\
            .capturar_mensagem_apresentada()

        assert mensagem_apresentada == 'Produto adicionado com sucesso'
