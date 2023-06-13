from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


#Variavel com a URL do site que iremos acessar
base_url = 'https://www.globo.com/'

@given(u'que eu acesso o site da globo')
def step_impl(context):
    context.driver.get(base_url)
    time.sleep(3)

@when(u'eu clico na aba g1')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="header-section"]/div[2]/div[4]/div[1]/ul/li[1]/a'))).click()
    time.sleep(3)
@when(u'eu clico em menu')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="header-produto"]/div[2]/div/div/div[1]/div'))).click()
    time.sleep(3)
@when(u'eu clico em servicos')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="menu-1-servicos"]/a/span[1]'))).click()
    time.sleep(3)
@when(u'eu clico em app')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="menu-2-app-g1"]/a/span[1]'))).click()
    time.sleep(3)