from bs4 import BeautifulSoup
import requests

# Carrega página 
html = requests.get('https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp').content

# Faz parser da página #
soup = BeautifulSoup(html, 'html.parser')

# Busca os dados nos elementos do html #
resume = soup.find(class_='-gray -line-height-24 _center')
tempMin = soup.find(id='min-temp-1')
tempMax = soup.find(id='max-temp-1')


print('\nResumo: ' + resume.text)
print('Temp. Mínima: ' + tempMin.string)
print('Temp. Máxima: ' + tempMax.string + '\n')

