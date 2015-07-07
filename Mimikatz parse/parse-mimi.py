#
# Parses a Mimikatz dump (mimikatz # sekurlsa::logonPasswords)
# and extracts DOMAIN/USERNAME:PASSWORD
#
# Useful when dealing with large mimikatz dumps... like dumps from an active Exchange server :)


import sys

def resetCounters():
	global gotUsername
	global gotPassword
	global gotDomain
	global usernameValue
	global domainValue
	global passwordValue
	gotUsername = 0
	gotPassword = 0
	gotDomain = 0
	usernameValue = ""
	domainValue = ""
	passwordValue = ""


if (len(sys.argv) < 2):
	print "Usage goes here"
elif (len(sys.argv) == 2):
	filename = sys.argv[1]
else:
	print "Usage goes here"

text_file = open(filename, "r")
lines = text_file.readlines()
gotUsername = 0
gotPassword = 0
gotDomain = 0
usernameValue = ""
domainValue = ""
passwordValue = ""

for encoded in lines:
	# We've hit a new user/credential record, reset counters
	if "Authentication Id :" in encoded:
		print domainValue + "\\" + usernameValue + ":" + passwordValue
		resetCounters()
	elif (("Username :" in encoded) and (gotUsername < 1)):			
		usernameValue = encoded.split(":")[1].strip()
		gotUsername = 1
	elif (("Domain   :" in encoded) and (gotDomain < 1)):			
		domainValue = encoded.split(":")[1].strip()
		gotDomain = 1
	elif (("Password :" in encoded) and (gotPassword < 1)):			
		passwordValue = encoded.split(":")[1].strip()
		gotPassword = 1