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
        self.create_charts(self.binary_bollinger_bands(prices), title="Binary Bollinger Bands Technical Indicator", xlabel="Date", ylabel="Binary Bollinger Bands")
        self.create_charts(self.normalized_momentum_indicator(prices), title="Normalized Momentum Indicator Technical Indicator", xlabel="Date", ylabel="Normalized Momentum Indicator")
        self.create_charts(self.ema(prices), title="EMA Technical Indicator", xlabel="Date", ylabel="EMA")
        self.create_charts(self.stochastic_oscillator(prices), title="Stochastic Oscillator Technical Indicator", xlabel="Date", ylabel="Stochastic Oscillator")


    def create_charts(self, df, symbol, signal_array, title="Stock prices", xlabel="Date", ylabel="Price"):  		  	   		 	   		  		  		    	 		 		   		 		  
        fig, ax1 = plt.subplots(figsize=(10, 6))
        df[symbol].plot(ax=ax1, color='blue', label=symbol)	  	   		 	   		  		  		    	 		 		   		 		  
        ax1.set_xlabel(xlabel)
        ax1.set_ylabel(ylabel, color='blue')
        ax1.tick_params(axis='y', labelcolor='blue')

        ax2 = ax1.twinx()
        signal_array.plot(ax=ax2, color='green', linestyle='--', label="Golden Death Cross")
        ax2.set_ylabel('Indicator Signal', color='green')
        ax2.tick_params(axis='y', labelcolor='green')
        plt.title(title)

        ax1.legend(loc='best')  # Legend for the price data
        ax2.legend(loc='best')

        plt.savefig(f'images/{title}.png')
        plt.close()

    def golden_death_cross(self, data, short_window=20, long_window=50):
        df = data.copy()
        short_col_name = f"sma_{short_window}_window"
        long_col_name = f"sma_{long_window}_window"
        df[short_col_name] = data.rolling(window=short_window).mean()
        df[long_col_name] = data.rolling(window=long_window).mean()
        df['signal'] = (df[short_col_name] > df[long_col_name]).astype(int)
        return df[['signal']]
        
    def binary_bollinger_bands(self, data, lookback=30):
        df = data.copy()
        sma = data.rolling(window=lookback, min_periods=lookback).mean()
        rolling_std = data.rolling(window=lookback, min_periods=lookback).std()
        top_band = sma + (2 * rolling_std)
        bottom_band = sma - (2 * rolling_std)
        bbp = (df - bottom_band) / (top_band - bottom_band)
        buy_signal = (bbp.shift(1) < 0) & (bbp >= 0)
        sell_signal = (bbp.shift(1) > 1) & (bbp <= 1)
        df['signal'] = np.where(buy_signal, 1, np.where(sell_signal, -1 ,0))
        return df[['signal']]
    
    def normalized_momentum_indicator(self, data, lookback=30, buy_threshold=0.5, sell_threshold=-0.5):
        df = data.copy()
        momentum = (df / df.shift(lookback)) - 1
        min_momentum = momentum.min(skipna=True).item()
        max_momentum = momentum.max(skipna=True).item()
        if min_momentum == max_momentum:
            df['momentum'] = np.zeros_like(momentum)
        else:
            normalized_momentum = 2 * (momentum - min_momentum) / (max_momentum - min_momentum) - 1
            df['momentum'] = normalized_momentum
        df['signal'] = np.where(df['momentum'] > buy_threshold, 1, np.where(df['momentum'] < sell_threshold, -1, 0))
        return df[['signal']]

    def ema(self, data, lookback=14):
        df = data.copy()
        df['ema'] = df.ewm(span=lookback, adjust=False).mean()
        df['signal'] = np.where(df.iloc[:, 0] > df['ema'], 1, -1)
        return df[['signal']]
    
    def stochastic_oscillator(self, data, lookback=30, oversold=20, overbought=80):
        df = data.copy()
        high = df.rolling(window=lookback).max()
        low = df.rolling(window=lookback).min()
        percent_k = 100 * (data - low) / (high - low)
        percent_k = percent_k.fillna(0)
        df['percent_k'] = percent_k
        df['signal'] = np.where(df['percent_k'] < oversold, 1, np.where(df['percent_k'] > overbought, -1, 0))
        return df[['signal']]
    
def main():
    indicators = Indicators()
    indicators.create_all_indicator_charts()

if __name__ == "__main__":  		  	   		 	   		  		  		    	 		 		   		 		  
    print("the secret clue is 'zzyzx'")  	
    main()