from django.test import TestCase
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class SeuTeste(TestCase):
    def setUp(self):
        self.servico = Service(ChromeDriverManager().install())
        self.navegador = webdriver.Chrome(service=self.servico)
        self.navegador.get('http://127.0.0.1:8000/')
        time.sleep(2)

    def test_CadastrandoNovoPadrinho(self):
        self.navegador.get('http://127.0.0.1:8000/')
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/button[3]/a').click()
        self.navegador.find_element(By.XPATH, '/html/body/form/div[1]/input[1]').send_keys('teste')
        self.navegador.find_element(By.XPATH, '/html/body/form/div[1]/input[2]').send_keys('teste')
        self.navegador.find_element(By.XPATH, '/html/body/form/div[1]/input[3]').send_keys('teste')
        self.navegador.find_element(By.XPATH, '/html/body/form/div[1]/input[4]').send_keys('teste')
        self.navegador.find_element(By.XPATH, '/html/body/form/div[2]/input[1]').send_keys('teste@gmail.com')
        self.navegador.find_element(By.XPATH, '/html/body/form/div[2]/input[2]').send_keys('teste')
        self.navegador.find_element(By.XPATH, '/html/body/form/div[2]/input[3]').send_keys('teste')
        self.navegador.find_element(By.XPATH, '/html/body/form/div[2]/input[4]').send_keys('teste')
        self.navegador.find_element(By.XPATH, '/html/body/form/div[3]/input').send_keys('teste')
        time.sleep(1)
        self.navegador.find_element(By.XPATH, '/html/body/form/div[4]/button/a').click()
        assert self.navegador.current_url == "http://127.0.0.1:8000/"

    def test_LoginFuncionario(self):
        self.navegador.get('http://127.0.0.1:8000/')
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/button[2]/a').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/form/div[1]/input').send_keys('12345678845')
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/form/div[2]/input').send_keys('123')
        time.sleep(1)
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/form/div[3]/button').click()
        assert self.navegador.current_url == "http://127.0.0.1:8000/funcionario"

    def test_LoginFuncionario_CadastrarCrianca(self):
        self.navegador.get('http://127.0.0.1:8000/')
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/button[2]/a').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/form/div[1]/input').send_keys('12345678845')
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/form/div[2]/input').send_keys('123')
        time.sleep(1)
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/form/div[3]/button').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/a[1]/button').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/form/div[1]/input').send_keys('Nome Completo')
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/form/div[2]/input').send_keys('12122012')
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/form/div[3]/select/option[2]').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/form/div[4]/input').send_keys('12345678845')
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/form/div[5]/input').send_keys('12345678')
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/form/div[6]/input').send_keys('Rua teste')
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/form/div[9]/button').click()
        time.sleep(1)
        nome = self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/form/div[1]/input').get_attribute("value")
        assert nome == ''

    def test_LoginFuncionario_SelecionarCriança(self):
        self.navegador.get('http://127.0.0.1:8000/')
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/button[2]/a').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/form/div[1]/input').send_keys('12345678845')
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/form/div[2]/input').send_keys('123')
        time.sleep(1)
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/form/div[3]/button').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/a[2]/button').click()
        assert self.navegador.current_url == "http://127.0.0.1:8000/selecionar"

    def test_LoginFuncionario_SelecionarCriança(self):
        self.navegador.get('http://127.0.0.1:8000/')
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/button[2]/a').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/form/div[1]/input').send_keys('12345678845')
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/form/div[2]/input').send_keys('123')
        time.sleep(1)
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/form/div[3]/button').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/a[2]/button').click()
        assert self.navegador.current_url == "http://127.0.0.1:8000/selecionar"

    def test_LoginPadrinho(self):
        self.navegador.get('http://127.0.0.1:8000/')
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/button[1]/a').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/form/div[1]/input').send_keys('12345678845')
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/form/div[2]/input').send_keys('123')
        time.sleep(1)
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/form/div[3]/button').click()
        assert self.navegador.current_url == "http://127.0.0.1:8000/criancas"

    def test_LoginPadrinho_MenuCrianca(self):
        self.navegador.get('http://127.0.0.1:8000/')
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/button[1]/a').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/form/div[1]/input').send_keys('12345678845')
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/form/div[2]/input').send_keys('123')
        time.sleep(1)
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/form/div[3]/button').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div[1]/a/div').click()
        assert self.navegador.current_url == "http://127.0.0.1:8000/menucrianca1"

    def test_LoginPadrinho_MenuCrianca_Feedback(self):
        self.navegador.get('http://127.0.0.1:8000/')
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/button[1]/a').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/form/div[1]/input').send_keys('12345678845')
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/form/div[2]/input').send_keys('123')
        time.sleep(1)
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/form/div[3]/button').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div[1]/a/div').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/a[1]/button').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/form/p[1]/input').send_keys('Nome')
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/form/p[2]/select/option[3]').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/form/p[3]/input').send_keys('Mensagem')
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/form/button').click()
        assert self.navegador.current_url == "http://127.0.0.1:8000/finishfeedback"

    def test_LoginPadrinho_MenuCrianca_Desenvolvimento(self):
        self.navegador.get('http://127.0.0.1:8000/')
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/button[1]/a').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/form/div[1]/input').send_keys('12345678845')
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/form/div[2]/input').send_keys('123')
        time.sleep(1)
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/form/div[3]/button').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div[1]/a/div').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/div/a[2]/button').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/form/p[1]/input').send_keys('Mes')
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/form/p[2]/input').send_keys('At')
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/form/p[3]/input').send_keys('3')
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/form/p[4]/input').send_keys('4')
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/form/p[5]/input').send_keys('5')
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/form/p[6]/input').send_keys('1')
        self.navegador.find_element(By.XPATH, '/html/body/div[3]/form/button').click()
        assert self.navegador.current_url == "http://127.0.0.1:8000/desenvolvimento?mes=Mes&atividade=At&carga_horaria=3&avaliacao_red=4&avaliacao_yellow=5&avaliacao_green=1"

    def test_Wpp(self):
        self.navegador.get('http://127.0.0.1:8000/')
        self.navegador.find_element(By.XPATH, '/html/body/div[2]/div/button[1]/a').click()
        assert self.navegador.current_url == "https://api.whatsapp.com/send?1=pt_BR&phone=5511988792324"
