import json
import os.path
from data.create import (fundamental_to_csv, tickers_to_csv, info_to_csv)
import pandas as pd

def get_data():

    if os.path.isfile('./data/files/tickers.csv'):
        pass
    else:
        tickers_to_csv()
    if os.path.isfile('./data/files/info_tickers.csv'):
        pass
    else:
        info_to_csv()
    if os.path.isfile('./data/files/fundamental.csv'):
        pass
    else:
        info_to_csv()
    return None

def main():
    get_data()

    info = pd.read_csv('./data/files/info_tickers.csv')
    fundamental = pd.read_csv('./data/files/fundamental.csv')

    df_merged = pd.merge(fundamental, info, how='inner', on='ticker')

    df = df_merged[['ticker', 'ROE', 'ROIC', 'P/L', 'EV / EBIT', 'setor']]

    agg_roe_roic = df[['setor', 'ROE', 'ROIC']].groupby('setor').mean()
    agg_roe_roic.columns = ['mean_roe', 'mean_roic']

    df2 = pd.merge(df, agg_roe_roic, how='inner', on='setor')

    df2['roe_mt_avg'] = df2['ROE'] > df2['mean_roe']
    df2['roic_mt_avg'] = df2['ROIC'] > df2['mean_roic']

    df2['pl_lt_15'] = df2['P/L'] < 15

    #TODO encontrar endividamento liquido / ebit e filtrar por menor que 3

    df_filtered = df2[df2['roe_mt_avg'] & df2['roic_mt_avg'] & df2['pl_lt_15']] \
        .drop(
            ['roe_mt_avg', 'roic_mt_avg', 'pl_lt_15'],
            axis = 1
        )

    df_filtered.sort_values(by='ticker').to_csv('./data/files/filtered_data.csv', index=False)
    
    return None

if __name__ == '__main__':
    main()