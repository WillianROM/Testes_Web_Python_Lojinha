import tests.pythonTests.paginas.ListaDeProdutosPage as Lista
from tests.pythonTests.paginas.FormularioDeEdicaoDeProdutoPage import FormularioDeEdicaoDeProdutoPage

# ###### Importações para automatizar a web
from selenium import webdriver   # Navegador
from selenium.webdriver.common.by import By  # Achar os elementos


class FormularioDeAdicaoDeProdutoPage:
    driver = webdriver

    def __init__(self, driver):
        self.driver = driver

    def informar_nome_do_produto(self, produto_nome):
        self.driver.find_element(By.CSS_SELECTOR, 'input#produtonome').send_keys(produto_nome)
        return self

    def informar_valor_do_produto(self, produto_valor):
        self.driver.find_element(By.CSS_SELECTOR, 'input#produtovalor').send_keys(produto_valor)
        return self

    def informar_cores_do_produto(self, produto_cores):
        self.driver.find_element(By.CSS_SELECTOR, 'input#produtocores').send_keys(produto_cores)
        return self

    def submeter_formulario_de_adicao_com_erro(self):
        self.driver.find_element(By.CSS_SELECTOR, 'button[name="action"]').click()
        return Lista.ListaDeProdutosPage(self.driver)

    def submeter_formulario_de_adicao_com_sucesso(self):
        self.driver.find_element(By.CSS_SELECTOR, 'button[name="action"]').click()
        return FormularioDeEdicaoDeProdutoPage(self.driver)
