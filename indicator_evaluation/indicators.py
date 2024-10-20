import pandas as pd
import numpy as np

class Indicators(object):
    def __init__(self):  	
        pass

    def author(self):  		  	   		 	   		  		  		    	 		 		   		 		  
        """  		  	   		 	   		  		  		    	 		 		   		 		  
        :return: The GT username of the student  		  	   		 	   		  		  		    	 		 		   		 		  
        :rtype: str  		  	   		 	   		  		  		    	 		 		   		 		  
        """  		  	   		 	   		  		  		    	 		 		   		 		  
        return "dkassin3"

    def golden_death_cross(self, data, short_window=20, long_window=50):
        golden_death_cross = data.copy()
        short_col_name = f"sma_{short_window}_window"
        long_col_name = f"sma_{long_window}_window"
        golden_death_cross[short_col_name] = golden_death_cross.rolling(window=short_window).mean()
        golden_death_cross[long_col_name] = golden_death_cross.rolling(window=long_window).mean()
        golden_death_cross['golden_cross_signal'] = (golden_death_cross["sma_20_window"] > golden_death_cross["sma_20_window"]).astype(int)
        return golden_death_cross
        
    def binary_bollinger_bands(self, data, lookback=14):
        bollinger_bands_data = data.copy()
        sma = bollinger_bands_data.rolling(window=lookback, min_periods=lookback).mean()
        rolling_std = bollinger_bands_data.rolling(window=lookback, min_periods=lookback).mean()
        top_band = sma + (2 * rolling_std)
        bottom_band = sma - (2 * rolling_std)
        bbp = (bollinger_bands_data - bottom_band) / (top_band - bottom_band)
        buy_signal = (bbp.shift(1) < 0) & (bbp >= 0)
        sell_signal = (bbp.shift(1) > 1) & (bbp <= 1)

        signals = np.where(buy_signal, 1, np.where(sell_signal, -1 ,0))
        return signals
    
    def normalized_momentum_indicator(self, data, lookback=14):
        momentum_data = data.copy()
        momentum = (momentum_data / momentum_data.shift(lookback)) - 1
        min_momentum = momentum.min(skipna=True)
        max_momentum = momentum.max(skipna=True)
        if min_momentum == max_momentum:
            return np.zeros_like(momentum.values)
        normalized_momentum = 2 * (momentum - min_momentum) / (max_momentum - min_momentum) - 1
        return normalized_momentum.values

    def ema(self, data, lookback=14):
        ema_data = data.copy()
        ema_values = ema_data.ewm(span=lookback, adjust=False).mean()
        return ema_values.to_numpy()
    
    def stochastic_oscillator(self, data, lookback=14):
        stochastic_data = data.copy()
        high = stochastic_data.rolling(window=lookback).max()
        low = stochastic_data.rolling(window=lookback).min()
        percent_k = 100 * (data - low) / (high - low)
        percent_k = percent_k.fillna(0)
        return percent_k.to_numpy()


if __name__ == "__main__":  		  	   		 	   		  		  		    	 		 		   		 		  
    print("the secret clue is 'zzyzx'")  	
