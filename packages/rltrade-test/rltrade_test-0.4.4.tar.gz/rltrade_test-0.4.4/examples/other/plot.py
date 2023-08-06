from rltrade.backtests import plot_chart_forex, plot_chart_stocks

#for forex
path = 'models/daytrades/forex-train11-single' #path where model is saved
symbol = 'EURUSD'
plot_chart_forex(path,symbol)

# for stocks
path = 'models/stocks/allstocks' #path where model is saved
symbol = 'pall'
plot_chart_stocks(path,symbol)