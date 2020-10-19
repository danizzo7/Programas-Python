import pandas as pd
import requests
from bs4 import BeautifulSoup

# definindo a URL de busca
url = 'https://www.amazon.com.br/s?k=iphone&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2'
page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')

# Coletando o Produto
review_product = {}
review_product_elem = soup.find_all(class_='s-expand-height s-include-content-margin s-border-bottom s-latency-cf-section')

for pos, item in enumerate(review_product_elem):
    if item.find(class_='a-link-normal a-text-normal') is not None:
        key = str(pos) + ' - ' + item.find(class_='a-link-normal a-text-normal').text.replace("\n", "")
        if item.find(class_='a-offscreen') is not None:
            review_product[key] = item.find(class_='a-offscreen').text
        else:
            review_product[key] = None
#enumerate pega a lista e divide em duasvariaveis
# print(review_product)

df = pd.DataFrame(data=review_product, index=[0])
df = (df.T)

print (df)

# Exportando os dados para a planilha Excel
df.to_excel('Lista de Produtod.xlsx',index=True)