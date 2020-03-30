import unittest
from utils import numbify, carre_in, seq_in

class TestFunctionsInUtils(unittest.TestCase):
	
	def test_numbify(self):
		hand = ['7C', 'JD', 'AS', 'QD', '8C', '9S', '10D', 'JS']

		result = numbify(hand)
		expected = [0, 1, 12, 13, 14, 29, 31, 34]

		self.assertEqual(result, expected)

	def test_hand_with_carre_of_9s(self):
		hand = ['7C', '9D', 'AS', 'QD', '9C', '9S', '10D', '9H']
		cards = numbify(hand)

		result = carre_in(cards)
		expected = [[2, 11, 20, 29]]

		self.assertEqual(result, expected)

	def test_hand_with_two_carres(self):
		hand = ['AC', 'AD', 'AH', 'AS', '9C', '9S', '9D', '9H']
		cards = numbify(hand)

		result = carre_in(cards)
		expected = [[2, 11, 20, 29], [7, 16, 25, 34]]

		self.assertEqual(result, expected)

	def test_hand_with_carre_of_7s(self):
		hand = ['7C', '7D', 'AS', 'QD', '9C', '7S', '10D', '7H']
		cards = numbify(hand)

		result = carre_in(cards)
		expected = []

		self.assertEqual(result, expected)

	def test_hand_with_belote_and_two_tierces(self):
		hand = ['KH', 'QH', '8C', '7C', '9C', '9D', '10D', 'JD']
		cards = numbify(hand)

		result = seq_in(cards)
		expected = [[0, 1, 2], [11, 12, 13], [23, 24]]

		self.assertEqual(result, expected)

	def test_hand_with_carre_and_tierce_thats_part_of_the_carre(self):
		hand = ['AC', '9H', '8C', '9S', '9C', '9D', '10D', 'JD']
		cards = numbify(hand)
		control = carre_in(cards)

		result = seq_in(cards, control)
		expected = []

		self.assertEqual(result, expected)


if __name__ == '__main__':
	unittest.main()