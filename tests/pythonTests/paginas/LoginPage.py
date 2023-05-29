from tests.pythonTests.paginas.ListaDeProdutosPage import ListaDeProdutosPage

# ###### Importações para automatizar a web
from selenium import webdriver   # Navegador
from selenium.webdriver.common.by import By  # Achar os elementos


class LoginPage:
    driver = webdriver

    def __init__(self, driver):
        self.driver = driver

    def informar_o_usuario(self, usuario):
        self.driver.find_element(By.CSS_SELECTOR, 'input#usuario').send_keys(usuario)
        return self

    def informar_a_senha(self, senha):
        self.driver.find_element(By.CSS_SELECTOR, 'input#senha').send_keys(senha)
        return self

    def submeter_formulario_de_login(self):
        self.driver.find_element(By.CSS_SELECTOR, 'button[name="action"]').click()
        return ListaDeProdutosPage(self.driver)
