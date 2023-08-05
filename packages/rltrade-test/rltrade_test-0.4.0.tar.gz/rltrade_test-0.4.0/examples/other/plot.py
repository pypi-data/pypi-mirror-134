from rltrade.backtests import plot_chart_forex, plot_chart_stocks

#for forex
path = 'models/dailytrade/forex-train10' #path where model is saved
symbol = 'USDCAD'
plot_chart_forex(path,symbol)

# for stocks
path = 'models/stocks/allstocks' #path where model is saved
symbol = 'pall'
plot_chart_stocks(path,symbol)