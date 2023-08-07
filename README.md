# Monte Carlo Simulator Project
Author: Rachel Holman

## Synopsis
How to install, import, and use the code to create dice, play a game, and analyze a game.

### Installation:

In your terminal or directly in python, run the following line of code to install the module:

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
List of all classes with their public methods and attributes.


