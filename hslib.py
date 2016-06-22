# Library containing most Hearthstone-related data structures
import random

# class for containing individual card
class Card:

	# id = easier identifier than card name?
	# name = card name as shown in logs
	# health = card health (nullable)
	# attack = card attack (nullable)
	# cost = card mana cost (in number of crystals)

	# if any of the parameters are left unfilled, replace with None
	def __init__(self, id = None, name = None, health = None, attack = None, cost = None):
		self.id = self
		self.name = name
		self.health = health
		self.attack = attack


# class for current hand
class Hand:

	def __init__(self):
		self.cards = {}

	def drawCard(self, card):
		self.cards[len(self.cards)] = card

	# temp function for testing
	def playCard(self, index):
		print "Played " + self.cards[index].name
		del self.cards[index]

# class for deck
class Deck:

	# pulls the card from an external file
	def __init__(self, import_file):

		# TODO: write a parser of a deck file to make the deck, 30 cards total
		self.cards = [ Card(0, "Savannah Highmane") for i in range(29)]

	def popTop(self):
		card = self.cards.pop()

	def shuffle(self):
		random.shuffle(self.cards)

	def printRemainingCards(self):
		for i in range(len(self.cards)):
			print self.cards[i].name







