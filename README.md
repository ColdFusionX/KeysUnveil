# Authenticated Memcached Keys Brute-force Script

#### NOTE: This Script is not a Exploit, It just automates the process of testing Keys manually on Memcached service supporting Binary Protocol 

Expected outcome: Discover Keys and there Values stored inside Memcached service

Intended only for educational and testing in corporate environments.

This Script was tested on Python 3.8.6

### Usage

```shell
cfx:  ~/Memcached_bruteforce 
→ ./keys_brute.py -h
usage: keys_brute.py [-h] [-l HOST] [-u USERNAME] [-p PASSWORD] [-w WORDLIST]

Authenticated Memcached Key Bruteforce Script by ColdFusionX

optional arguments:
  -h, --help            show this help message and exit
  -l HOST, --host HOST  Connection to Host -> IP:PORT (Example: 127.0.0.1:11211)
  -u USERNAME, --username USERNAME
                        Username
  -p PASSWORD, --password PASSWORD
                        Password
  -w WORDLIST, --wordlist WORDLIST
                        Bruteforce Dictionary

Script Usage : 
./keys_brute.py -l 127.0.0.1:11211 -u username -p password -w wordlist.txt

```
- Make sure Python3 is installed with following additional modules:

### Additional required Python modules :
- bmemcached
- pwn

Installation:
```shell
pip3 install pwn
pip3 install python-binary-memcached
```
### Proof of Concept :

This script expects four user inputs :
- **Host** - Connection to Host -> IP:PORT (Example: 127.0.0.1:11211)
- **Username** - Memcached Username
- **Password** - Memcached Password
- **Wordlist** - Dictionary for Bruteforce

#### Expected Output :

```shell
cfx:  ~/Memcached_bruteforce
→ ./keys_brute.py -l 127.0.0.1:11211 -u cold -p fusionx -w dictionary.txt

[*] Initiating Keys Bruteforce

[*] Key -> username
[+] Magnus
    Shockwave
    Optimus

[*] Key -> email
[+] Magnus@autobots.cy
    Shockwave@decepticons.cy
    Optimus@prime.cy

[*] Key -> password
[+] $2y$12$Vz8Z4adaLo3uKGaLpHa0IeuER15KtM0hAZuNy06OzCfThUD0gaFES
    $2y$12$2nmCPrn67.GdgjjBgE1q1.Y6B2sXICIHy3wTpib3O9OIQyfr/j/LO
    $2y$12$Gmiv7J69Xkh4ObQKhCbQ9uV6IWEvsAoMRp.kLzkrV8NO.WLT.ooUq 

```

### Reference

https://pypi.org/project/python-binary-memcached/

https://github.com/memcached/memcached/wiki/BinaryProtocolRevamped





