import os
import getpass
os.system("tput setaf 2")
print("\t\t\tWelcome to TUI - Linux Made Simple")
os.system("tput setaf 7")
print("\t\t\t----------------------------------")
password = getpass.getpass("Enter Your Password: ") # getpass won't show what is being typed as password
if password == "dheeth":
    print("Authentication Success")
else:
    print("Authentication Failed")
    exit()

location = input("Where You Would Like to Perform Your Tasks (Local/Remote)? ")
if location.lower() == "remote":
    if int(os.popen("which ssh | grep ssh | wc -l").read()) > 0:
        remote_ip = input("Enter the IP of remote system: ")
        print("Starting passwordless remote system authentication")
        pub_key_check = os.popen("ls ~/.ssh/ | grep id_rsa.pub | wc -l").read()
        if int(pub_key_check) > 0:
            print("Public Key Already Generated")
            ask_login = input("Have you logged in to this system through this TUI before? [yes/no] ")
            if ask_login.lower() == "yes" or ask_login.lower() == "y":
                pass
            elif ask_login.lower() == "no" or ask_login.lower() == "n":
                os.system("ssh-copy-id root@"+remote_ip)
            else:
                print("Invalid Response")
        elif int(pub_key_check) == 0:
            os.system("ssh-keygen; ssh-copy-id root@"+remote_ip)
    else:
        print("SSH is not installed in your system, please install ssh first")
while True:
    print('''
    Enter 1 for Basic Operations
    ''')
    ch = int(input("Enter Your Choice: "))
    if location.lower() == "local":
        pass
    if location.lower() == "remote":
        pass