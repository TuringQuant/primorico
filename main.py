import json
import os.path
from data.data import (fundamental_to_csv, tickers_to_csv, info_to_csv)
import pandas as pd

def get_data():

    if os.path.isfile('./data/csv/tickers.csv'):
        pass
    else:
        tickers_to_csv()
    if os.path.isfile('./data/csv/info_tickers.csv'):
        pass
    else:
        info_to_csv()
    if os.path.isfile('./data/csv/fundamental.csv'):
        pass
    else:
        info_to_csv()
    return None

def main():
    get_data()

    info = pd.read_csv('./data/csv/info_tickers.csv')
    fundamental = pd.read_csv('./data/csv/fundamental.csv')

    df_merged = pd.merge(fundamental, info, how='inner', on='ticker')

    df = df_merged[['ticker', 'ROE', 'ROIC', 'P/L', 'EV / EBIT', 'setor']]

    agg_roe_roic = df[['setor', 'ROE', 'ROIC']].groupby('setor').mean()

    #TODO criar flags de roe maior que a media
    #TODO criar flag de roic maior que a media
    #TODO filtrar por p/l < 15
    #TODO encontrar endividamento liquido / ebit e filtrar por menor que 3
    
    #df['avg_roe'] = df.index.apply(lambda index: agg_roe_roic.loc[df.iloc[index]['setor']]['ROE'])
    #df['avg_roic'] = df.apply(lambda x: x['setor']agg_roe_roic.loc[x['setor']]['ROIC'])
    
    return None

if __name__ == '__main__':
    main()