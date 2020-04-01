import unittest
from classes import Player, Dealer

class TestFunctionsInClasses(unittest.TestCase):

    def test_declaration_announcement_if_round_trump_is_no_trumps(self):
        p1 = Player('Choko', 'Qgoda' )
        p2 = Player('Doko', 'Chereshka' )
        p3 = Player('Boko', 'Qgoda' )
        p4 = Player('Toko', 'Chereshka')
        players = [p1, p2, p3, p4]

        order = [0, 1, 2, 3]
        d = Dealer(players)
        d.round_trump = 'No trumps'
        d.dealing(order)
        d.resolve_announcement_conflicts(order)

        result0 = d.players[0].all_announcements
        result1 = d.players[1].all_announcements
        result2 = d.players[2].all_announcements
        result3 = d.players[3].all_announcements
        expected = []

        self.assertEqual(result0, result3, expected)

if __name__ == '__main__':
    unittest.main()