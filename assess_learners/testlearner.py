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
import time



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
    # import pdb; pdb.set_trace()
    train_rows = int(0.6 * combined_data.shape[0])  		  	   		 	   		  		  		    	 		 		   		 		  
    test_rows = combined_data.shape[0] - train_rows  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
    # separate out training and testing data  		  	   		 	   		  		  		    	 		 		   		 		  
    train_x = combined_data[:train_rows, 0:-1]  		  	   		 	   		  		  		    	 		 		   		 		  
    train_y = combined_data[:train_rows, -1]  		  	   		 	   		  		  		    	 		 		   		 		  
    test_x = combined_data[train_rows:, 0:-1]  		  	   		 	   		  		  		    	 		 		   		 		  
    test_y = combined_data[train_rows:, -1]  		  	   		 	   		  		  		    	 		 		   		 		     	   		  		  		    	 		 		   		 		  

    # Experiment 1 

    max_leaf_size = 50
    experiment_1_learners = np.empty(max_leaf_size, dtype=object)

    # Model Training for models up to max leaf size
    for i in range(max_leaf_size):
        experiment_1_learners[i] = dt.DTLearner(leaf_size=(i+1))
        experiment_1_learners[i].add_evidence(train_x,train_y)
    
    training_rmse = np.zeros(max_leaf_size) 
    
    for i in range(max_leaf_size):
        y_pred_train = experiment_1_learners[i].query(train_x)
        training_rmse[i] = math.sqrt(((train_y - y_pred_train) ** 2).sum() / train_y.shape[0])  

    testing_rmse = np.zeros(max_leaf_size)
    for i in range(max_leaf_size):
        y_pred_test = experiment_1_learners[i].query(test_x)
        testing_rmse[i] = math.sqrt(((test_y - y_pred_test) ** 2).sum() / test_y.shape[0])

    plt.figure(figsize=(10,6))
    plt.plot(range(1,max_leaf_size + 1), training_rmse, label = 'Training RMSE', color = 'blue')
    plt.plot(range(1,max_leaf_size + 1), testing_rmse, label = 'Testing RMSE', color = 'green')
    plt.xlabel('Leaf Size', fontsize=14)
    plt.ylabel('RMSE', fontsize=14)
    plt.title('RMSE With Respect to Leaf Size', fontsize=16)
    plt.legend(loc=0, fontsize=12)
    plt.tight_layout()
    plt.savefig('images/rmse_with_respect_to_leaf_size.png')

    # Experiment 2 

    max_leaf_size = 50
    experiment_2_learners = np.empty(max_leaf_size, dtype=object)

    for i in range(max_leaf_size):
        experiment_2_learners[i] = bl.BagLearner(learner = dt.DTLearner, kwargs = {"leaf_size":i})
        experiment_2_learners[i].add_evidence(train_x, train_y)

    training_rmse = np.zeros(max_leaf_size) 
    
    for i in range(max_leaf_size):
        y_pred_train = experiment_2_learners[i].query(train_x)
        training_rmse[i] = math.sqrt(((train_y - y_pred_train) ** 2).sum() / train_y.shape[0])  

    testing_rmse = np.zeros(max_leaf_size)
    for i in range(max_leaf_size):
        y_pred_test = experiment_2_learners[i].query(test_x)
        testing_rmse[i] = math.sqrt(((test_y - y_pred_test) ** 2).sum() / test_y.shape[0])


    plt.figure(figsize=(10,6))
    plt.plot(range(1,max_leaf_size + 1), training_rmse, label = 'Training RMSE', color = 'blue')
    plt.plot(range(1,max_leaf_size + 1), testing_rmse, label = 'Testing RMSE', color = 'green')
    plt.xlabel('Leaf Size', fontsize=14)
    plt.ylabel('RMSE', fontsize=14)
    plt.title('RMSE With Respect to Leaf Size with Bagging', fontsize=16)
    plt.legend(loc=0, fontsize=12)
    plt.tight_layout()
    plt.savefig('images/rmse_with_respect_to_leaf_size_with_bagging.png')

    # Experiment 3
    random_dataset_indexes = np.zeros((10, combined_data.shape[0]), dtype=int)
    combined_random_dataset = np.zeros((10, combined_data.shape[0], combined_data.shape[1]))

    for i in range(10):
        random_dataset_indexes[i] = np.random.default_rng(i).choice(combined_data.shape[0],combined_data.shape[0])
        combined_random_dataset[i] = combined_data[random_dataset_indexes[i]]  

    dt_all_time_to_build = np.empty(10, dtype=object)
    rt_all_time_to_build = np.empty(10, dtype=object)
    dt_all_r_squared = np.empty(10, dtype=object)
    rt_all_r_squared = np.empty(10, dtype=object)
    # Model Training for models up to max leaf size
    for index, dataset in enumerate(combined_random_dataset):
        train_rows = int(0.6 * dataset.shape[0])  		  	   		 	   		  		  		    	 		 		   		 		  
        test_rows = dataset.shape[0] - train_rows  		  	   		 	   		  		  		    	 		 		   		 		  
                                                                                            
        # separate out training and testing data  		  	   		 	   		  		  		    	 		 		   		 		  
        train_x = dataset[:train_rows, 0:-1]  		  	   		 	   		  		  		    	 		 		   		 		  
        train_y = dataset[:train_rows, -1]  		  	   		 	   		  		  		    	 		 		   		 		  
        test_x = dataset[train_rows:, 0:-1]  		  	   		 	   		  		  		    	 		 		   		 		  
        test_y = dataset[train_rows:, -1]  		

        max_leaf_size = 25
        dt_learners = np.empty(max_leaf_size, dtype=object)
        rt_learners = np.empty(max_leaf_size, dtype=object)
        dt_learners_time_to_build = np.zeros(max_leaf_size)
        rt_learners_time_to_build = np.zeros(max_leaf_size)
        dt_test_r_squared = np.zeros(max_leaf_size) 
        rt_test_r_squared = np.zeros(max_leaf_size)

        for j in range(max_leaf_size):
            dt_learners[j] = dt.DTLearner(leaf_size=(j+1))
            start_time = time.time()
            dt_learners[j].add_evidence(train_x,train_y)
            end_time = time.time()
            dt_learners_time_to_build[j] = end_time - start_time
            
        
        for k in range(max_leaf_size):
            rt_learners[k] = rt.RTLearner(leaf_size=(k+1))
            start_time = time.time()
            rt_learners[k].add_evidence(train_x,train_y)
            end_time = time.time()
            rt_learners_time_to_build[k] = end_time - start_time

        dt_all_time_to_build[index] = dt_learners_time_to_build
        rt_all_time_to_build[index] = rt_learners_time_to_build
        

        for m in range(max_leaf_size):
            y_pred_test = dt_learners[m].query(test_x)
            ss_residual = ((test_y - y_pred_test) ** 2).sum()
            ss_total = ((test_y - test_y.mean()) ** 2).sum()
            dt_test_r_squared[m] = 1 - (ss_residual / ss_total)

        for n in range(max_leaf_size):
            y_pred_test = rt_learners[n].query(test_x)
            ss_residual = ((test_y - y_pred_test) ** 2).sum()
            ss_total = ((test_y - test_y.mean()) ** 2).sum()
            rt_test_r_squared[n] = 1 - (ss_residual / ss_total)

        dt_all_r_squared[index] = dt_test_r_squared
        rt_all_r_squared[index] = rt_test_r_squared

    dt_mean_build_time_all_sims = np.mean(dt_all_time_to_build) 
    rt_mean_build_time_all_sims = np.mean(rt_all_time_to_build) 
    dt_mean_r_squared_all_sims = np.mean(dt_all_r_squared) 
    rt_mean_r_squared_all_sims = np.mean(rt_all_r_squared) 
    
    plt.figure(figsize=(10,6))
    plt.plot(range(1,max_leaf_size + 1), dt_mean_build_time_all_sims, label = 'Decision Tree', color = 'blue')
    plt.plot(range(1,max_leaf_size + 1), rt_mean_build_time_all_sims, label = 'Random Tree', color = 'green')
    plt.xlabel('Leaf Size', fontsize=14)
    plt.ylabel('Build Time', fontsize=14)
    plt.title('Time To Build With Respect To Leaf Size', fontsize=16)
    plt.legend(loc=0, fontsize=12)
    plt.tight_layout()
    plt.savefig('images/time_to_build_with_respect_to_leaf_size.png')

    plt.figure(figsize=(10,6))
    plt.plot(range(1,max_leaf_size + 1), dt_mean_r_squared_all_sims, label = 'Decision Tree', color = 'blue')
    plt.plot(range(1,max_leaf_size + 1), rt_mean_r_squared_all_sims, label = 'Random Tree', color = 'green')
    plt.xlabel('Leaf Size', fontsize=14)
    plt.ylabel('R Squared', fontsize=14)
    plt.title('R Sqaured With Respect To Leaf Size', fontsize=16)
    plt.legend(loc=0, fontsize=12)
    plt.tight_layout()
    plt.savefig('images/r_squared_with_respect_to_leaf_size.png')