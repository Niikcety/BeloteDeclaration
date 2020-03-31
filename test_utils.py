import unittest
from utils import (
    declarations_in, 
    numbify, 
    belotes_in,
    carres_in, 
    tqq_in, 
    set_lad, 
    validate_all
    )

class TestFunctionsInUtils(unittest.TestCase):

    def test_numbify(self):
        hand = ['7C', 'JD', 'AS', 'QD', '8C', '9S', '10D', 'JS']

        result = numbify(hand)
        expected = [0, 1, 12, 13, 14, 29, 31, 34]

        self.assertEqual(result, expected)

    def test_hand_with_two_belotes(self):
        hand = ['KC', 'JD', 'AS', 'QD', 'QC', '9S', 'KD', 'JS']
        cards = numbify(hand)

        expected = [(5, 6), (14, 15)]
        result = belotes_in(cards)

        self.assertEqual(result, expected)

    def test_hand_with_zero_belotes(self):
        hand = ['7C', 'JD', 'AS', 'QD', '8C', '9S', '10D', 'JS']
        cards = numbify(hand)

        result = belotes_in(cards)
        expected = [(0,)]

        self.assertEqual(result, expected)

    def test_hand_with_carre_of_9s(self):
        hand = ['7C', '9D', '8H', '9S', '9C', '10D', '9H', 'JS']
        cards = numbify(hand)

        result = carres_in(cards)
        expected = [(2, 11, 20, 29)]

        self.assertEqual(result, expected)

    def test_hand_with_two_carres(self):
        hand = ['AC', 'AD', 'AH', 'AS', '9C', '9S', '9D', '9H']
        cards = numbify(hand)

        result = carres_in(cards)
        expected = [(2, 11, 20, 29), (7, 16, 25, 34)]

        self.assertEqual(result, expected)

    def test_hand_with_carre_of_7s(self):
        hand = ['7C', '7D', 'AS', 'QD', '9C', '7S', '10D', '7H']
        cards = numbify(hand)

        result = carres_in(cards)
        expected = [(0,)]

        self.assertEqual(result, expected)

    def test_hand_wit_two_tierces(self):
        hand = ['KH', '8C', 'AH', '7C', '9C', '9D', '10D', 'JD']
        cards = numbify(hand)

        result = tqq_in(cards)
        expected = [(0, 1, 2), (11, 12, 13)]

        self.assertEqual(result, expected)

    def test_hand_with_carre_and_tierce_thats_part_of_the_carre(self):
        cards = [3, 11, 12, 13, 21, 26, 30, 34]
        carre = carres_in(cards)

        result = tqq_in(cards, carre)
        expected = [(0,)]

        self.assertEqual(result, expected)

    # def test_hand_with_nothing_in_it(self):
    #     hand = ['AC', '9H', '8C', '9S', '7C', '9D', '10D', 'QD']

    #     result = declarations_in(hand)
    #     expected = [[],[]]


    # def test_setting_of_lad(self):
    #     an1 = [[5, 6], [5, 6, 7]]
    #     an2 = [[28, 29, 30, 31]]
    #     opp_ann = an1+an2

    #     result = set_lad(opp_ann)
    #     expected = 4.1

    #     self.assertEqual(result, expected)

    # def test_setting_of_lad_with_empty_opp_announcements(self):
    #     an1 = [[], []]
    #     an2 = [[]]
    #     opp_ann = an1+an2

    #     result = set_lad(opp_ann)
    #     expected = 0

    #     self.assertEqual(result, expected)

    # def test_invalid_tierce_and_valid_quinte(self):
    #     ann = [[0, 1, 2],[9, 8, 10, 11, 12]]
    #     lad = 4
        
    #     result = validate_all(ann, 4)
    #     expected = [[9, 8, 10, 11, 12]]

    #     self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()