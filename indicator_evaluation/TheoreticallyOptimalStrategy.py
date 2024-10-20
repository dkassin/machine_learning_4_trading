import pandas as pd
import numpy as np
from util import get_data
import datetime as dt

def author():  		  	   		 	   		  		  		    	 		 		   		 		  
        """  		  	   		 	   		  		  		    	 		 		   		 		  
        :return: The GT username of the student  		  	   		 	   		  		  		    	 		 		   		 		  
        :rtype: str  		  	   		 	   		  		  		    	 		 		   		 		  
        """  		  	   		 	   		  		  		    	 		 		   		 		  
        return "dkassin3"

def testPolicy(symbol='JPM', sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011,12,31), sv = 100000):
        prices = get_data([symbol], pd.date_range(sd, ed), False).dropna()
        prices['future_returns'] = prices.diff().shift(-1)
        prices['signals'] = np.where(prices['future_returns'] > 0, 1, np.where(prices['future_returns'] < 0, -1, 0))
        df_trades = pd.DataFrame(data=0.0, columns=["Trades"], index=prices.index)
        current_position = 0
        
        for i in range(len(prices) - 1): 
                signal = prices['signals'].iloc[i]
                prev_day = prices['signals'].iloc[i - 1]
                
                if i == 0:
                        if signal == 1:
                                current_position = 1000
                                df_trades.iloc[i] = 1000
                        elif signal == -1:
                                current_position = -1000
                                df_trades.iloc[i, 0] = -1000
                        continue
                
                if signal == prev_day:
                        df_trades.iloc[i, 0] = 0
                else:   
                        if signal == -1 and current_position > 0:
                                trade_size = -2000
                                current_position += trade_size
                                df_trades.iloc[i, 0] = trade_size
                        elif signal == 1 and current_position < 0:
                                trade_size = 2000        
                                current_position += 2000
                                df_trades.iloc[i, 0] = 2000
  
        prices['df_trades'] = df_trades
        return df_trades

if __name__ == "__main__":  
        trades = testPolicy()
        