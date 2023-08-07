# Monte Carlo Simulator Project
Author: Rachel Holman

## Synopsis
How to install, import, and use the code to create dice, play a game, and analyze a game.

### Installation:

Download the montecarlo folder and setpup.py file to your computer. Then, in terminal, navigate to the folder you saved these two items and them run the following line of code to install the module:

```pip install -e . ```


### Importing:

To import this newly installed project into your python coding system, run the following line of code: ```import montecarlo.montecarlo```

To learn more about the classes and methods included in this module, learn more by running the command: ```help(montecarlo)```

### Using it:

1. Create a die

```python
test_die1 = m.Die() #by default, creates a regular 6-sided dice
test_die2 = m.Die(np.array(['H','T'])) #creates a 2-sided coin
test_die1.change_side_weight(3, 5) #changes the weight of landing on side 3

test_die1.roll_die() #rolls die once
test_die2.roll_die(4) #rolls die 4 times

test_die1.current_state() #see all faces and weights for a die
```

2. Play a game

```python
test_die1 = m.Die() 
test_die2 = m.Die() #create 2 regular 6-sided dice
test_die2.change_side_weight(3, 5) #change the weight of one side of the second dice

test_game = m.Game([test_die1, test_die2]) #create a game with the 2 dice
test_game.play(5) #play the game (roll the dice) 5 times
test_game.show_results() #view the results after playing the game
```

3. Analyze a game

```python
test_analyzer = m.Analyzer(test_game) #pass in the game created in step 2
test_analyzer.jackpot() #see how many jackpots from the game
test_analyzer.face_counts() #see a count of how many faces were rolled each round
test_analyzer.combo_count() #see a count of unique face combinations rolled
test_analyzer.permutation_count() #see a count of unique face permutations rolled
```

## API Description

Help on module montecarlo.montecarlo in montecarlo:

NAME
    montecarlo.montecarlo

CLASSES
    builtins.object
        Analyzer
        Die
        Game
    
    class Analyzer(builtins.object)
     |  Analyzer(game)
     |  
     |  Analyzes the oucome of a given game in terns of jackpot rolls,
     |  value counts for each face, counts for each combination of faces
     |  rolled, and counts for each permutation of faces rolled.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, game)
     |      Initializes the game value so long as it is an instance of 
     |      the Game object
     |      
     |      Parameters: 
     |      game - Game object of game that has been played 
     |      
     |      Returns:
     |      N/A
     |  
     |  combo_count(self)
     |      Computes the distinct combinations of faces rolled along with their
     |      counts. Combinations are order-independent and may contain repetitions.
     |      Returns a dataframe with a MultiIndex of distinct combinations 
     |      and a column for associated counts
     |      
     |      Parameters: 
     |      N/A
     |      
     |      Returns:
     |      data frame with distinct combinations and counts
     |  
     |  face_counts(self)
     |      This method computes the number of times a given face is rolled
     |      in each roll event and returns a data frame with an index of
     |      roll number, face values as columns, and count values in the cells.
     |      
     |      Parameters: 
     |      N/A
     |      
     |      Returns:
     |      data frame with roll number, face values, and count values
     |  
     |  jackpot(self)
     |      A jackpot is a result in which all faces are the same for one roll.
     |      This method computes and returns the total number of jackpots 
     |      in the game.
     |      
     |      Parameters: 
     |      N/A
     |      
     |      Returns:
     |      total number of jackpots
     |  
     |  permutation_count(self)
     |      Computes the distinct permitation of faces rolled along with their
     |      counts. Permutations are order-dependent and may contain repetitions.
     |      Returns a dataframe with a MultiIndex of distinct permutations 
     |      and a column for associated counts
     |      
     |      Parameters: 
     |      N/A
     |      
     |      Returns:
     |      data frame with distinct permutations and counts
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class Die(builtins.object)
     |  Die(faces=array([1, 2, 3, 4, 5, 6]))
     |  
     |  Allows user to create a die, specify side-weights, randomly roll
     |  the die, and view the die.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, faces=array([1, 2, 3, 4, 5, 6]))
     |      Creates a die with faces in the NumPy array list of faces 
     |      given by the user. Defaults to a 6-sided standard die with 
     |      face values 1-6 each with equal weight 1.0. The faces must 
     |      be distinct strings or numbers or the same data type.
     |      
     |      Parameters: 
     |      faces - Numpy Array of strings or numbers
     |      
     |      Returns:
     |      N/A
     |  
     |  change_side_weight(self, side, weight)
     |      Allows user to change the weight value for a specific side
     |      of the dice. Takes a valid side from die and a weight value that
     |      is either an integer, float, or value that can be cast as an 
     |      integer.
     |      
     |      Parameters: 
     |      side - string or number value in the Die face array
     |      weight - numeric value
     |      
     |      Returns:
     |      N/A
     |  
     |  current_state(self)
     |      Returns a copy of the private die data frame
     |      
     |      Parameters: 
     |      N/A
     |      
     |      Returns:
     |      copy of data frame
     |  
     |  roll_die(self, rolls=1)
     |      Takes a random sample with replacement from the private die
     |      data frame and applies the weight values. Returns a list of
     |      outcomes. Only one roll by default.
     |      
     |      Parameters: 
     |      rolls - integer value
     |      
     |      Returns:
     |      list of random outcomes for each roll
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class Game(builtins.object)
     |  Game(dice)
     |  
     |  Takes a list of dice and allows user to roll them all and see
     |  the results.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, dice)
     |      Initialized a list of similar dice.
     |      We assume the dice in the list each have the same number of sides
     |      and associated faces, but each may have their own weights. 
     |      
     |      Parameters: 
     |      dice - list of Die objects
     |      
     |      Returns:
     |      N/A
     |  
     |  play(self, rolls=1)
     |      Rolls each dice a specified number of times (default 1) and saves
     |      the output in a private wide-form table with roll number as a 
     |      named index, columns for each die number (using its list index 
     |      as column name), and the face rolled in the instance in each cell
     |      
     |      Parameters: 
     |      rolls - integer value
     |      
     |      Returns:
     |      N/A
     |  
     |  show_results(self, form='wide')
     |      Returns a copy of the private play data frame to the user.
     |      User is allowed to specify whether they want to see the output
     |      in narrow or wide form (wide by default). 
     |      A ValueError is raised if the user enters an invalid viewing option.
     |      Narrow form will have a MultiIndex comprising of roll number and 
     |      die number (in this order) and a single column with faces roled.
     |      
     |      Parameters: 
     |      form - string value of either "wide" or "narrow"
     |      
     |      Returns:
     |      either a wide or narrow data frame
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)

