import pandas as pd
import numpy as np
import datetime as dt
from util import get_data
import matplotlib.pyplot as plt

class Indicators(object):
    def __init__(self):  	
        pass

    def author(self):  		  	   		 	   		  		  		    	 		 		   		 		  
        """  		  	   		 	   		  		  		    	 		 		   		 		  
        :return: The GT username of the student  		  	   		 	   		  		  		    	 		 		   		 		  
        :rtype: str  		  	   		 	   		  		  		    	 		 		   		 		  
        """  		  	   		 	   		  		  		    	 		 		   		 		  
        return "dkassin3"
    
    def create_all_indicator_charts(self, symbols = ['JPM'], start_date = dt.datetime(2008, 1, 1), end_date = dt.datetime(2009, 12, 31)):
        prices = get_data(symbols, pd.date_range(start_date, end_date), addSPY=False).dropna(axis=0)
        self.create_charts(self.golden_death_cross(prices), title="Golden Death Cross Technical Indicator", xlabel="Date", ylabel="Golden Death Cross")
        import pdb; pdb.set_trace()
        self.create_charts(self.binary_bollinger_bands(prices), title="Binary Bollinger Bands Technical Indicator", xlabel="Date", ylabel="Binary Bollinger Bands")
        self.create_charts(self.normalized_momentum_indicator(prices), title="Normalized Momentum Indicator Technical Indicator", xlabel="Date", ylabel="Normalized Momentum Indicator")
        self.create_charts(self.ema(prices), title="EMA Technical Indicator", xlabel="Date", ylabel="EMA")
        self.create_charts(self.stochastic_oscillator(prices), title="Stochastic Oscillator Technical Indicator", xlabel="Date", ylabel="Stochastic Oscillator")


    def create_charts(self, df, title="Stock prices", xlabel="Date", ylabel="Price"):  		  	   		 	   		  		  		    	 		 		   		 		  
        ax = df.plot(title=title, fontsize=12)  		  	   		 	   		  		  		    	 		 		   		 		  
        ax.set_xlabel(xlabel)  		  	   		 	   		  		  		    	 		 		   		 		  
        ax.set_ylabel(ylabel)
        plt.savefig('images/f"{title}.png')
        plt.close()

    def golden_death_cross(self, data, short_window=20, long_window=50):
        df = data.copy()
        short_col_name = f"sma_{short_window}_window"
        long_col_name = f"sma_{long_window}_window"
        df[short_col_name] = df.rolling(window=short_window).mean()
        df[long_col_name] = df.rolling(window=long_window).mean()
        df['signal'] = (df["sma_20_window"] > df["sma_20_window"]).astype(int)
        import pdb; pdb.set_trace()
        return df[['signal']]
        
    def binary_bollinger_bands(self, data, lookback=14):
        df = data.copy()
        sma = df.rolling(window=lookback, min_periods=lookback).mean()
        rolling_std = df.rolling(window=lookback, min_periods=lookback).mean()
        top_band = sma + (2 * rolling_std)
        bottom_band = sma - (2 * rolling_std)
        bbp = (df - bottom_band) / (top_band - bottom_band)
        buy_signal = (bbp.shift(1) < 0) & (bbp >= 0)
        sell_signal = (bbp.shift(1) > 1) & (bbp <= 1)

        df['signals'] = np.where(buy_signal, 1, np.where(sell_signal, -1 ,0))
        return df['signals']
    
    def normalized_momentum_indicator(self, data, lookback=14):
        df = data.copy()
        momentum = (df / df.shift(lookback)) - 1
        min_momentum = momentum.min(skipna=True)
        max_momentum = momentum.max(skipna=True)
        if min_momentum == max_momentum:
            return np.zeros_like(momentum.values)
        else:
            normalized_momentum = 2 * (momentum - min_momentum) / (max_momentum - min_momentum) - 1
        df['momentum'] = normalized_momentum
        return df[['momentum']]

    def ema(self, data, lookback=14):
        df = data.copy()
        df['ema'] = df.ewm(span=lookback, adjust=False).mean()
        return df[['ema']]
    
    def stochastic_oscillator(self, data, lookback=14):
        df = data.copy()
        high = df.rolling(window=lookback).max()
        low = df.rolling(window=lookback).min()
        percent_k = 100 * (data - low) / (high - low)
        percent_k = percent_k.fillna(0)
        df['percent_k'] = percent_k
        return df[['percent_k']]
    
def main():
    indicators = Indicators()
    indicators.create_all_indicator_charts()

if __name__ == "__main__":  		  	   		 	   		  		  		    	 		 		   		 		  
    print("the secret clue is 'zzyzx'")  	
    main()