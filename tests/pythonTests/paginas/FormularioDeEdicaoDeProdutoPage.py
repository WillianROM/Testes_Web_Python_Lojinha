

# ###### Importações para automatizar a web
from selenium import webdriver   # Navegador
from selenium.webdriver.common.by import By  # Achar os elementos


class FormularioDeEdicaoDeProdutoPage:
    driver = webdriver

    def __init__(self, driver):
        self.driver = driver

    def capturar_mensagem_apresentada(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'div.toast.rounded').text
