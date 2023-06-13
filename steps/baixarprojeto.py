from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


#Variavel com a URL do site que iremos acessar
base_url = 'https://github.com/douglvv'

@given(u'que eu acesso o site do GitHub')
def step_impl(context):
    context.driver.get(base_url)
    time.sleep(3)

@when(u'eu clico no botão')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[4]/main/div[1]/div/div/div[2]/div/nav/a[2]'))).click()
    time.sleep(3)

@when(u'eu clico projeto')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="user-repositories-list"]/ul/li[1]/div[1]/div[1]/h3/a'))).click()
    time.sleep(3)

@when(u'eu clico em code')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="repo-content-pjax-container"]/div/div/div[2]/div[1]/div[1]/span[1]/get-repo/details/summary/span[1]/span'))).click()
    time.sleep(3)

@when(u'eu clico em baixar')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="local-panel"]/ul/li[3]/a'))).click()
    time.sleep(3)    

@when(u'eu clico em code novamente')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="repo-content-pjax-container"]/div/div/div[2]/div[1]/div[1]/span[1]/get-repo/details/summary'))).click()
    time.sleep(3)   

@when(u'eu clico em voltar')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="repository-container-header"]/div[1]/div/div/span[1]/a'))).click()
    time.sleep(3)

@when(u'eu clico em seguir')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[4]/main/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div/div/span/span/a'))).click()
    time.sleep(3)    
    
@when(u'eu clico em termos')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[4]/ul/li[1]/a'))).click()
    time.sleep(3)     


@when(u'eu clico em definicoes')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="article-contents"]/div/table/tbody/tr[1]/td[1]/a'))).click()
    time.sleep(3)    


@when(u'eu clico em privacidade')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="article-contents"]/div/ol/li[2]/a[1]'))).click()
    time.sleep(3) 
    