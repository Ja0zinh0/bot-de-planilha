from selenium import webdriver #webdriver serve para simulor o navegador
from selenium.webdriver.common.by import By   #serve para encontrar os elementos na pagina

import openpyxl   #biblioteca que permite ler e escrever em arquivos do Excel, cria planilhas 

driver = webdriver.Chrome() #inicializa o navegador Chrome
driver.get('https://www.zara.com/br/pt/man-outerwear-l715.html?v1=2209319') #acessa a página de produtos da Zara

precos = driver.find_elements(By.XPATH,"//span[@class='money-amount__main']") #encontra todos os preços da página
titulos = driver.find_elements(By.XPATH,"//a[@class= 'product-link _item product-grid-product-info__name link']") #encontra todos os títulos dos produtos

workbook = openpyxl.Workbook() #criando a planilha

workbook.create_sheet('produtos') #criando a pagina 'produtos'

sheet_produtos = workbook['produtos'] #seleciono