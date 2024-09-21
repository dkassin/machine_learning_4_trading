import numpy as np, LinRegLearner as lrl, BagLearner as bl	 
class InsaneLearner(object):  		  	   		 	   		  		  		    	 		 		   		 		  	  		  		    	 		 		   		 		  
    def __init__(self, verbose=False):  		  	   		 	   		  		  		    	 		 		   		 		  
        self.learners = np.array([bl.BagLearner(learner= lrl.LinRegLearner, kwargs = {}) for _ in range(20)])
    def author(self):  		  	   		 	   		  		  		    	 		 		   		 		  	  	   		 	   		  		  		    	 		 		   		 		  
        return "dkassin3"
    def add_evidence(self, data_x, data_y):  		  	   		 	   		  		  		    	 		 		   		 		  
        reshape_data_y = data_y.reshape(-1, 1)
        combined_data = np.hstack((data_x, reshape_data_y)) 
        for index, learner in enumerate(self.learners):
            random_sample = np.random.RandomState(index).choice(combined_data.shape[0],combined_data.shape[0], replace=True)     
            train_x = combined_data[random_sample, :-1]  		  	   		 	   		  		  		    	 		 		   		 		  
            train_y = combined_data[random_sample, -1]
            learner.add_evidence(train_x, train_y)                	  	   		 	   		  		  		    	 		 		   			 	   		  		  		    	 		 		   		 		  
    def query(self, points):  		  	   		 	   		  		  		    	 		 		   		 		  
        predictions = np.zeros((points.shape[0], 20)) 		
        for index, learner in enumerate(self.all_learners):
            predictions[:, index] = learner.query(points)   		 	   		  		  		    	 		 		   		 		  
        return np.mean(predictions, axis=1)
	