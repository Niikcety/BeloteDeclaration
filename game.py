class Player:
	def __init__(self, name, cards = None, announcements = None):
		self.name = name
		if cards == None:
			self.cards = []
		else:
			self.cards = cards
		if announcements == None:
			self.announcements = []
		else:
			self.announcements = announcements

	def get_points(self):
		points = 0
		for i in self.announcements:
			if i == 'belote':
				points += 20
			elif i == 'tierce':
				points += 20
			elif i == 'quarte':
				points += 50
			elif i == 'quinte':
				points += 100
			else:
				# TODO: different carre's
				points += 150

		return points



