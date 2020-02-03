import json
import os.path
from data.fundamental import Fundamentus
from tickers.tickers import get_tickers
from tickers.info import get_info
import pandas as pd

def main():
    if os.path.isfile('./data/tickers.csv'):
        pass
    else:
        tickers_to_csv()
    if os.path.isfile('./data/info_tickers.csv'):
        pass
    else:
        info_to_csv()

    tickers = pd.read_csv('./data/tickers.csv', header=None)[0]
    info = pd.read_csv('./data/info_tickers.csv')
    fundamental = pd.read_csv('/data/fundamental.csv')

if __name__ == '__main__':
    main()