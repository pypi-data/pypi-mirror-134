from rltrade.data import IBKRDownloader

demo = True
time_frame = '1 min' # options 1 min, 5 mins, 15 mins. 1 hour , 4 hours, 1 day 
train_period = ('2021-10-17','2021-11-18') #for training the model
test_period = ('2021-11-02','2021-12-20') #for trading and backtesting

csv_path = 'data/ibkrfutsingle1min.csv' # path with .csv extension

ticker_list = ['CLG2']
sec_types = ['FUT']
exchanges = ['NYMEX']
trades_per_stock = [2]

ib = IBKRDownloader(start_date = train_period[0], # first date
                    end_date = test_period[1], #last date
                    ticker_list = ticker_list,
                    time_frame=time_frame,
                    sec_types=sec_types,
                    exchanges=exchanges,
                    demo=demo)
                    
if time_frame == '1 day':
    df = ib.fetch_daily_data()
else:
    df = ib.fetch_data()

df = df.sort_values(by=['date','tic'])
df.to_csv(csv_path,index=False)