from outcome import Outcome

class Bin(object):
    '''Represents one of the 38 bins in the Roulette wheel
    
    Each bin can contain a collection of Outcome objects which reflect
    the winning bets that are paid for a particular bin on a Roulette
    wheel
    
    E.g. a spin of 1, select the "1" bin with the following winning
    Outcomes: "1", "Red", "Odd", "Low", etc...
    '''
    
    def __init__(self, *outcomes):
        '''
        Parameter
        outcomes - any number of Outcome objects used to populate the 
                   Bin initially
        '''
        
        self.outcomes = frozenset(outcomes)
    
    def __str__(self):
        '''List all Outcomes in this Bin'''
        
        return ', '.join(map(str, self.outcomes))
    
    def add(self, outcome):
        '''Adds an Outcome to the Bin'''
        
        self.outcomes |= set(outcome)
        
if __name__ == '__main__':
    five = Outcome('00-0-1-2-3', 6)
    zero = Bin(Outcome('0', 35), five)
    zerozero = Bin(Outcome('00', 35), five)
    
    print(zero)