from classes import Player, Dealer

match_won = False

# t1 = input('Team 1 name: ')
# t2 = input('Team 2 name: ')

# t1_pnames = input(f'"{t1}" players: ')
# t2_pnames = input(f'"{t2}" players: ')

# p1 = Player(t1_pnames.split(', ')[0], t1)
# p2 = Player(t2_pnames.split(', ')[0], t2)
# p3 = Player(t1_pnames.split(', ')[1], t1)
# p4 = Player(t2_pnames.split(', ')[1], t2)

p1 = Player('Ivan','Mecheta')
p2 = Player('Koko','Pandi')
p3 = Player('John','Mecheta')
p4 = Player('Niki','Pandi')

players = [p1, p2, p3, p4]

d = Dealer(players)

while not match_won:
    order = d.order()
    d.dealing(order)
    d.declare_round_trump()
    d.resolve_announcement_conflicts(order)
    d.score_round()
    d.check_for_won_games()
    match_won = d.check_for_match_win()
    # TODO: If 2 wins match_won = TRUE