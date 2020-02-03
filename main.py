import json
import os.path
from data.data import (fundamental_to_csv, tickers_to_csv, info_to_csv)
import pandas as pd

def main():
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

    tickers = pd.read_csv('./data/csv/tickers.csv', header=None)[0]
    info = pd.read_csv('./data/csv/info_tickers.csv')
    fundamental = pd.read_csv('./data/csv/fundamental.csv')

if __name__ == '__main__':
    main()