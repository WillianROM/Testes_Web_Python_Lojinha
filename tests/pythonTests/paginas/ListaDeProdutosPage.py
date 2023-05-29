from tests.pythonTests.paginas.FormularioDeAdicaoDeProdutoPage import FormularioDeAdicaoDeProdutoPage

# ###### Importações para automatizar a web
from selenium import webdriver   # Navegador
from selenium.webdriver.common.by import By  # Achar os elementos


class ListaDeProdutosPage:
    driver = webdriver

    def __init__(self, driver):
        self.driver = driver

    def acessar_formulario_adicao_novo_produto(self):
        self.driver.find_element(By.LINK_TEXT, 'ADICIONAR PRODUTO').click()
        return FormularioDeAdicaoDeProdutoPage(self.driver)

    def capturar_mensagem_apresentada(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'div.toast.rounded').text

    # <div class="toast rounded" style="top: 0px; opacity: 1;">
    # O valor do produto deve estar entre R$ 0,01 e R$ 7.000,00</div>
