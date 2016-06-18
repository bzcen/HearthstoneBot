import subprocess, hslib

choice = input("Enter 1 for Mac, 2 for Windows, 3 for Linux (yeah right): ");

if choice == 1:
	print "Running for Mac..."
	subprocess.call(('open', '../../../Applications/Hearthstone/Hearthstone.app'))

else:
	print "Running for Windows..."
	c = hslib.Card(1, "Coldlight Oracle", 2, 2)
	h = hslib.Hand()
	print "My hand size is " + str(h.handSize)
	print "Draw"
	h.drawCard(c)
	print "My hand size is " + str(h.handSize)
	h.playCard(0)
	print "My hand size is " + str(h.handSize)