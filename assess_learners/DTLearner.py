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
    
    def factor_selector(self, data_x, data_y):
        correlation_table = self.compute_correlations(data_x, data_y)
        max_correlation_index = np.argmax(np.abs(correlation_table))

    def build_tree(self, data_x, data_y):
        reshape_data_y = data_y.reshape(-1, 1)
        combined_data = np.hstack((data_x, reshape_data_y))

        if combined_data.shape[0] == 1:
            return np.asarray([["leaf", combined_data[0,-1], "NA", "NA"]])
        
        if np.all(combined_data[: -1] == combined_data[0, -1]):
            return np.asarray([["leaf", combined_data[0,-1], "NA", "NA"]])
    
        

    def add_evidence(self, data_x, data_y):  		  	   		 	   		  		  		    	 		 		   		 		  
        """  		  	   		 	   		  		  		    	 		 		   		 		  
        Add training data to learner  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
        :param data_x: A set of feature values used to train the learner  		  	   		 	   		  		  		    	 		 		   		 		  
        :type data_x: numpy.ndarray  		  	   		 	   		  		  		    	 		 		   		 		  
        :param data_y: The value we are attempting to predict given the X data  		  	   		 	   		  		  		    	 		 		   		 		  
        :type data_y: numpy.ndarray  		  	   		 	   		  		  		    	 		 		   		 		  
        """  	

        self.tree = self.build_tree(data_x, data_y)


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


    