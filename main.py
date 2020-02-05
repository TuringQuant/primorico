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
    agg_roe_roic.columns = ['mean_roe', 'mean_roic']

    df2 = pd.merge(df, agg_roe_roic, how='inner', on='setor')

    df2['roe_mt_avg'] = df2['ROE'] > df2['mean_roe']
    df2['roic_mt_avg'] = df2['ROIC'] > df2['mean_roic']

    df2['pl_lt_15'] = df2['P/L'] < 15

    #TODO encontrar endividamento liquido / ebit e filtrar por menor que 3

    df_filtered = df2[df2['roe_mt_avg'] & df2['roic_mt_avg'] & df2['pl_lt_15']]
    
    return None

if __name__ == '__main__':
    main()