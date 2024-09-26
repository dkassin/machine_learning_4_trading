""""""  		  	   		 	   		  		  		    	 		 		   		 		  
"""  		  	   		 	   		  		  		    	 		 		   		 		  
A simple wrapper for linear regression.  (c) 2015 Tucker Balch  		  	   		 	   		  		  		    	 		 		   		 		  
Note, this is NOT a correct DTLearner; Replace with your own implementation.  		  	   		 	   		  		  		    	 		 		   		 		  
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
  		  	   		 	   		  		  		    	 		 		   		 		  
Student Name: Tucker Balch (replace with your name)  		  	   		 	   		  		  		    	 		 		   		 		  
GT User ID: tb34 (replace with your User ID)  		  	   		 	   		  		  		    	 		 		   		 		  
GT ID: 904063414 (replace with your GT ID)  		  	   		 	   		  		  		    	 		 		   		 		  
"""  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
import warnings  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
import numpy as np  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
class DTLearner(object):  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    This is a Decision Tree Learner (DTLearner)		  	   	

  	:leaf_size: Is the maximum number of samples to be aggregated at a leaf 
    :type leaf_size: int  		  	   		 	   		  		  		    	 		 		   		 		  
    :param verbose: If “verbose” is True, your code can print out information for debugging.  		  	   		 	   		  		  		    	 		 		   		 		  
        If verbose = False your code should not generate ANY output. When we test your code, verbose will be False.  		  	   		 	   		  		  		    	 		 		   		 		  
    :type verbose: bool  		  	   		 	   		  		  		    	 		 		   		 		  
    """  

    def __init__(self, leaf_size=1, verbose=False):  		  	   		 	   		  		  		    	 		 		   		 		  
        """  		  	   		 	   		  		  		    	 		 		   		 		  
        Constructor method  		  	   		 	   		  		  		    	 		 		   		 		  
        """  		
        self.tree = None  	 
        self.leaf_size = leaf_size
        pass  # move along, these aren't the drones you're looking for  

    def author(self):  		  	   		 	   		  		  		    	 		 		   		 		  
        """  		  	   		 	   		  		  		    	 		 		   		 		  
        :return: The GT username of the student  		  	   		 	   		  		  		    	 		 		   		 		  
        :rtype: str  		  	   		 	   		  		  		    	 		 		   		 		  
        """  		  	   		 	   		  		  		    	 		 		   		 		  
        return "dkassin3"

    def study_group(self):
        return "dkassin3"  	

    def compute_correlations(self, data_x, data_y):
        correlation_table = np.zeros(data_x.shape[1])
        for i in range(data_x.shape[1]):
            correlation_table[i] = np.corrcoef(data_x[:, i], data_y)[0, 1]
        
        return correlation_table
    
    def feature_selector(self, data_x, data_y):
        correlation_table = self.compute_correlations(data_x, data_y)
        max_correlation_index = np.argmax(np.abs(correlation_table))
        
        return max_correlation_index

    def build_tree(self, data):
        if data.shape[0] <= self.leaf_size:
            leaf_value = np.median(data[:, -1])
            return np.asarray([["leaf", leaf_value, np.nan, np.nan]])
        
        if np.all(data[:, -1] == data[0, -1]):
            leaf_value = np.median(data[:, -1])
            return np.asarray([["leaf", leaf_value, np.nan, np.nan]])

        data_x = data[:, :-1]
        data_y = data[:, -1]

        split_feature_index =  self.feature_selector(data_x, data_y)
        split_value = np.median(data_x[:, split_feature_index])
        

        left_data = data[data[:, split_feature_index] <= split_value]
        right_data = data[data[:, split_feature_index] > split_value]

        if left_data.shape[0] == 0 or right_data.shape[0] == 0:
            # import pdb; pdb.set_trace()
            leaf_value = np.median(data[:, -1]) 
            return np.asarray([["leaf", leaf_value, np.nan, np.nan]])

        left_tree = self.build_tree(left_data)
        right_tree = self.build_tree(right_data)

        root = np.array([f"x{split_feature_index}", split_value, 1, left_tree.shape[0] + 1])
        
        return_value = np.vstack((root, left_tree, right_tree))
        
        return return_value

    def add_evidence(self, data_x, data_y):  		  	   		 	   		  		  		    	 		 		   		 		  
        """  		  	   		 	   		  		  		    	 		 		   		 		  
        Add training data to learner  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
        :param data_x: A set of feature values used to train the learner  		  	   		 	   		  		  		    	 		 		   		 		  
        :type data_x: numpy.ndarray  		  	   		 	   		  		  		    	 		 		   		 		  
        :param data_y: The value we are attempting to predict given the X data  		  	   		 	   		  		  		    	 		 		   		 		  
        :type data_y: numpy.ndarray  		  	   		 	   		  		  		    	 		 		   		 		  
        """ 
        reshape_data_y = data_y.reshape(-1, 1)
        combined_data = np.hstack((data_x, reshape_data_y)) 	

        self.tree = self.build_tree(combined_data)

    def query(self, points):  		  	

        """  		  	   		 	   		  		  		    	 		 		   		 		  
        Estimate a set of test points given the model we built.  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
        :param points: A numpy array with each row corresponding to a specific query.  		  	   		 	   		  		  		    	 		 		   		 		  
        :type points: numpy.ndarray  		  	   		 	   		  		  		    	 		 		   		 		  
        :return: The predicted result of the input data according to the trained model  		  	   		 	   		  		  		    	 		 		   		 		  
        :rtype: numpy.ndarray  		  	   		 	   		  		  		    	 		 		   		 		  
        """  		  	   
        predictions = np.zeros(points.shape[0])
        for i, point in enumerate(points):
            node_index = 0

            while True:
                node = self.tree[node_index]

                if node[0] == 'leaf':
                    predictions[i] = float(node[1])
                    break

                feature_index = int(node[0][1:])
                if point[feature_index] <= float(node[1]):
                    node_index += int(node[2])
                else: 
                    node_index += int(node[3])
    
        # import pdb; pdb.set_trace()
        return predictions    

if __name__ == "__main__":  		  	   		 	   		  		  		    	 		 		   		 		  
    print("the secret clue is 'zzyzx'")  		  	   		 	   		  		  		    	 		 		   		 		  
