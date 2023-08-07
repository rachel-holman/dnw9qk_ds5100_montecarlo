import unittest
import pandas as pd
import random
from pandas.testing import assert_frame_equal
from montecarlo import Die
from montecarlo import Game
from montecarlo import Analyzer

class DieTestSuite(unittest.TestCase):
    
    def test_init(self):
        test_die = Die()
        
        f=[1,2,3,4,5,6]
        w=[1.0,1.0,1.0,1.0,1.0,1.0]
        df = pd.DataFrame(dict(face = f, weight = w)).set_index('face')
        
        self.assertTrue(df.equals(test_die.current_state()))
        self.assertTrue(isinstance(test_die, Die))
    
    def test_change_side_weight(self):
        test_die = Die()
        test_die.change_side_weight(3, 5)
        
        f=[1,2,3,4,5,6]
        w=[1.0,1.0,5.0,1.0,1.0,1.0]
        df = pd.DataFrame(dict(face = f, weight = w)).set_index('face')
        
        self.assertEqual(df.equals(test_die.current_state()), True)
    
    
    def test_roll_die(self):
        random.seed(12345)
        test_die = Die()
        
        self.assertEqual(test_die.roll_die(5), [3, 1, 5, 2, 3])
        
        
    def test_current_state(self):
        test_die = Die()
        test_die.change_side_weight(1, 5)
        
        f=[1,2,3,4,5,6]
        w=[5.0,1.0,1.0,1.0,1.0,1.0]
        df = pd.DataFrame(dict(face = f, weight = w)).set_index('face')
        
        self.assertEqual(df.equals(test_die.current_state()), True)
        
    
class GameTestSuite(unittest.TestCase):
    
    def test_init(self):
        test_die1 = Die()
        test_die2 = Die()
        test_die2.change_side_weight(3, 5)
        
        test_game = Game([test_die1, test_die2])
        
        self.assertTrue(all(isinstance(d, Die) for d in test_game.dice))
        self.assertTrue(isinstance(test_game, Game))
        
    def test_play(self):
        random.seed(12345)
        test_die1 = Die()
        test_die2 = Die()
        test_die2.change_side_weight(3, 5)
        
        test_game = Game([test_die1, test_die2])
        test_game.play(5)
        
        r = [1,2,3,4,5]
        d1= [3,1,5,2,3]
        d2= [2,3,2,2,3]
        df = pd.DataFrame(dict(roll=r, d1=d1, d2=d2))\
             .set_index('roll').rename({'d1':1, "d2":2}, axis=1)

        self.assertEqual(df.equals(test_game.show_results()), True)
        
    
    def test_show_results(self):
        random.seed(12345)
        test_die1 = Die()
        test_die2 = Die()
        test_die2.change_side_weight(3, 5)
        
        test_game = Game([test_die1, test_die2])
        test_game.play(5)
        
        r = [1,2,3,4,5]
        d1= [3,1,5,2,3]
        d2= [2,3,2,2,3]
        df = pd.DataFrame(dict(roll=r, d1=d1, d2=d2))\
             .set_index('roll').rename({'d1':1, "d2":2}, axis=1)

        self.assertEqual(df.equals(test_game.show_results()), True)
    
    
class AnalyzerTestSuite(unittest.TestCase):
    
    def test_init(self):
        test_die1 = Die()
        test_die2 = Die()
        test_die2.change_side_weight(3, 5)
        
        test_game = Game([test_die1, test_die2])
        test_game.play(5)
        
        test_analyzer = Analyzer(test_game)
        
        self.assertTrue(isinstance(test_game, Game))
        self.assertTrue(isinstance(test_analyzer, Analyzer))
        
    def test_jackpot(self):
        random.seed(12345)
        test_die1 = Die()
        test_die2 = Die()
        test_die2.change_side_weight(3, 5)
        
        test_game = Game([test_die1, test_die2])
        test_game.play(5)
        
        test_analyzer = Analyzer(test_game)
        test_analyzer.jackpot()
        
        self.assertEqual(test_analyzer.jackpot(), 2)
        
    
    def test_face_counts(self):
        random.seed(12345)
        test_die1 = Die()
        test_die2 = Die()
        test_die2.change_side_weight(3, 5)
        
        test_game = Game([test_die1, test_die2])
        test_game.play(5)
        
        test_analyzer = Analyzer(test_game)
        
        r = [1,2,3,4,5]
        f1= [0.0,1.0,0.0,0.0,0.0]
        f2= [1.0,0.0,1.0,2.0,0.0]
        f3= [1.0,1.0,0.0,0.0,2.0]
        f4= [0.0,0.0,0.0,0.0,0.0]
        f5= [0.0,0.0,1.0,0.0,0.0]
        f6= [0.0,0.0,0.0,0.0,0.0]
        df = pd.DataFrame(dict(roll=r, f1=f1, f2=f2,
                              f3=f3,f4=f4,f5=f5,f6=f6))\
             .set_index('roll').rename({'f1':1, "f2":2,
                                        'f3':3, 'f4':4,
                                        'f5':5, 'f6':6}, axis=1)
        
        self.assertEqual(df.equals(test_analyzer.face_counts()), True)
    
    def test_combo_count(self):
        random.seed(12345)
        test_die1 = Die()
        test_die2 = Die()
        test_die2.change_side_weight(3, 5)
        
        test_game = Game([test_die1, test_die2])
        test_game.play(10)
        
        test_analyzer = Analyzer(test_game)
        
        d1 = [1,1,2,3,3,3,4]
        d2= [2,3,3,3,5,6,6]
        c= [2,2,2,1,1,1,1]
        df = pd.DataFrame(dict(d1=d1, d2=d2, count=c))\
             .rename({'d1':1, "d2":2}, axis=1).set_index([1,2])

        self.assertEqual(df.equals(test_analyzer.combo_count()), True)

    
    def test_permutation_count(self):
        random.seed(12345)
        test_die1 = Die()
        test_die2 = Die()
        test_die2.change_side_weight(3, 5)
        
        test_game = Game([test_die1, test_die2])
        test_game.play(10)
        
        test_analyzer = Analyzer(test_game)
        
        d1 = [1,1,2,2,3,3,3,4,5]
        d2= [2,3,1,3,2,3,6,6,3]
        c= [1,2,1,1,1,1,1,1,1]
        df = pd.DataFrame(dict(d1=d1, d2=d2, count=c))\
             .rename({'d1':1, "d2":2}, axis=1).set_index([1,2])
        
        self.assertEqual(df.equals(test_analyzer.permutation_count()), True)
    
    
    
if __name__ == '__main__':
    
    unittest.main(verbosity=3)
    
