import unittest
from game import Player

class TestPlayer(unittest.TestCase):
	def test_initialization(self):
		player = Player("Koko")
		wanted_result = {'name': 'Koko', 'cards': [], 'announcements': []}
		
		result = player.__dict__

		self.assertEqual(result, wanted_result)


	def test_initialization_with_parameters(self):
		player = Player("Koko", ["7s", "8s", "9s", "10c", "Jd", "Qd", "Kh", "As"],["tierce"])
		wanted_result = {'name': 'Koko', 'cards':["7s", "8s", "9s", "10c", "Jd", "Qd", "Kh", "As"],'announcements':['tierce']}

		result = player.__dict__

		self.assertEqual(result, wanted_result)

	def test_get_points_with_empty_announcements_should_return_zero(self):
		player = Player("Koko", ["7s", "8s", "9s", "10c", "Jd", "Qd", "Kh", "As"])

		self.assertEqual(player.get_points(),0)

	def test_get_points_with_announcements(self):
		player = Player("Koko",announcements = ["belote","tierce"])

		self.assertEqual(player.get_points(),40)


if __name__ == '__main__':
	unittest.main()