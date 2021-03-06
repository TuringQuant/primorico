import pandas as pd
from data.get.fundamentus import Fundamentus
from data.get.tickers import get_tickers
from data.get.info import get_info

def tickers_to_csv():
    """
    Cria csv com todos tickers das empresas listadas na B3
    """
    tickers =  get_tickers()
    s_tickers = pd.Series(tickers)
    s_tickers.to_csv('./data/files/tickers.csv', index=False, header=False)

    return None

def info_to_csv():
    """
    Cria csv com dados dos setores dos tickers das empresas listadas na B3
    """
    tickers =  pd.read_csv('./data/files/tickers.csv')
    info = get_info()
    aux_list = []
    for ticker in tickers:
        try:
            info_ticker = info[ticker[:4]]
        except:
            info_ticker = ['', '', '']
        aux_dict = {}
        aux_dict['ticker'] = ticker
        aux_dict['setor'] = info_ticker[0]
        aux_dict['subsetor'] = info_ticker[1]
        aux_dict['segmento'] = info_ticker[2]
        aux_list.append(aux_dict)

    df_info_tickers = pd.DataFrame(aux_list)
    df_info_tickers.to_csv('./data/files/info_tickers.csv', index=False)

    return None

def fundamental_to_csv():
    """
    Cria csv com dados fundamentalistas dos tickers das empresas listadas na B3.
    Usando o site fundamentus.com.br
    """
    tickers = pd.read_csv('./data/csv/tickers.csv', header=None)[0]
    #info = pd.read_csv('./data/info_tickers.csv')

    f = Fundamentus(list(tickers))
    f.get('fundamentalista')

    df = pd.DataFrame(f.data)

    df.to_csv('./data/files/fundamental.csv', index=False)

    return None

def balanco_to_csv():
    """
    Cria csv com dados de balanco dos tickers das empresas listadas na B3.
    Usando o site fundamentus.com.br
    """
    tickers = pd.read_csv('./data/csv/tickers.csv', header=None)[0]
    #info = pd.read_csv('./data/info_tickers.csv')

    f = Fundamentus(list(tickers))
    f.get('balanco')

    df = pd.DataFrame(f.data)

    df.to_csv('./data/files/balance.csv', index=False)

    return None 