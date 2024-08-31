""""""  		  	   		 	   		  		  		    	 		 		   		 		  
"""Assess a betting strategy.  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
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
  		  	   		 	   		  		  		    	 		 		   		 		  
Student Name: David Kassin  		  	   		 	   		  		  		    	 		 		   		 		  
GT User ID: dkassin3  		  	   		 	   		  		  		    	 		 		   		 		  
GT ID: 904063414	  	   		 	   		  		  		    	 		 		   		 		  
"""  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
import numpy as np  		  	   		 	   		  		  		    	 		 		   		 		  
		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
def author():  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    :return: The GT username of the student  		  	   		 	   		  		  		    	 		 		   		 		  
    :rtype: str  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    return "dkassin3"  	

def study_group():
    return "dkassin3"	  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
def gtid():  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    :return: The GT ID of the student  		  	   		 	   		  		  		    	 		 		   		 		  
    :rtype: int  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    return 904063414  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
def get_spin_result(win_prob):  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
    :param win_prob: The probability of winning  		  	   		 	   		  		  		    	 		 		   		 		  
    :type win_prob: float  		  	   		 	   		  		  		    	 		 		   		 		  
    :return: The result of the spin.  		  	   		 	   		  		  		    	 		 		   		 		  
    :rtype: bool  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    result = False  		  	   		 	   		  		  		    	 		 		   		 		  
    if np.random.random() <= win_prob:  		  	   		 	   		  		  		    	 		 		   		 		  
        result = True  		  	   		 	   		  		  		    	 		 		   		 		  
    return result  		



def bach_betting_strategy(win_prob):
    episode_winnings = 0
    winnings = [0]
    bet_amount = 1

    for _ in range(20):
        if episode_winnings >= 80:
            winnings.append(episode_winnings)
        else:
            won = get_spin_result(win_prob)
            if won:
                episode_winnings = episode_winnings + bet_amount
                winnings.append(episode_winnings)
                bet_amount = 1
            else:
                episode_winnings = episode_winnings - bet_amount
                winnings.append(episode_winnings)
                bet_amount =  bet_amount * 2


    return np.array(winnings)

def realistic_betting_strategy(win_prob):
    episode_winnings = 0
    winnings = [0]
    bet_amount = 1
    bank_roll = 50

    for _ in range(20):
        if episode_winnings >= 80 or episode_winnings <= (-50):
            winnings.append(episode_winnings)
        else:
            won = get_spin_result(win_prob)
            if won:
                episode_winnings += bet_amount
                bank_roll += bet_amount
                winnings.append(episode_winnings)
                bet_amount = 1
            else:
                episode_winnings -= bet_amount
                bank_roll -= bet_amount
                winnings.append(episode_winnings)
                if (bank_roll - (bet_amount*2)) > 0:
                    bet_amount =  bet_amount * 2
                else:
                    bet_amount = bank_roll

    return np.array(winnings)

def simple_simulator(number_of_episodes, win_prob):
    episodes = []
    for _ in range(number_of_episodes):
        winnings = bach_betting_strategy(win_prob)
        episodes.append(winnings)

    spin_array = np.stack(episodes, axis = 0)
    mean_values = np.mean(spin_array, axis = 0)
    median_values = np.median(spin_array, axis = 0)
    std_values = np.std(spin_array, axis = 0)

    mean_values = np.round(mean_values, 4)
    median_values = np.round(median_values, 4)
    std_values = np.round(std_values, 4)

    stats_stack = np.stack([mean_values, median_values, std_values], axis = 0)
    final_array = np.concatenate([spin_array, stats_stack], axis = 0)
    print(final_array)

def realistic_simulator(number_of_episodes, win_prob):
    episodes = []
    for _ in range(number_of_episodes):
        winnings = realistic_betting_strategy(win_prob)
        episodes.append(winnings)

    spin_array = np.stack(episodes, axis = 0)
    mean_values = np.mean(spin_array, axis = 0)
    median_values = np.median(spin_array, axis = 0)
    std_values = np.std(spin_array, axis = 0)

    mean_values = np.round(mean_values, 4)
    median_values = np.round(median_values, 4)
    std_values = np.round(std_values, 4)

    stats_stack = np.stack([mean_values, median_values, std_values], axis = 0)
    final_array = np.concatenate([spin_array, stats_stack], axis = 0)
    print(final_array)

def test_code():  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    Method to test your code  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	  
    np.set_printoptions(linewidth=np.inf) 	
    win_prob = 0.4736  # set appropriately to the probability of a win  		  	   		 	   		  		  		    	 		 		   		 		  
    np.random.seed(gtid())  # do this only once  		  	   		 	   		  		  		    	 		 		   		 		  
    # print(get_spin_result(win_prob))  # test the roulette spin
    # figure_1 = simple_simulator(10, win_prob)
    # figure_2 = simple_simulator(1000, win_prob)
    print(realistic_betting_strategy(win_prob))
    # print(figure_1)
    # add your code here to implement the experiments  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
if __name__ == "__main__":		    	 		 		   		 		  
    test_code()  		  	   		 	   		  		  		    	 		 		   		 		  


# Notes, both strategies are implemented, just need to add the matplotlib charts and then write reports.