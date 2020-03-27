import json

class ToJson():
	def __init__(self):
		self.result_dict = dict()
		self.result_dict["game 1"] = dict()
		self.result_dict["game 1"]["round 1"] = dict()


	def to_json(self):			
		game_number = "game " + str(self.game_counter + 1)
		round_number = "round " + str(self.round_counter + 1)
		# if there isn't dictionary with associated with this game it creates new
		if not game_number in self.result_dict:
			self.result_dict[game_number] = dict()
		# if there isn't dictionary associated with this round it creates new one
		if not round_number in self.result_dict[game_number]:
			self.result_dict[game_number][round_number] = dict()
	
		self.result_dict[game_number][round_number][self.players[0].team_name] = self.get_team1_dict()
		self.result_dict[game_number][round_number][self.players[2].team_name] = self.get_team2_dict()
		
		self.save_to_json()

	def save_to_json(self, indent = 4):
		name = self.players[0].team_name + '_vs_' + self.players[2].team_name + ".json"
		f = open(name, "w")
		f.write(json.dumps(self.result_dict, indent = indent))

		f.close()


	def get_team1_dict(self):
		team_dict = dict()
		team_dict[self.players[0].name] = {"cards": self.players[0].hand, "announcements": self.players[0].announcements, "points": self.players[0].points}
		team_dict[self.players[1].name] = {"cards": self.players[1].hand, "announcements": self.players[1].announcements, "points": self.players[1].points}

		return team_dict

	def get_team2_dict(self):
		team_dict = dict()
		team_dict[self.players[2].name] = {"cards": self.players[0].hand, "announcements": self.players[0].announcements, "points": self.players[0].points}
		team_dict[self.players[3].name] = {"cards": self.players[1].hand, "announcements": self.players[1].announcements, "points": self.players[1].points}

		return team_dict


		

