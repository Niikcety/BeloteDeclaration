suites = ['C', 'D', 'H', 'S']
faces = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']

deck = [f+s for s in suites for f in faces]
num = [i for i in range(35)]

del num[8::9] 
'''This removes 8, 17 & 26 from the list. 
The idea is to give non-sequential values to Aces and 7s 
of different suites in the dictionary below.''' 

int_of_card_dict = {k: v for k, v in zip(deck, num)}


belote_dict = {
    (5, 6): ['belote', 20],   # of Clubs
    (14, 15): ['belote', 20], # of Diamonds
    (23, 24): ['belote', 20], # of Hearts
    (32, 33): ['belote', 20]  # of Spades
}

carre_dict = {
    (2, 11, 20, 29): ['carre', 150], # of 9s
    (3, 12, 21, 30): ['carre', 100], # of 10s
    (4, 13, 22, 31): ['carre', 200], # of Js
    (5, 14, 23, 32): ['carre', 100], # of Qs
    (6, 15, 24, 33): ['carre', 100], # of Ks
    (7, 16, 25, 34): ['carre', 100], # of As
}

#tqq = tierce, quarte, quinte
tqq_dict = {
    (0, 1, 2): ['tierce', 20, 3.0],
    (1, 2, 3): ['tierce', 20, 3.1],
    (2, 3, 4): ['tierce', 20, 3.2],
    (3, 4, 5): ['tierce', 20, 3.3],
    (4, 5, 6): ['tierce', 20, 3.4],
    (5, 6, 7): ['tierce', 20, 3.5],
    (0, 1, 2, 3): ['quarte', 50, 4.0],
    (1, 2, 3, 4): ['quarte', 50, 4.1],
    (2, 3, 4, 5): ['quarte', 50, 4.2],
    (3, 4, 5, 6): ['quarte', 50, 4.3],
    (4, 5, 6, 7): ['quarte', 50, 4.4],
    (0, 1, 2, 3, 4): ['quinte', 100, 5.0],
    (1, 2, 3, 4, 5): ['quinte', 100, 5.1],
    (2, 3, 4, 5, 6): ['quinte', 100, 5.2],
    (3, 4, 5, 6, 7): ['quinte', 100, 5.3],
    (9, 10, 11): ['tierce', 20, 3.0],
    (10, 11, 12): ['tierce', 20, 3.1], 
    (11, 12, 13): ['tierce', 20, 3.2],
    (12, 13, 14): ['tierce', 20, 3.3],
    (13, 14, 15): ['tierce', 20, 3.4],
    (14, 15, 16): ['tierce', 20, 3.5],
    (9, 10, 11, 12): ['quarte', 50, 4.0],
    (10, 11, 12, 13): ['quarte', 50, 4.1], 
    (11, 12, 13, 14): ['quarte', 50, 4.2],
    (12, 13, 14, 15): ['quarte', 50, 4.3],
    (13, 14, 15, 16): ['quarte', 50, 4.4],
    (9, 10, 11, 12, 13): ['quinte', 100, 5.0],
    (10, 11, 12, 13, 14): ['quinte', 100, 5.1], 
    (11, 12, 13, 14, 15): ['quinte', 100, 5.2],
    (12, 13, 14, 15, 16): ['quinte', 100, 5.3],
    (18, 19, 20): ['tierce', 20, 3.0],
    (19, 20, 21): ['tierce', 20, 3.1],
    (20, 21, 22): ['tierce', 20, 3.2],
    (21, 22, 23): ['tierce', 20, 3.3],
    (22, 23, 24): ['tierce', 20, 3.4],
    (23, 24, 25): ['tierce', 20, 3.5],
    (18, 19, 20, 21): ['quarte', 50, 4.0],
    (19, 20, 21, 22): ['quarte', 50, 4.1],
    (20, 21, 22, 23): ['quarte', 50, 4.2],
    (21, 22, 23, 24): ['quarte', 50, 4.3],
    (22, 23, 24, 25): ['quarte', 50, 4.4],
    (18, 19, 20, 21, 22): ['quinte', 100, 5.0],
    (19, 20, 21, 22, 23): ['quinte', 100, 5.1],
    (20, 21, 22, 23, 24): ['quinte', 100, 5.2],
    (21, 22, 23, 24, 25): ['quinte', 100, 5.3],
    (27, 28, 29): ['tierce', 20, 3.0],
    (28, 29, 30): ['tierce', 20, 3.1], 
    (29, 30, 31): ['tierce', 20, 3.2],
    (30, 31, 32): ['tierce', 20, 3.3],
    (31, 32, 33): ['tierce', 20, 3.4],
    (32, 33, 34): ['tierce', 20, 3.5],
    (27, 28, 29, 30): ['quarte', 50, 4.0],
    (28, 29, 30, 31): ['quarte', 50, 4.1],
    (29, 30, 31, 32): ['quarte', 50, 4.2],
    (30, 31, 32, 33): ['quarte', 50, 4.3],
    (31, 32, 33, 34): ['quarte', 50, 4.4],
    (27, 28, 29, 30, 31): ['quinte', 100, 5.0],
    (28, 29, 30, 31, 32): ['quinte', 100, 5.1],
    (29, 30, 31, 32, 33): ['quinte', 100, 5.2],
    (30, 31, 32, 33, 34): ['quinte', 100, 5.3]
    }