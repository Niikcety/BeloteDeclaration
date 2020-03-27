import unittest
import json
from classes import Dealer, Player


class TestToJson(unittest.TestCase):
    def test_initialization(self):
        dealer = Dealer([Player("Niki", "Mecheta"), Player(
            "Vanko", "Mecheta"), Player("Koko", "Pandi"), Player("Kiro", "Pandi")])
        self.assertEqual(dealer.result_dict, {'game 1': {'round 1': {}}})

    def test_to_json_with_no_new_round_should_create_new_dict_in_game(self):
        dealer = Dealer([Player("Niki", "Mecheta"), Player(
            "Vanko", "Mecheta"), Player("Koko", "Pandi"), Player("Kiro", "Pandi")])

        dealer.to_json()
        wanted_result = {'game 1': {
            'round 1': {
                'Mecheta': {
                    'Niki': {'cards': [], 'announcements': [], 'points': 0},
                    'Vanko': {'cards': [], 'announcements': [], 'points': 0}},
                'Pandi': {
                    'Koko': {'cards': [], 'announcements': [], 'points': 0},
                    'Kiro': {'cards': [], 'announcements': [], 'points': 0}}}}}

        self.assertEqual(wanted_result, dealer.result_dict)

    def test_to_json_with_new_round_should_create_new_dict_in_game(self):
        dealer = Dealer([Player("Niki", "Mecheta"), Player(
            "Vanko", "Mecheta"), Player("Koko", "Pandi"), Player("Kiro", "Pandi")])
        dealer.to_json()

        dealer.__setattr__('round_counter', 1)
        dealer.to_json()

        wanted_result = {'game 1': {
            'round 1': {
                'Mecheta': {
                    'Niki': {'cards': [], 'announcements': [], 'points': 0},
                    'Vanko': {'cards': [], 'announcements': [], 'points': 0}},
                'Pandi': {
                    'Koko': {'cards': [], 'announcements': [], 'points': 0},
                    'Kiro': {'cards': [], 'announcements': [], 'points': 0}}},
            'round 2': {
                'Mecheta': {
                    'Niki': {'cards': [], 'announcements': [], 'points': 0},
                    'Vanko': {'cards': [], 'announcements': [], 'points': 0}},
                'Pandi': {
                    'Koko': {'cards': [], 'announcements': [], 'points': 0},
                    'Kiro': {'cards': [], 'announcements': [], 'points': 0}}}}}

        self.assertEqual(wanted_result, dealer.result_dict)

    def test_to_json_with_new_game_should_create_new_dict_in_result_dict(self):
        dealer = Dealer([Player("Niki", "Mecheta"), Player(
            "Vanko", "Mecheta"), Player("Koko", "Pandi"), Player("Kiro", "Pandi")])
        dealer.to_json()

        dealer.__setattr__('game_counter', 1)
        dealer.to_json()

        wanted_result = {'game 1': {
            'round 1': {
                'Mecheta': {
                    'Niki': {'cards': [], 'announcements': [], 'points': 0},
                    'Vanko': {'cards': [], 'announcements': [], 'points': 0}},
                'Pandi': {
                    'Koko': {'cards': [], 'announcements': [], 'points': 0},
                    'Kiro': {'cards': [], 'announcements': [], 'points': 0}}}},
            'game 2': {
            'round 1': {
                'Mecheta': {
                    'Niki': {'cards': [], 'announcements': [], 'points': 0},
                    'Vanko': {'cards': [], 'announcements': [], 'points': 0}},
                'Pandi': {
                    'Koko': {'cards': [], 'announcements': [], 'points': 0},
                    'Kiro': {'cards': [], 'announcements': [], 'points': 0}}}}}

        self.assertEqual(wanted_result, dealer.result_dict)

    def test_get_team1_and_get_team2_dict(self):
        dealer = Dealer([Player("Niki", "Mecheta"), Player(
            "Vanko", "Mecheta"), Player("Koko", "Pandi"), Player("Kiro", "Pandi")])

        wanted_result_team1 = {"Niki": {"cards": [], "announcements": [
        ], 'points': 0}, "Vanko": {"cards": [], "announcements": [], 'points': 0}}
        wanted_result_team2 = {"Koko": {"cards": [], "announcements": [
        ], 'points': 0}, "Kiro": {"cards": [], "announcements": [], 'points': 0}}

        self.assertEqual(wanted_result_team1, dealer.get_team1_dict())
        self.assertEqual(wanted_result_team2, dealer.get_team2_dict())

    def test_save_to_json(self):
        dealer = Dealer([Player("Niki", "Mecheta"), Player(
            "Vanko", "Mecheta"), Player("Koko", "Pandi"), Player("Kiro", "Pandi")])
        dealer.to_json()

        with open("Mecheta_vs_Pandi.json", "r") as read_file:
            jsonned = json.load(read_file)

        self.assertEqual(jsonned, dealer.result_dict)

    def test_save_to_json_after_round_change_and_game_change(self):
        dealer = Dealer([Player("Niki", "Mecheta"), Player(
            "Vanko", "Mecheta"), Player("Koko", "Pandi"), Player("Kiro", "Pandi")])

        dealer.to_json()
        dealer.__setattr__('round_counter', 1)
        dealer.to_json()
        dealer.__setattr__('game_counter', 1)
        dealer.__setattr__('round_counter', 0)
        dealer.to_json()

        with open("Mecheta_vs_Pandi.json", "r") as read_file:
            jsonned = json.load(read_file)

        self.assertEqual(jsonned, dealer.result_dict)


if __name__ == '__main__':
    unittest.main()
