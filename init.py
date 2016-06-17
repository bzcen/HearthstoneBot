import subprocess

choice = input("Enter 1 for Mac, 2 for Windows, 3 for Linux (yeah right): ");

if choice == 1:
	print "Running for Mac..."
	subprocess.call(('open', '../../../Applications/Hearthstone/Hearthstone.app'))

else:
	print "Running for Windows..."