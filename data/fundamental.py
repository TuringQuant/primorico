import requests
from bs4 import BeautifulSoup

class Fundamentus:

    base_url = 'https://www.fundamentus.com.br/detalhes.php?papel='

    def __init__(self, tickers):

        if isinstance(tickers, list):
            self.tickers = tickers
        elif isinstance(tickers, str):
            self.tickers = [].append(tickers)
        else:
            self.tickers = []

        self.data = []

    def get(self):

        fundamental = []

        for ticker in self.tickers:
            
            print(f'Requisitando dados {ticker} ...')
            
            try:
                url = self.base_url + ticker
                response = requests.get(url)
            except:
                print(f'Não foi possível obter dados de {ticker}')
                continue

            soup = BeautifulSoup(response.content, 'html.parser')

            alltables = soup.find_all('table', 'w728')
            t = alltables[2]

            label = t.find_all('td', {'class': 'label'})
            content = t.find_all('td', {'class': 'data'})

            fundamental.append(
                {l.find('span', {'class': 'txt'}).getText(): c.getText() for l, c in zip(label, content)}
            )
        
        self.data = Fundamentus.fix(fundamental, self.tickers)

    @staticmethod
    def fix(json, tickers):
        lista = []
        for ticker_data, ticker in zip(json, tickers):
            new_dict = {}    
            for key in ticker_data:
                string = ticker_data[key]
                is_percentage = True if '%' in string else False
                replaced_string = string.replace(',','.').replace('%', '').replace('\n', '')
                if replaced_string:
                    if is_percentage:
                        new_dict[key] =  float(replaced_string) / 100
                    else:
                        new_dict[key] =  float(replaced_string)
            new_dict['ticker'] = ticker
            lista.append(new_dict)
        return lista




#dados = Fundamental('WEGE3')
#dados.get()
#print(dados.data)

