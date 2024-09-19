import numpy as np  
import random		  	   		 	   		  		  		    	 		 		   		 		  




  		  	   		 	   		  		  		    	 		 		   		 		  
class RTLearner(object):  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    This is a Random Tree Learner (RTLearner)		  	   	

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
        random.seed(self.gtid())
        self.tree = None  	 
        self.leaf_size = leaf_size
        self.verbose = verbose
        pass  # move along, these aren't the drones you're looking for  

    def gtid(self):  		  	   		 	   		  		  		    	 		 		   		 		  
        """  		  	   		 	   		  		  		    	 		 		   		 		  
        :return: The GT ID of the student  		  	   		 	   		  		  		    	 		 		   		 		  
        :rtype: int  		  	   		 	   		  		  		    	 		 		   		 		  
        """  		  	   		 	   		  		  		    	 		 		   		 		  
        return 904063414  	

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
    
    def random_feature_selector(self, data_x, data_y):
        random_index = random.randint(0, data_x.shape[1] - 1)
        return random_index

    def build_tree(self, data):
        if data.shape[0] <= self.leaf_size:
            return np.asarray([["leaf", data[0,-1], np.nan, np.nan]])
        
        if np.all(data[:, -1] == data[0, -1]):
            leaf_value = np.median(data[:, -1])
            return np.asarray([["leaf", leaf_value, np.nan, np.nan]])

        data_x = data[:, :-1]
        data_y = data[:, -1]

        split_feature_index =  self.random_feature_selector(data_x, data_y)
        split_value = np.median(data_x[:, split_feature_index])
        # import pdb; pdb.set_trace()

        left_data = data[data[:, split_feature_index] <= split_value]
        right_data = data[data[:, split_feature_index] > split_value]

        if left_data.shape[0] == 0 or right_data.shape[0] == 0:
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
        import pdb; pdb.set_trace()

    def query(self, points):  		  	   		 	   		  		  		    	 		 		   		 		  
        """  		  	   		 	   		  		  		    	 		 		   		 		  
        Estimate a set of test points given the model we built.  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
        :param points: A numpy array with each row corresponding to a specific query.  		  	   		 	   		  		  		    	 		 		   		 		  
        :type points: numpy.ndarray  		  	   		 	   		  		  		    	 		 		   		 		  
        :return: The predicted result of the input data according to the trained model  		  	   		 	   		  		  		    	 		 		   		 		  
        :rtype: numpy.ndarray  		  	   		 	   		  		  		    	 		 		   		 		  
        """  		  	   		 	   		  		  		    	 		 		   		 		  
        return (self.model_coefs[:-1] * points).sum(axis=1) + self.model_coefs[  		  	   		 	   		  		  		    	 		 		   		 		  
            -1  		  	   		 	   		  		  		    	 		 		   		 		  
        ]  		 
    

if __name__ == "__main__":  		  	   		 	   		  		  		    	 		 		   		 		  
    print("the secret clue is 'zzyzx'")  