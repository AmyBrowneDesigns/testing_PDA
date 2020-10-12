import unittest

from src.card import Card
from src.card_game import CardGame

class CardGameTest(unittest.TestCase):
    
    def setUp(self):
        self.card = Card ("diamonds", 10)
        self.card_game = CardGame()
       

    # def test_add_card(self):
    #     self.card_1 = Card ('hearts', 8)
    #     self.card_2 = Card ('spades', 4)
    #     self.card_3 = Card ('clubs', 6)
    #     self.card_game.add_card(card_1)
    #     self.card_game.add_card(card_2)
    #     self.card_game.add_card(card_3)
    #     self.assertEqual(3, len(self.card_game.card))
        

    def test_check_for_ace_result_is_true(self):
        card1 = Card('hearts', 8)
        self.assertEqual(False, self.card_game.check_for_ace(card1))
    
    def test_check_for_ace_result_is_false(self):
        card2 = Card('clubs', 1)
        self.assertEqual(True,self.card_game.check_for_ace(card2))


    def test_highest_card(self):
        card1 = Card('hearts', 8)
        card2 = Card('spades', 4)
        self.assertEqual(card1,CardGame.highest_card(self,card1,card2))
#

    def test_cards_total(self):
        card1 = Card('hearts', 8)
        card2 = Card('spades', 4)
        card3 = Card('clubs', 6)
        cards = [card1, card2, card3]
        self.assertEqual("You have a total of 18",self.card_game.cards_total(cards))

