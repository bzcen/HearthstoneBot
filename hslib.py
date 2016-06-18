# Library containing most Hearthstone-related data structures

# class for containing individual card
class Card:

	# id = easier identifier than card name?
	# name = card name as shown in logs
	# health = card health (nullable)
	# attack = card attack (nullable)

	def __init__(self, id, name, health, attack):
		self.id = self
		self.name = name
		self.health = health
		self.attack = attack


# class for current hand
class Hand:

	def __init__(self):
		self.handSize = 0
		self.cards = {}

	def drawCard(self, card):
		self.handSize += 1
		self.cards[len(self.cards)] = card

	# temp function for testing
	def playCard(self, index):
		print "Played " + self.cards[index].name
		del self.cards[index]
		self.handSize -= 1