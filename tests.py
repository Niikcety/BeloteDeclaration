import unittest
from utils import numbify, carre_in

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
		expected = ['carre_of_9s']

		self.assertEqual(result, expected)

	def test_hand_with_two_carres(self):
		hand = ['AC', 'AD', 'AH', 'AS', '9C', '9S', '9D', '9H']
		cards = numbify(hand)

		result = carre_in(cards)
		expected = ['carre_of_9s', 'carre_of_As']

		self.assertEqual(result, expected)

	def test_hand_with_carre_of_7s(self):
		hand = ['7C', '7D', 'AS', 'QD', '9C', '7S', '10D', '7H']
		cards = numbify(hand)

		result = carre_in(cards)
		expected = []

		self.assertEqual(result, expected)


if __name__ == '__main__':
	unittest.main()