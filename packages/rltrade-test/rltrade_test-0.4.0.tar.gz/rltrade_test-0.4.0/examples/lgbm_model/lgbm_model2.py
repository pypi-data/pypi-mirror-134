import asyncio
import matplotlib.pyplot as plt
import seaborn as sns
import lightgbm as lgb
import pandas as pd
from rltrade import config
from metaapi_cloud_sdk import MetaApi
from rltrade.data import OandaDownloader,DayTradeFeatureEngineer


"""
time_frame - last date available
4h  - '2017-12-01'
1h  - '2020-06-19'
30m - '2021-11-18'
15m - '2021-12-03'
5m -  '2021-10-01'
"""

time_frame = "5m" # available 5m, 15m, 30m, 1h, 4h
train_period = ('2021-10-01','2021-12-01') #for training the model
test_period = ('2021-12-01','2021-12-20') 
start_time = "00:00:00"
end_time = "23:55:00" 

token = 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiIzYTI0YzMwYzFkNDRmZGFmZGI3NmVmYTUxZmQ2MDJmMCIsInBlcm1pc3Npb25zIjpbXSwidG9rZW5JZCI6IjIwMjEwMjEzIiwiaWF0IjoxNjM5NDkwMzEzLCJyZWFsVXNlcklkIjoiM2EyNGMzMGMxZDQ0ZmRhZmRiNzZlZmE1MWZkNjAyZjAifQ.DhA6Q-AlWNssi8ScOaWy2Bxo4Hebgw94BDE6PiT9J-TvsuF7OqvdYBQ1IWYEMtsYsg3Ij8p8Wpvn8ZdZeHRkR3vLcQnMH-GZj3DyYkeqovQKk6U3uOobV-GS3meJPZYfw2zItuTDBWxuHDZsVW1ZvF4sItBDmsWIe2svF0NmKE1nu-ephcYVzYo9grr93de_h-QwlP-yeZFeGEqrz3-q5gYWcARJsIR1BX63zePuDHkUK9k5W9Rm28WdB87MHEyMSWhcAZDf8si5MwsPYC3wpzNtzGqORF3UY-w5EmolCtSPMBqM7AI0LKc1n8GPS3ZhnvHkfGhWEdb5gKlCWwshk30tICN24C1bZG06zfs450oLm8ih9ls5oyshcg_xwawNvsA305D7Siz0Pzqr1xnUA8zMz8cVUFZtjdBWCfot05_ziVO0x_mApVyAVC2OA-Sh61RtkwNNpg4bTCzK30OpdiS9GO0HLgnepnuwWOO0T9DTzTAJUxyJcXOzcWcXGdMTWaGAp5ranytU97k8GxDHa5jOS_WvphL24C8QA6of0pYZwHM3Ul5Aw351H1SbJLIqs2AChDoUnpJb9OZb-27ESLZgM1mhU6rwzt8lRRbxUHaXSv5QpM29nPm3k5KrFSv-UTXiX6oU9c1nNh3qLb6FKV_B1CQarcvyx66iUg-1DcU'
domain = 'agiliumtrade.agiliumtrade.ai'
account_id = 'ddc8fb93-e0f5-4ce8-b5d5-8290d23fc143'

ticker_list = ['AUDUSD','EURUSD','NZDUSD','USDCAD','USDCHF','GBPUSD']
# ticker_list = ['USDCAD','USDCHF']
sec_types = ['-'] * len(ticker_list)
exchanges = ['-'] * len(ticker_list)

async def download_data():
    api = MetaApi(token,{'domain':domain})

    try:
        account = await api.metatrader_account_api.get_account(account_id)

        if account.state != 'DEPLOYED':
            print("Deploying account")
            await account.deploy()
        else:
            print('Account already deployed')
        if account.connection_status != 'CONNECTED':
            print('Waiting for API server to connect to broker (may take couple of minutes)')
            await account.wait_connected()
        else:
            print("Account already connected")
    
        oa = OandaDownloader(
            account = account,
            time_frame=time_frame,
            start_date=train_period[0],
            end_date=test_period[1],
            start_time=start_time,
            end_time=end_time,
            ticker_list=ticker_list)

        df = await oa.fetch_daily_data()
        
        return df

    except Exception as err:
            print(api.format_error(err))

df = asyncio.run(download_data())


tech_indicators = config.STOCK_INDICATORS_LIST # indicators from stockstats
additional_indicators = config.ADDITIONAL_DAYTRADE_INDICATORS

all_indicators = tech_indicators + additional_indicators

fe = DayTradeFeatureEngineer(additional_indicators=additional_indicators,
                    stock_indicator_list=tech_indicators,
                    cov_matrix=True)

df = fe.create_data(df)

# df = pd.read_csv('testdata/testdata.csv')
# df['date'] = pd.to_datetime(df['date'])
# df = fe.create_data(df)
# df.to_csv('testdata/testdata.csv',index=False)
# df = pd.read_csv('testdata/testdata.csv')
# df['date'] = pd.to_datetime(df['date'])

df['target'] = df.groupby('tic')['close'].shift(-1)
df = df.dropna()

train = fe.time_series_split(df, start = train_period[0], end = train_period[1])
test = fe.time_series_split(df, start = test_period[0], end = test_period[1])

x_train = train[all_indicators].values
y_train = train['target'].values
x_test = test[all_indicators].values
y_test = test['target'].values


params = {'reg_alpha': 6.147694913504962,
 'reg_lambda': 0.002457826062076097,
 'colsample_bytree': 0.3,
 'subsample': 0.8,
 'learning_rate': 0.001,
 'max_depth': 20,
 'num_leaves': 111,
 'min_child_samples': 285,
 'random_state': 48,
 'verbose':-1,
 'n_estimators': 10_000,
 'metric': 'rmse',
 'cat_smooth': 39}

lgb_train = lgb.Dataset(x_train,y_train)
lgb_test = lgb.Dataset(x_test,y_test)

lgb_model = lgb.train(
    params,
    lgb_train,
    valid_sets=[lgb_train,lgb_test],
    verbose_eval=1000,
    early_stopping_rounds=800,
)

def plot_feature_importance(model,features,plot=False):
    feature_importance = pd.DataFrame({"feature":features,"importance":model.feature_importance(importance_type='gain')})
    feature_importance = feature_importance.sort_values(by='importance',ascending=False)
    
    if plot:
        plt.figure(figsize=(10,10))
        sns.barplot(data=feature_importance,x='importance',y='feature')
        
        for idx, v in enumerate(feature_importance.importance):
                plt.text(v, idx, "  {:.2e}".format(v))
        
        plt.show()
    return feature_importance

feature_importance = plot_feature_importance(lgb_model,all_indicators)
print(feature_importance)
feature_importance.to_csv('featureimportance.csv',index=False)