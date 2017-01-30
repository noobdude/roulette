class Outcome(object):
    '''Contains a single outcome on which a bet can be placed'''
    
    def __init__(self, name, odds):
        self.name = name
        self.odds = odds # assume denominator is 1, i.e. odds:1
        
    def __eq__(self, other):
        '''Compares the name attributes of self and other.
        
        Return:
        True - if both names match
        '''
        
        return self.name == other.name
    
    def __hash__(self):
        pass
    
    def __ne__(self, other):
        '''Compare name attributes of self and other.
        
        Return:
        True - if this name does not match the other name
        '''
        
        return self.name != other.name
        
    def __str__(self):
        '''Easy-to-read representation of this outcome'''
        
        return '%s (%i:1)' %(self.name, self.odds)
        
    def win_amount(self, amount):
        '''Multiple this outcome's odds by the given amount and returns
        the product.
        
        Parameters:
        amount - amount being bet
        '''
        
        return self.odds*amount
    
if __name__ == '__main__':
    test1 = Outcome('bob', 3)
    test2 = Outcome('Joe', 2)
    test3 = Outcome('Joe', 2)
    
    print(test1.win_amount(10))
    print(test1 == test2)
    print(test2 == test3)
    print(test2 != test3)
    print(test2 is test3)
    