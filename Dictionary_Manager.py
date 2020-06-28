"""
Base class which will provide functionality 

"""
import random

class Dictionary_Manager:
    
    
    def __init__(self , in_dict = {}):
        """Initialization of manager. Optional parameter:dictonary that needs to be managed"""
        self.in_dict = in_dict

    def set_input_dictionary (self,in_dict):
        """Set the dictionary that needs to be managed""" 
        self.in_dict = in_dict
    
    def sample_random_dictionary (self,K,indexed = False):
        """
        Randomly sample K items from a dictionary

        Parameters:
        K : Number of items to be sampled out randomly from entire dictionary 
        indexed : If the keys of the sampled dictionary should be numbers (See docs for more details)
        """
        if (K > len(self.in_dict)):
            raise ValueError("Desired sample size is larger than the size of input dictionary into the manager")
        
        #If indexing is not wanted 
        if (indexed == False):
            keys_in_dict = list(self.in_dict.keys())  #list of keys of input dictionary
            keys_in_dict = random.shuffle(keys_in_dict) #Shuffled list of keys 

            count = 0
            out_dict = {}
            for key in keys_in_dict:
                if (count == K):
                    break
                out_dict[key] = self.in_dict[key] #Add sampled entry into output dictionary 
                count += 1
            return out_dict
        
        if (indexed == True):
            raise NotImplementedError ("Feature yet to be implemented")
        