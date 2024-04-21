from selenium import webdriver #webdriver serve para simular o navegador
from selenium.webdriver.common.by import By   #serve para encontrar os elementos na pagina

import openpyxl   #biblioteca que permite ler e escrever em arquivos do Excel, cria planilhas 

driver = webdriver.Chrome() 
driver.get('https://www.zara.com/br/pt/man-outerwear-l715.html?v1=2209319')

precos = driver.find_elements(By.XPATH,"//span[@class='money-amount__main']") 
"""encontra todos os preços da página, find elements serve para procurar elementos na pagina """
titulos = driver.find_elements(By.XPATH,"//a[@class= 'product-link _item product-grid-product-info__name link']")

workbook = openpyxl.Workbook() #criando a planilha

workbook.create_sheet('produtos') #criando a pagina 'produtos'

sheet_produtos = workbook['produtos'] #seleciono a pagina 'produtos'
sheet_produtos['A1'].value = 'produto'
sheet_produtos['B1'].value = 'preço'


#inserir os titulos e precos na planilha
for titulo,preco in zip(titulos,precos): #zip une as duas listas, vai ser usado pra juntar o preço com a descrição mas ele vai igualar entao os que nao tiver preco ele nao vai colocar 
    sheet_produtos.append([titulo.text,preco.text])
    
workbook.save('produtos.xlsx')

    



