from random import shuffle, choice
from utils import declarations_in, set_lad, validate_all
from mixins import ToJson, ToTxt

class Player:
    def __init__(self, name, team_name):
        self.name = name
        self.hand = []
        self.all_announcements = []
        self.valid_announcements = []
        self.team_name = team_name
        self.points = 0
        self.team_points = 0
        self.team_wins = 0

    def announce(self):
        self.all_announcements = declarations_in(self.hand)

class Dealer(ToJson, ToTxt):
    def __init__(self, list_of_player_instances):
        self.players = list_of_player_instances
        self.round_trump = ''
        self.round_counter = 1
        self.game_counter = 1
        self.team1_lad = 0 #lowest allowed declaration, this = opposing team's highest declaration
        self.team2_lad = 0  #lowest allowed declaration, this = opposing team's highest declaration

    def order(self):
        order = [0, 1, 2, 3]
        rc = self.round_counter

        if self.round_counter <= 4: 
            pass 
        else:
            rc = self.round_counter % 4
        
        return order[rc-1:]+order[:rc-1]

    def dealing(self, order):
        suits = 'C', 'D', 'H', 'S' 
        faces = '7', '8', '9', '10', 'J', 'Q', 'K', 'A'
        deck = [f+s for s in suits for f in faces]
        shuffle(deck)

        self.players[order[0]].hand = deck[:8]
        self.players[order[1]].hand = deck[8:16]
        self.players[order[2]].hand = deck[16:24]
        self.players[order[3]].hand = deck[24:]


    def declare_round_trump(self):
        trumps = ['Clubs', 'Diamonds', 'Hearts', 'Spades', 'No trumps', 'All trumps']
        self.round_trump = choice(trumps)

    def resolve_announcement_conflicts(self, order):

        self.players[order[0]].announce()
        self.players[order[0]].valid_announcements = validate_all(self.players[order[0]].all_announcements)
        self.team2_lad = set_lad(self.players[order[0]].valid_announcements+self.players[order[2]].valid_announcements)

        self.players[order[1]].announce()
        self.players[order[1]].valid_announcements = validate_all(self.players[order[1]].all_announcements,self.team2_lad)
        self.team1_lad = set_lad(self.players[order[1]].valid_announcements+self.players[order[3]].valid_announcements)

        self.players[order[2]].announce()
        self.players[order[2]].valid_announcements = validate_all(self.players[order[2]].all_announcements,self.team1_lad)
        self.team2_lad = set_lad(self.players[order[0]].valid_announcements+self.players[order[2]].valid_announcements)

        self.players[order[3]].announce()
        self.players[order[3]].valid_announcements = validate_all(self.players[order[3]].all_announcements,self.team2_lad)
        self.team1_lad = set_lad(self.players[order[1]].valid_announcements+self.players[order[3]].valid_announcements)

        self.players[order[0]].valid_announcements = validate_all(self.players[order[0]].all_announcements,team1_lad)
        self.players[order[1]].valid_announcements = validate_all(self.players[order[1]].all_announcements,team2_lad)

    def score_round(): #def add_round_score_to_team_score  
        pass

    def check_for_wins():
        self.write_result()
        self.to_json()
        self.players[0].team_points += self.players[0].points + self.players[2].points
        self.players[2].team_points += self.players[0].points + self.players[2].points
        self.players[0].points = 0
        self.players[2].points = 0

        self.players[1].team_points += self.players[1].points + self.players[3].points
        self.players[3].team_points += self.players[1].points + self.players[3].points
        self.players[1].points = 0
        self.players[3].points = 0
        
        if self.players[0].team_points > 150 and self.players[1].team_points > 150:
            
            if self.players[0].team_points == max(self.players[0].team_points, self.players[1].team_points):
                self.players[0].team_wins +=1
                self.players[2].team_wins +=1
                self.score_line()
            else:
                self.players[1].team_wins +=1
                self.players[3].team_wins +=1
                self.score_line()
        
        elif self.players[0].team_points > 150:
            self.players[0].team_wins +=1
            self.players[2].team_wins +=1
            self.score_line()

        elif self.players[1].team_points > 150:
            self.players[1].team_wins +=1
            self.players[3].team_wins +=1
            self.score_line()