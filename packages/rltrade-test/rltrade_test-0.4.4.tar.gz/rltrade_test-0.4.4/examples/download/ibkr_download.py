from rltrade import config
from rltrade.data import IBKRDownloader
from rltrade.backtests import get_metrics

demo = True
train_period = ('2012-01-01','2020-08-01') #for training the model
test_period = ('2020-08-02','2021-12-29') #for trading and backtesting

csv_path = 'testdata/ibkr.csv' # path with .csv extension

# ticker_list = config.ALL_STOCKS_LIST
ticker_list = ['pall', 'rio', 'spy', 'tlt', 'jbss', 'aapl']
sec_types = ['STK'] * len(ticker_list)
exchanges = ['SMART'] * len(ticker_list)

print('Downloading Data')
ib = IBKRDownloader(start_date = train_period[0], # first date
                    end_date = test_period[1], #last date
                    ticker_list = ticker_list,
                    sec_types=sec_types,
                    exchanges=exchanges,
                    demo=demo,)

df = ib.fetch_data()

df.to_csv(csv_path)

