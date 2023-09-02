"""
Class for a car
"""

class Car:
    """
    Create car object
    """
    
    def __init__(self,make, model):
        """
        _summary_

        :param make: manufacturer
        :type make: str
        :param model: eg "A3"
        :type model:str
        """
        self.make = make
        self.model = model
        
    def get_car(self):
        """
        Getter for car

        :return: make and model
        :rtype: str tuple
        """
        return self.make, self.model    
    