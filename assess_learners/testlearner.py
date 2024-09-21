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
import random	 		  	   		 	   		  		  		    	 		 		   		 		  
import numpy as np  		  	   		 	   		  		  		    	 		 		   		 		  
import DTLearner as dt
import RTLearner as rt
import BagLearner as bl
import InsaneLearner as it  	   		 	   		  		  		    	 		 		   		 		  
import LinRegLearner as lrl  
import matplotlib.pyplot as plt	



def gtid():  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    :return: The GT ID of the student  		  	   		 	   		  		  		    	 		 		   		 		  
    :rtype: int  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    return 904063414  

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
    random.seed(gtid())	  	   		 	   		  		  		    	 		 		   		 		  
    if len(sys.argv) != 2:  		  	   		 	   		  		  		    	 		 		   		 		  
        print("Usage: python testlearner.py <filename>")  		  	   		 	   		  		  		    	 		 		   		 		  
        sys.exit(1)
        
    np.set_printoptions(suppress=True)
    
    data_x, data_y = get_data(sys.argv[1])
    reshaped_data_y = data_y.reshape(-1, 1)
    combined_data = np.hstack((data_x, reshaped_data_y))
  		  	   		 	   		  		  		    	 		 		   		 		  
    train_rows = int(0.6 * combined_data.shape[0])  		  	   		 	   		  		  		    	 		 		   		 		  
    test_rows = combined_data.shape[0] - train_rows  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
    # separate out training and testing data  		  	   		 	   		  		  		    	 		 		   		 		  
    train_x = combined_data[:train_rows, 0:-1]  		  	   		 	   		  		  		    	 		 		   		 		  
    train_y = combined_data[:train_rows, -1]  		  	   		 	   		  		  		    	 		 		   		 		  
    test_x = combined_data[train_rows:, 0:-1]  		  	   		 	   		  		  		    	 		 		   		 		  
    test_y = combined_data[train_rows:, -1]  		  	   		 	   		  		  		    	 		 		   		 		     	   		  		  		    	 		 		   		 		  
    print(f"{test_x.shape}")  		  	   		 	   		  		  		    	 		 		   		 		  
    print(f"{test_y.shape}")  	


    # Experiment 1 

    max_leaf_size = 25
    experiment_1_learners = np.empty(max_leaf_size, dtype=object)

    # Model Training for models up to max leaf size
    for i in range(max_leaf_size):
        experiment_1_learners[i] = dt.DTLearner(leaf_size=(i+1))
        experiment_1_learners[i].add_evidence(train_x,train_y)

    # import pdb; pdb.set_trace()
    
    training_rmse = np.zeros(max_leaf_size) 
    training_corr = np.zeros(max_leaf_size)
    
    for i in range(max_leaf_size):
        y_pred_train = experiment_1_learners[i].query(train_x)
        training_rmse[i] = math.sqrt(((train_y - y_pred_train) ** 2).sum() / train_y.shape[0])  
        training_corr[i] = np.corrcoef(y_pred_train, y=train_y)[0,1]  

    testing_rmse = np.zeros(max_leaf_size)
    testing_corr = np.zeros(max_leaf_size)
    for i in range(max_leaf_size):
        y_pred_test = experiment_1_learners[i].query(test_x)
        testing_rmse[i] = math.sqrt(((test_y - y_pred_test) ** 2).sum() / test_y.shape[0])
        testing_corr[i] = np.corrcoef(y_pred_test, y=test_y)[0,1]  

    # import pdb; pdb.set_trace()

    plt.figure(figsize=(10,6))
    plt.plot(range(1,max_leaf_size + 1), training_rmse, label = 'Training RMSE', color = 'blue')
    plt.plot(range(1,max_leaf_size + 1), testing_rmse, label = 'Testing RMSE', color = 'green')
    plt.xlabel('Leaf Size', fontsize=14)
    plt.ylabel('RMSE', fontsize=14)
    plt.title('Leaf Size impact on RMSE', fontsize=16)
    plt.legend(loc=0, fontsize=12)
    plt.tight_layout()
    plt.savefig('images/leaf_ssize_impact_on_rmse.png')

    plt.figure(figsize=(10,6))
    plt.plot(range(1,max_leaf_size + 1), training_corr, label = 'Training Corr', color = 'blue')
    plt.plot(range(1,max_leaf_size + 1), testing_corr, label = 'Testing Corr', color = 'green')
    plt.xlabel('Leaf Size', fontsize=14)
    plt.ylabel('Correlation', fontsize=14)
    plt.title('Leaf Size impact on Correlation', fontsize=16)
    plt.legend(loc=0, fontsize=12)
    plt.tight_layout()
    plt.savefig('images/leaf_size_impact_on_corr.png')




  		  	   		 	   		  		  		    	 		 		   		 		  
    # evaluate in sample  		  	   		 	   		  		  		    	 		 		   		 		  
    # pred_y = dt_learner.query(train_x)  # get the predictions  		  	   		 	   		  		  		    	 		 		   		 		  
    		  	   		 	   		  		  		    	 		 		   		 		  
    # print()  		  	   		 	   		  		  		    	 		 		   		 		  
    # print("In sample results")  		  	   		 	   		  		  		    	 		 		   		 		  
    # print(f"RMSE: {rmse}")  		  	   		 	   		  		  		    	 		 		   		 		  
    # c = np.corrcoef(pred_y, y=train_y)  		  	   		 	   		  		  		    	 		 		   		 		  
    # print(f"corr: {c[0,1]}")  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
    # # evaluate out of sample  		  	   		 	   		  		  		    	 		 		   		 		  
    # # pred_y = dt_learner.query(test_x)  # get the predictions  		  	   		 	   		  		  		    	 		 		   		 		  
    # # rmse = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])  		  	   		 	   		  		  		    	 		 		   		 		  
    # print()  		  	   		 	   		  		  		    	 		 		   		 		  
    # print("Out of sample results")  		  	   		 	   		  		  		    	 		 		   		 		  
    # print(f"RMSE: {rmse}")  		  	   		 	   		  		  		    	 		 		   		 		  
    # c = np.corrcoef(pred_y, y=test_y)  		  	   		 	   		  		  		    	 		 		   		 		  
    # print(f"corr: {c[0,1]}")  		  	   		 	   		  		  		    	 		 		   		 		  
