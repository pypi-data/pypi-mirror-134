import os
from netmiko import ConnectHandler


def requesthost():
    host = input('Enter a host name: ')
    return host


def requestusername():
    username = input('Enter your username: ')
    return username


def requestpassword():
    password = input('Enter your password: ')
    return password


def createdevicedictionary(host, username, password):  # used with ConnectHandler()
    device = {
        'device_type': 'cisco_ios',
        'host': host,
        'username': username,
        'password': password
    }
    return device


def sshconnect(device):  # ssh to host
    connectdevice = ConnectHandler(**device)
    return connectdevice


def mycommands():  # input device, spit out commands for device
    commands = [
        'show ssh',
        'show ver',
    ]
    return commands


def createdirectory():  # create a folder on desktop to store output
    try:
        os.mkdir(os.path.expanduser('~/Desktop/Network Checks/'))
    except FileExistsError:
        pass


def runcommands(host, connectdevice, commands):  # runs commands and saves in a file
    path = os.path.expanduser('~/Desktop/Network Checks/')
    with open(path + host + '.txt', 'w') as newfile:
        for command in commands:
            result = connectdevice.send_command(command)
            newfile.write(result)


def sshdisconnect(connectdevice):
    connectdevice.disconnect()


def sessionsetup():  # data that wont change during session
    username, password = requestusername(), requestpassword()
    createdirectory()
    return username, password


def issuecommands(username, password):  # ssh to host, run commands
    host = requesthost()
    device = createdevicedictionary(host, username, password)
    connectdevice = sshconnect(device)
    commands = mycommands()  # input device
    runcommands(host, connectdevice, commands)
    sshdisconnect(connectdevice)


def additionalhosts(username, password):  # ask for additional host, repeat if applicable
    while True:
        print('Any additional hosts?')
        confirm = input('Enter "y" to continue: ')
        if confirm == 'y':
            issuecommands(username, password)
        else:
            break


def main():
    username, password = sessionsetup()
    issuecommands(username, password)
    additionalhosts(username, password)


main()
