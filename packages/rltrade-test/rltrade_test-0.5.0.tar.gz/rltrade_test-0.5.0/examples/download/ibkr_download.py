from rltrade.data import IBKRDownloader

demo = True
time_frame = '4 hours' # options 1 min, 5 mins, 15 mins. 1 hour , 4 hours, 1 day 
train_period = ('2021-10-17','2021-11-18') #for training the model
test_period = ('2021-11-02','2021-12-20') #for trading and backtesting

csv_path = 'data/ibkrcontfutsingle4hours.csv' # path with .csv extension

ticker_list = ['CL']
sec_types = ['CONTFUT']
exchanges = ['NYMEX']

change_name = True # for changing name of ticker else keep False
ticker_list2 = ['CLG2']
sec_types2 = ['FUT']
exchanges2 = ['NYMEX']

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

if change_name:
    for i in range(len(ticker_list)):
        df.loc[df['tic']==ticker_list[i],'tic'] = ticker_list2[i]
        df.loc[df['tic']==ticker_list[i],'sec'] = sec_types2[i]
        df.loc[df['tic']==ticker_list[i],'exchange'] = exchanges2[i]

df.to_csv(csv_path,index=False)