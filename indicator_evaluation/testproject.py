import datetime as dt
import pandas as pd 
import numpy as np
from util import get_data
import indicators as Id
import TheoreticallyOptimalStrategy as tos
from marketsimcode import compute_portvals

def author():  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    :return: The GT username of the student  		  	   		 	   		  		  		    	 		 		   		 		  
    :rtype: str  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    return "dkassin3"

def generate_performance_table(benchmark_port_values, port_values, output_file="performance_table.txt"):
    port_cumulative_return = (port_values.iloc[-1] / port_values.iloc[0]) - 1
    benchmark_cumulative_return = (benchmark_port_values.iloc[-1] / benchmark_port_values.iloc[0]) - 1
    benchmark_daily_returns = benchmark_port_values.pct_change().dropna()
    portfolio_daily_returns = port_values.pct_change().dropna()
    benchmark_std = benchmark_daily_returns.std()
    portfolio_std = portfolio_daily_returns.std()
    benchmark_mean = benchmark_daily_returns.mean()
    portfolio_mean = portfolio_daily_returns.mean()
    performance_data = {
        "Metric": [
            "Cumulative Return", 
            "Stdev of Daily Returns", 
            "Mean of Daily Returns"
        ],
        "Benchmark": [
            round(benchmark_cumulative_return, 6), 
            round(benchmark_std, 6), 
            round(benchmark_mean, 6)
        ],
        "Portfolio": [
            round(port_cumulative_return, 6), 
            round(portfolio_std, 6), 
            round(portfolio_mean, 6)
        ]
    }
    performance_table = pd.DataFrame(performance_data)
    with open(output_file, "w") as f:
        f.write(performance_table.to_string(index=False))

if __name__ == "__main__":  
    sd,ed = dt.datetime(2008, 1, 1), dt.datetime(2009,12,31)
    symbols = ["JPM"]
    prices = get_data(symbols, pd.date_range(sd, ed), addSPY=False).dropna(axis=0)
    indicators = Id.Indicators()
    golden_death_cross = indicators.golden_death_cross(prices)
    indicators.create_charts(prices, symbols, golden_death_cross, title="JPM Golden Death Cross", xlabel="Date", ylabel="Price")
    binary_bollinger_bands = indicators.binary_bollinger_bands(prices)
    indicators.create_charts(prices, symbols, binary_bollinger_bands, title="JPM Binary Bollinger Bands", xlabel="Date", ylabel="Price")
    normalized_momentum_indicator = indicators.normalized_momentum_indicator(prices)
    indicators.create_charts(prices, symbols, normalized_momentum_indicator, title="JPM Normalized Momentum Indicator", xlabel="Date", ylabel="Price")
    ema = indicators.ema(prices)
    indicators.create_charts(prices, symbols, ema, title="EMA Indicator", xlabel="Date", ylabel="Price")
    stochastic_oscillator = indicators.stochastic_oscillator(prices)
    indicators.create_charts(prices, symbols, stochastic_oscillator, title="JPM Stochastic Oscillator", xlabel="Date", ylabel="Price")
    
    df_trades = tos.testPolicy(symbols[0], sd, ed)
    orders = pd.DataFrame(index=df_trades.index, columns=['Symbol','Order','Shares'])
    orders['Symbol'] = symbols[0]
    orders['Order'] = np.where(df_trades['Trades'] > 0, "BUY", "SELL")
    orders["Shares"] = abs(df_trades)
    orders = orders[orders['Shares'] != 0]
    bench_orders = pd.DataFrame(index=df_trades.index, columns=['Symbol','Order','Shares'])
    bench_orders['Symbol'] = symbols[0]
    bench_orders['Order'][0] = "BUY"
    bench_orders['Shares'][0] = 1000
    last_index = orders.index[-1]
    bench_orders['Symbol'][last_index] = symbols[0]
    bench_orders['Order'][last_index] = "SELL"
    bench_orders['Shares'][last_index] = 1000   
    bench_orders = bench_orders.dropna(subset=['Shares'])
    port_values = compute_portvals(orders)
    benchmark_port_values = compute_portvals(bench_orders)
    generate_performance_table(benchmark_port_values, port_values)
    


    # import pdb; pdb.set_trace()


    

