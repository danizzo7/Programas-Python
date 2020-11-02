
#pip install selenium 3.11.0
#instalar o googgle chrome drive :https://chromedriver.chromium.org/dow...
#pip install webdriver_manager
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# navegar ate o whatsapp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com')
time.sleep(30)

#definir contatos e gripos e mensagens a serem enviadas)
contatos = ['Paulo']
mensagem = 'Ola tudo bem? Este é um teste de envio automático de mensagens '
#campo de pesquisa copyable-text selectable-text
#campo de mensagem <div tabindex="-1" class="_2FVVk _2UL8j"_3FRCZ copyable-text selectable-text"
#buscar contatos/grupos
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)
    time.sleep(5)


def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)

for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)


