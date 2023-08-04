import pandas as pd
import numpy as np
import random

class Die:
    """
    Allows user to create a die, specify side-weights, randomly roll
    the die, and view the die.
    """
    
    def __init__(self, faces=np.arange(1,7)):
        """
        Creates a die with faces in the NumPy array list of faces 
        given by the user. Defaults to a 6-sided standard die with 
        face values 1-6 each with equal weight 1.0. The faces must 
        be distinct strings or numbers or the same data type.
        """
        if len(set(faces)) != len(faces):
            raise ValueError("Face values must be distinct")
        
        if not isinstance(faces, np.ndarray):
            raise TypeError("Input must be a NumPy array")
            
        self._die = pd.DataFrame(dict(face = faces,
                                     weight = np.ones(len(faces), 
                                                      dtype=float)))
        self._die = self._die.set_index('face')
        self.faces = faces
        
        
    def change_side_weight(self, side, weight):
        """
        Allows user to change the weight value for a specific side
        of the dice. Takes a valid side from die and a weight value that
        is either an integer, float, or value that can be cast as an 
        integer.
        """
        if side not in self.faces:
            raise IndexError("Face value must be in the die array")
            
        if not (type(weight) == int or type(weight) == float):
            if not weight.isnumeric():
                raise TypeError("Weight value must be numeric")
        
        weight = int(weight)
        self._die.loc[side, 'weight'] = weight
        
    def roll_die(self, rolls=1):
        """
        Takes a random sample with replacement from the private die
        data frame and applies the weight values. Returns a list of
        outcomes. Only one roll by default.
        """
        rolled = random.choices(self._die.index, 
                                weights=self._die.weight, 
                                k=rolls)
        return rolled
        
    def current_state(self):
        """
        Returns a copy of the private die data frame
        """
        return self._die.copy()

    
class Game:
    """
    Takes a list of dice and allows user to roll them all and see
    the results.
    """
    
    def __init__(self, dice):
        """
        Initialized a list of similar dice.
        We assume the dice in the list each have the same number of sides
        and associated faces, but each may have their own weights. 
        """
        self.dice = dice
        
        
    def play(self, rolls=1):
        """
        Rolls each dice a specified number of times (default 1) and saves
        the output in a private wide-form table with roll number as a 
        named index, columns for each die number (using its list index 
        as column name), and the face rolled in the instance in each cell
        """
        self._game = pd.DataFrame({'roll': np.arange(1,rolls+1)})
        self._game = self._game.set_index('roll')
        
        col = 1
        for d in self.dice:
            self._game[col] = random.choices(d.current_state().index, 
                                           weights=d.current_state().weight, 
                                           k=rolls)
            col += 1
        
        
    def show_results(self, form="wide"):
        """
        Returns a copy of the private play data frame to the user.
        User is allowed to specify whether they want to see the output
        in narrow or wide form (wide by default). 
        A ValueError is raised if the user enters an invalid viewing option.
        Narrow form will have a MultiIndex comprising of roll number and 
        die number (in this order) and a single column with faces roled.
        """
        if not (form.lower() == 'wide' or form.lower() == 'narrow'):
            raise ValueError("Invalid option for narrow or wide output")
        
        cols = list(1+np.arange(len(self._game.reset_index().columns)-1))
        narrow = pd.melt(self._game.reset_index(), 
                         id_vars=['roll'], 
                         value_vars=cols).rename({'variable':'die',
                                                  'value':'outcome'}, 
                                                 axis=1)
        narrow = narrow.set_index(['roll','die']).sort_index()
        
        if form.lower() == 'wide':
            return self._game.copy()
        else:
            return narrow
            
            
    
class Analyzer:
    """
    Analyzes the oucome of a given game in terns of jackpot rolls,
    value counts for each face, counts for each combination of faces
    rolled, and counts for each permutation of faces rolled.
    """
    
    def __init__(self, game):
        """
        Initializes the game value so long as it is an instance of 
        the Game object
        """
        if not isinstance(game, Game):
            raise ValueError("Input must be a Game object")
            
        self.game = game
        
        
    def jackpot(self):
        """
        A jackpot is a result in which all faces are the same for one roll.
        This method computes and returns the total number of jackpots 
        in the game.
        """
        jack = np.transpose(self.game.show_results())
        
        jackpots = 0
        for c in jack.columns:
            if len(np.unique(jack[[c]])) == 1:
                jackpots = jackpots + 1

        return jackpots
        
    def face_counts(self):
        """
        This method computes the number of times a given face is rolled
        in each roll event and returns a data frame with an index of
        roll number, face values as columns, and count values in the cells.
        """
        base = pd.DataFrame({'roll': self.game.show_results().index})
        base = base.set_index('roll')
        
        for d in self.game.dice:
            for i in d.current_state().index :
                base[i] = np.zeros(len(base),dtype=float)
        
        nums = pd.DataFrame(self.game.show_results('narrow')\
                            .groupby(['roll','outcome']).size())\
                            .rename({0:'count'},axis=1).reset_index()
        nums = pd.pivot_table(nums, 
                               values='count',
                               index='roll',
                               columns='outcome')
        counts = base + nums
        return counts.fillna(0)
        
        
    def combo_count(self):
        """
        Computes the distinct combinations of faces rolled along with their
        counts. Combinations are order-independent and may contain repetitions.
        Returns a dataframe with a MultiIndex of distinct combinations 
        and a column for associated counts
        """
        df = self.game.show_results('wide')
        
        combo = pd.DataFrame(np.sort(df.values, axis=1), columns=df.columns)\
            .value_counts(sort=False).to_frame().rename({0:'count'}, axis=1)
       
        return combo
    
    def permutation_count(self):
        """
        Computes the distinct permitation of faces rolled along with their
        counts. Permutations are order-dependent and may contain repetitions.
        Returns a dataframe with a MultiIndex of distinct permutations 
        and a column for associated counts
        """
        perm = self.game.show_results('wide').value_counts(sort=False)\
                .to_frame().rename({0:'count'},axis=1)
        return perm
        
        
        
    
        