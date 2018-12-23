#!/usr/bin/env python

# Python Port Scanner

import socket, subprocess, sys
from datetime import datetime

# Clears the screen
subprocess.call('clear',shell=True)

# Ask for remote host to scan
target = input('Target: ')

# Translate domain to IPv4 address
target_ip = socket.gethostbyname(target)
print('Target\'s IP: ' + str(target_ip))

# Option for single port scan
single = input('Input specific port or use \'default\' [default = 1 - 1024]: ')

while(single == ''):
    single = input('Please input a valid choice (default or port number): ')

# Separate information with dashes
print('-' * 50)
print('Scanning ' + str(target_ip))
print('-' * 50)

# Counter
count = 0

# Begin timing the scan
t_initial = datetime.now()

# Scan ports from 1-1024 or specific port
# Use exceptions for errors

try:
    if single != 'default':
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        fail = sock.connect_ex((target_ip, int(single)))

        if fail == False:
            print('Port ' + single + ': Open')
            count += 1
        else:
            print('Port ' + single + ': Closed')
        
        sock.close()

    else:
        for port in range(1,1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            fail = sock.connect_ex((target_ip,port))
            
            if fail == False:
                count += 1
                print('Port ' + str(port) + ':  Open')
                
            sock.close()

except socket.error:
    print('Error: Unable to connect to target')
    sys.exit()

except socket.gaierror:
    print('Error: Target cannot be resolved')
    sys.exit()

except KeyboardInterrupt:
    print('Alert: Keyboard interrupt detected... exiting program')
    sys.exit()

# End timing
t_end = datetime.now()

# Total time
t_result = t_end - t_initial

print('-' * 50)

# Analysis
print('Scanning Complete')
print('Target: ' + target)
print('IP: ' + str(target_ip))
print('Time Elapsed: ' + str(t_result))
print('Number of ports open: ' + str(count))
