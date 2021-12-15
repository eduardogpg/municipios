import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    
    response = requests.get('http://cuentame.inegi.org.mx/monografias/informacion/chis/territorio/div_municipal.aspx?tema=me&e=07')
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        with open('municipios.txt', 'w') as file:
            
            for row in soup.find_all('tr', { 'onmouseout': "fuera (this,'#FFFFFF');" }):
                municipio = row.contents[3].text.replace('    ', '')
                
                format = f'({municipio}, {municipio}),\n'
                file.write(format)