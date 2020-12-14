# Import the module
import subprocess 

# Ask the user for input
host = raw_input("Enter a host to ping: ")	

# Set up the echo command and direct the output to a pipe
p1 = subprocess.Popen(['nmap', '-sP', host], stdout=subprocess.PIPE)
if p1 < 0:
     print "Child was terminated by signal", -p1
else:
     print "Child returned", p1

# Run the command
output = p1.communicate()[0]

print output
