#The purpose of this script is to parse the INTERFACES file and generate a 
#NETMAP file to run the emulator
import socket
print "Starting NETMAP generator . . . "
myfile = open("INTERFACES", "r")
lines = myfile.read().split("\n")
del lines[len(lines) -1]
print lines
netmap = open("NETMAP", "w")
a = 21
for line in lines:
	tokens = line.split(":")
	slot = int(tokens[0])
	port = int(tokens[1])
	interface = tokens[2]
	netmap.write("10" + str(slot) + "/" + str(port) + "@" + socket.gethostname() + "\t" + str(a) + ":" + "0/0" + "@" + socket.gethostname())


