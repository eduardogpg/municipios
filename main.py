import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    
    response = requests.get('http://cuentame.inegi.org.mx/monografias/informacion/chis/territorio/div_municipal.aspx?tema=me&e=07')
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        with open('municipios.txt', 'w') as file:
            
            for row in soup.find_all('tr', { 'onmouseout': "fuera (this,'#FFFFFF');" }):
                municipio = row.contents[3].text.replace('    ', '')
                
                municipio = municipio.replace('Á', 'A')
                municipio = municipio.replace('É', 'E')
                municipio = municipio.replace('Í', 'I')
                municipio = municipio.replace('Ó', 'O')
                municipio = municipio.replace('Ú', 'U')
                
                title = municipio.replace(' ', '_').upper()
  
                format = f"{title} = '{municipio}', _('{municipio}'),\n"
                file.write(format)