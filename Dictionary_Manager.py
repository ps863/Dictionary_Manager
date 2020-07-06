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
        
        #If indexing is wanted
        if (indexed == True):
            keys_in_dict = list(self.in_dict.keys())  #list of keys of input dictionary
            keys_in_dict = random.shuffle(keys_in_dict) #Shuffled list of keys 

            count = 0
            out_dict = {}
            for key in keys_in_dict:
                if (count == K):
                    break
                out_dict[count] = self.in_dict[key] #Add sampled entry into output dictionary. Key is index
                count += 1
            return out_dict
        
        raise ValueError("Invalid parameter for indexed. Indexed can either be true or false only")


        def value_sort_alphabetically (decending = False):
            """
            Sorts the dictionary such that all values are alphabetically arranged

            Parameters:
            decending : By default False. If True, follow an order from Z to A. If False, follow an order from A to Z

            Condition: 
            No key should have more than one value each 
            All values should be strings
            """

            # Implement the error handling 

            # A to Z
            if (decending == False):
                values = list (self.in_dict.values)
                values_sorted = sorted(values)

                new_dict = {}
            
                for value in values_sorted:
                    for key in self.in_dict:
                        if (self.in_dict[key] == value):
                            new_dict[key] = value
                            break
                            
                return new_dict
            
            if (decending == True):
                NotImplementedError()
            