#The purpose of this script is to parse the INTERFACES file and generate a 
#NETMAP file to run the emulator
import socket
import subprocess
print "Starting NETMAP generator . . . "
myfile = open("/root/INTERFACES", "r")
lines = myfile.read().split("\n")
del lines[len(lines) -1]
print lines
netmap = open("/root/NETMAP", "w")
a = 21
components = []
for line in lines:
	tokens = line.split(":")
	slot = int(tokens[0])
	port = int(tokens[1])
	interface = tokens[2]
	components.append(["perl", "/root/iou2net/iou2net.pl", "-p",str(a),"-i",interface])
	netmap.write("10:" + str(slot) + "/" + str(port) + "@" + socket.gethostname() + "\t" + str(a) + ":" + "0/0" + "@" + socket.gethostname())
	a+=1
netmap.close()
myfile.close()
subprocess.Popen(["/root/image.bin","10"])
for component in components:
	subprocess.Popen(component)

