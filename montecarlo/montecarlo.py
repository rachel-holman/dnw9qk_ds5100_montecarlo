import pandas as pd
import numpy as np

class Die:
    """
    Docstring
    """
    
    def __init__(self, faces, w=1.0):
        """
        Docstring
        """
        #throw TypeError if faces is not a NumPy array
        #faces dtype may be strings or numbers
        #throw ValueError if face values are not distinct
        self.faces = faces
        self.w = w
        
    def change_side_weight(self, face, new_w):
        """
        Docstring
        """
        #check if face is valid value (raise IndexError if not)
        #check if weight is valid type (int/float) or can be cast as numeric. if not, raise TypeError
        
    def roll_die(self, rolls=1):
        """
        Docstring
        """
        #take random sample without replacement from privare die data frame and apply weights
        #return list of outcomes
        #do not store results internally
        
    def current_state(self):
        """
        Docstring
        """
        #return copy of private die data frame


    
class Game:
    """
    Docstring
    """
    
    def __init__(self, dice):
        """
        Docstring
        """
        #ideally, check if list ocntains die objects with same faces (not required)
        self.dice = dice
        
    def play(self, rolls):
        """
        Docstring
        """
        #save result to private data frame
        #data frame should be in wide format: roll number as a named index, columns for each die number (using its list index as column name), and the face rolled in the instance in each cell
        
    def show_results(self, form="wide"):
        """
        Docstring
        """
        # return a copy of private play data frame to user
        #allows user to get output in narrow or wide form
        #Narrow form will have MultiIndex comprising of roll num and die num (in this order) and a single column with faces roled
        #raide a ValueError if the user passes invalid option for narrow or wide
        
    
    
class Analyzer:
    """
    Docstring
    """
    
    def __init__(self, game):
        """
        Docstring
        """
        #throw ValueError if passed value is not a Game object
        self.game = game
        
    def jackpot(self):
        """
        Docstring
        """
        #jackpot is result which all faces are the same
        #compute how many times the game resulted in a jackpot
        #return a data frame of results
        #data frame should have roll number as a named index and a column for the jackpot count per roll
        
    def face_counts(self):
        """
        Docstring
        """
        # Computes how many times a given face is rolled in each event. For example, if a roll of five dice has all sixes, then the counts for this roll would be for the face value ‘6’ and for the other faces.
        #return data frame of results
        # Data frame has an index of roll number, fave values as columns, and count values in the cells 
        
    def combo_count(self):
        """
        Docstring
        """
        #computes distinct combos of faces rolled, along with their counts
        # combos are order-independent and may contain repitations
        #return data frame of results
        #dataframe should have MultiIndex of distinct combos and a column for the associated counts
        
    def permutation_count(self):
        """
        Docstring
        """
        #computes distinct permutations of faces rolled, along with their counts
        # permutations are order-dependent and may contain repitations
        #return data frame of results
        #dataframe should have MultiIndex of distinct permutations and a column for the associated counts
        
    
        