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

        '''
            TODO the line below should be equal to method getting the call
            self.result_dict[game_number][round_number]['contract'] = self.get_call()
        '''
        self.result_dict[game_number][round_number][self.players[0].team_name] = self.get_team1_dict()
        self.result_dict[game_number][round_number][self.players[2].team_name] = self.get_team2_dict()

        self.save_to_json()

    def save_to_json(self, indent=4):
        name = self.players[0].team_name + '_vs_' + \
            self.players[2].team_name + ".json"
        f = open(name, "w")
        f.write(json.dumps(self.result_dict, indent=indent))

        f.close()

    def get_team1_dict(self):
        team_dict = dict()
        team_dict[self.players[0].name] = {
            "cards": self.players[0].hand, "announcements": self.players[0].announcements, "points": self.players[0].points}
        team_dict[self.players[1].name] = {
            "cards": self.players[1].hand, "announcements": self.players[1].announcements, "points": self.players[1].points}

        return team_dict

    def get_team2_dict(self):
        team_dict = dict()
        team_dict[self.players[2].name] = {
            "cards": self.players[0].hand, "announcements": self.players[0].announcements, "points": self.players[0].points}
        team_dict[self.players[3].name] = {
            "cards": self.players[1].hand, "announcements": self.players[1].announcements, "points": self.players[1].points}

        return team_dict

class WriteInFile():
    def write_in_file(self, name_of_file, string, mode):
        file = open(self.name, mode)
        file.write(string)
        file.close() 


class ToTxt(WriteInFile):
    # printing names of the teams
    def starter_line(self):
        self.name = self.players[0].team_name + '_vs_' + self.players[2].team_name + ".txt"
        entry_string = 6*' ' + self.players[0].team_name + 6*' ' + '|' + 6*' ' + self.players[2].team_name + 6*' ' + '\n'
        
        self.write_in_file(self.name, entry_string, 'w')

        self.entry_string_len = len(entry_string)
    # printing ======
    def line_of_equals(self):
        self.write_in_file(self.name, self.entry_string_len * '=' + '\n', 'a')

    # printing results if round points are equal to zero it won't add them
    def write_result(self):
        if(self.players[0].points + self.players[1].points == 0):
            score1 = str(self.players[0].team_points) 
        else:
            score1 = str(self.players[0].team_points) + ' + ' + str(self.players[0].points + self.players[1].points)
        if(self.players[2].points + self.players[3].points == 0):
            score2 = str(self.players[2].team_points)
        else:
            score2 = str(self.players[2].team_points) + ' + ' + str(self.players[2].points + self.players[3].points) 
        
        len_to_first_line = len(self.players[0].team_name) + 12

        final_string = score1 + (len_to_first_line - len(score1)) * ' ' + '| ' + score2 + '\n'
        
        self.write_in_file(self.name, final_string, 'a')

    # printing the score line
    def end_line(self):
        len_to_first_line = len(self.players[0].team_name) + 9
        string = f'({self.players[0].team_wins})' + len_to_first_line*' ' + '| ' + f'({self.players[2].team_wins})' + '\n'
        self.write_in_file(self.name, string, 'a')        


