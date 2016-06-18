import subprocess, hslib

choice = input("Enter 1 for Mac, 2 for Windows, 3 for Linux (yeah right): ");

if choice == 1:
	print "Running for Mac..."
	subprocess.call(('open', '../../../Applications/Hearthstone/Hearthstone.app'))

else:
	print "Running for Windows..."
	c = hslib.Card(1, "Coldlight Oracle", 2, 2)
	h = hslib.Hand()
	h.drawCard(c)
	h.playCard(0)