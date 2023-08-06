# showdown
A tool to automate local network health checks on Cisco iOS devices.
+ You will be prompted to enter a username/password
+ A folder will be generated on your local desktop
+ You will then enter the FQDN
+ showdown will ssh to the device
+ Execute each show command *(NOT in enable)*
+ Defaults are; 'show ssh' + 'show ver'
+ The command output is then saved to the folder on your local desktop
+ You will then be prompted to enter additional FQDN, to repeat the above using the original username/password entered at the start of session
+ When finished, enter 'y'

##Requires
>Python 3.8

>Windows 10

##Install:

>pip install showdown.ssh

##Run:
**View install directory:**

>pip show showdown.ssh

**Launch the app:**

1. navigate to directory 
2. navigate to /showdown.ssh
>python3 main.py

##Uninstall:

>pip uninstall -y showdown.ssh
___

`https://pypi.org/project/showdown.ssh/`