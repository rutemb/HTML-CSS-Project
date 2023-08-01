import socket
import time

# IP and port of the Tello drone
tello_address = ('192.168.10.1', 8889)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a local port
sock.bind(('', 9000))

# Send the command to start command mode
sock.sendto(b'command', tello_address)
time.sleep(2)

# Function to send commands to the drone
def send_command(command):
    sock.sendto(command.encode(), tello_address)

# Takeoff
send_command('takeoff')
time.sleep(5)

# Move forward
send_command('forward 50')
time.sleep(5)

# Rotate clockwise
send_command('cw 90')
time.sleep(5)

# Move up
send_command('up 50')
time.sleep(5)

# Land
send_command('land')
time.sleep(5)

# Close the socket
sock.close()
