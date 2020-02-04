import requests
from bs4 import BeautifulSoup

class Fundamentus:

    base_url = 'https://www.fundamentus.com.br/detalhes.php?papel='

    def __init__(self, tickers: list):

        self.tickers = tickers
        self.data = []

    def get(self):

        fundamental = []
        for ticker in self.tickers:
            
            print(f'Requisitando dados {ticker} ...')

            try:
                url = self.base_url + ticker
                response = requests.get(url)

                soup = BeautifulSoup(response.content, 'html.parser')

                alltables = soup.find_all('table', 'w728')
                t = alltables[2]

                label = t.find_all('td', {'class': 'label'})
                content = t.find_all('td', {'class': 'data'})
            except:
                print(f'Não foi possível obter dados de {ticker}')
                continue

            #print(f'Convertendo dados de {ticker} ...')
            ticker_data = {}
            for l, c in zip(label, content):
                data_label = l.find('span', {'class': 'txt'}).getText()
                data_content = c.getText()
                if self.fix_string(data_label):
                    ticker_data[data_label] = self.string_to_float(data_content)
            ticker_data['ticker'] = ticker

            fundamental.append(ticker_data)

        self.data = fundamental

    @staticmethod
    def string_to_float(string):
        is_percentage = True if '%' in string else False
        replaced_string = string.replace('\n', '') \
            .replace('%', '').replace(' ', '').replace('.', '').replace(',', '.')
        if replaced_string == '-':
            return 0.0
        if is_percentage:
            return float(replaced_string) / 100
        return float(replaced_string)

    @staticmethod
    def fix_string(string):
        return string.replace(' ', '').replace('\n', '')
