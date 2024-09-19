""""""  		  	   		 	   		  		  		    	 		 		   		 		  
"""  		  	   		 	   		  		  		    	 		 		   		 		  
Test a learner.  (c) 2015 Tucker Balch  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		 	   		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		 	   		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		 	   		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		  	   		 	   		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		 	   		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		 	   		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	   		  		  		    	 		 		   		 		  
or edited.  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		  	   		 	   		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		 	   		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		 	   		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		  	   		 	   		  		  		    	 		 		   		 		  
"""  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
import math  		  	   		 	   		  		  		    	 		 		   		 		  
import sys  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
import numpy as np  		  	   		 	   		  		  		    	 		 		   		 		  
import DTLearner as dt
import RTLearner as rt
import BagLearner as bl
import InsaneLearner as it  	   		 	   		  		  		    	 		 		   		 		  
import LinRegLearner as lrl  

def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def check_for_headers(data):
    first_row_values = data[0].strip().split(",")
    if all(is_numeric(value) for value in first_row_values[1:]):
        return 0
    else:
       return 1

def compute_correlations(data_x, data_y):
    correlations = np.zeros(data_x.shape[1])
    for i in range(data_x.shape[1]):
        correlations[i] = np.corrcoef(data_x[:, i], data_y)[0, 1]
    
    return correlations

def factor_selector(data_x, data_y):
    correlation_table = compute_correlations(data_x, data_y)
    max_correlation_index = np.argmax(np.abs(correlation_table))
    return max_correlation_index

        

def get_data(arg):
    inf = open(arg)  	
    unprocessed_data  = inf.readlines()
    header_start_index = check_for_headers(unprocessed_data)
    
    first_column_is_numeric = all(is_numeric(row.strip().split(",")[0]) for row in unprocessed_data)

    if first_column_is_numeric:
        data = np.array(  		  	   		 	   		  		  		    	 		 		   		 		  
            [list(map(float, s.strip().split(",")[:])) for s in unprocessed_data[header_start_index:]]  		  	   		 	   		  		  		    	 		 		   		 		  
        )  	
    else:
        data = np.array(  		  	   		 	   		  		  		    	 		 		   		 		  
            [list(map(float, s.strip().split(",")[1:])) for s in unprocessed_data[header_start_index:]]  		  	   		 	   		  		  		    	 		 		   		 		  
        )     

    inf.close()
    	    	   		 	   		  		  		    	 		 		   		 		  
    data_x = data[:, :-1]
    data_y = data[:, -1]

    return data_x, data_y
  		  	   		 	   		  		  		    	 		 		   		 		  
if __name__ == "__main__":  		  	   		 	   		  		  		    	 		 		   		 		  
    if len(sys.argv) != 2:  		  	   		 	   		  		  		    	 		 		   		 		  
        print("Usage: python testlearner.py <filename>")  		  	   		 	   		  		  		    	 		 		   		 		  
        sys.exit(1)

    data_x, data_y = get_data(sys.argv[1])
    reshaped_data_y = data_y.reshape(-1, 1)
    combined_data = np.hstack((data_x, reshaped_data_y))
    # build_tree(combined_data, 1)
    

    # compute how much of the data is training and testing  		  	   		 	   		  		  		    	 		 		   		 		  
    train_rows = int(0.6 * combined_data.shape[0])  		  	   		 	   		  		  		    	 		 		   		 		  
    test_rows = combined_data.shape[0] - train_rows  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
    # separate out training and testing data  		  	   		 	   		  		  		    	 		 		   		 		  
    train_x = combined_data[:train_rows, 0:-1]  		  	   		 	   		  		  		    	 		 		   		 		  
    train_y = combined_data[:train_rows, -1]  		  	   		 	   		  		  		    	 		 		   		 		  
    test_x = combined_data[train_rows:, 0:-1]  		  	   		 	   		  		  		    	 		 		   		 		  
    test_y = combined_data[train_rows:, -1]  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
    print(f"{test_x.shape}")  		  	   		 	   		  		  		    	 		 		   		 		  
    print(f"{test_y.shape}")  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
    # create a learner and train it  	
    dt_learner = dt.DTLearner(leaf_size = 1, verbose = True)    
    value = dt_learner.add_evidence(train_x, train_y)  	
    
    learner = lrl.LinRegLearner(verbose=True)  # create a LinRegLearner  		  	   		 	   		  		  		    	 		 		   		 		  
    learner.add_evidence(train_x, train_y)  # train it  		  	   		 	   		  		  		    	 		 		   		 		  
    print(learner.author())  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
    # evaluate in sample  		  	   		 	   		  		  		    	 		 		   		 		  
    pred_y = learner.query(train_x)  # get the predictions  		  	   		 	   		  		  		    	 		 		   		 		  
    rmse = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])  		  	   		 	   		  		  		    	 		 		   		 		  
    print()  		  	   		 	   		  		  		    	 		 		   		 		  
    print("In sample results")  		  	   		 	   		  		  		    	 		 		   		 		  
    print(f"RMSE: {rmse}")  		  	   		 	   		  		  		    	 		 		   		 		  
    c = np.corrcoef(pred_y, y=train_y)  		  	   		 	   		  		  		    	 		 		   		 		  
    print(f"corr: {c[0,1]}")  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
    # evaluate out of sample  		  	   		 	   		  		  		    	 		 		   		 		  
    pred_y = learner.query(test_x)  # get the predictions  		  	   		 	   		  		  		    	 		 		   		 		  
    rmse = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])  		  	   		 	   		  		  		    	 		 		   		 		  
    print()  		  	   		 	   		  		  		    	 		 		   		 		  
    print("Out of sample results")  		  	   		 	   		  		  		    	 		 		   		 		  
    print(f"RMSE: {rmse}")  		  	   		 	   		  		  		    	 		 		   		 		  
    c = np.corrcoef(pred_y, y=test_y)  		  	   		 	   		  		  		    	 		 		   		 		  
    print(f"corr: {c[0,1]}")  		  	   		 	   		  		  		    	 		 		   		 		  
