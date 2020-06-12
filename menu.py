# Import Modules

import os
import getpass

# Header Section

os.system("tput setaf 2")
print("\t\t\tWelcome to TUI - Linux Made Simple")
os.system("tput setaf 7")
print("\t\t\t----------------------------------")

# Authentication for TUI

# getpass won't show what is being typed as password
password = getpass.getpass("Enter Your Password: ")
if password == "dheeth":
    print("Authentication Success")
else:
    print("Authentication Failed")
    exit()

location = input("Where You Would Like to Perform Your Tasks (Local/Remote)? ")

# Authentication for Remote Login

if location.lower() == "remote":
    # check if ssh is installed in the system
    if int(os.popen("which ssh | grep ssh | wc -l").read()) > 0:
        remote_ip = input("Enter the IP of remote system: ")
        print("Starting passwordless remote system authentication")
        # check if ssh key is generated
        pub_key_check = os.popen("ls ~/.ssh/ | grep id_rsa.pub | wc -l").read() 
        if int(pub_key_check) > 0:
            print("Public Key Already Generated")
            # check if key already copied to the given ip
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
        # ask for ssh installation in the system
        ask_ssh_install = input("Do you want to install ssh now? [yes/no] ")
        if ask_ssh_install.lower() == "yes" or ask_ssh_install.lower() == "y":
            os.system("yum install openssh-clients -y")
        elif ask_ssh_install.lower() == "no" or ask_ssh_install.lower() == "n":
            print("Okay! Have a Good Day")
        else:
            print("Invalid Response")
while True:
    # Ask the choice to perform the operations
    print('''
    Enter 1 for Basic Operations
    ''')
    choice = int(input("Enter Your Choice: "))
    if location.lower() == "local":
        if choice == 1:
            while True:
                print('''
    Enter 1 to Change Directory
    Enter 2 to list the files and folders in the Current Directory
    Enter 3 to Check the location of a program file
                ''')
                basic_choice = int(input("Enter Your Choice: "))
                if basic_choice == 1:
                    path = input("Enter the Path Where you want to navigate: ")
                    os.chdir(path)
                if basic_choice == 2:
                    ask_hidden_files = input("Do you want to list hidden files and folders in the directory too? [yes/no] ")
                    if ask_hidden_files.lower() == "yes" or ask_hidden_files.lower() == "y":
                        os.system("ls -a ")
                    elif ask_hidden_files.lower() == "no" or ask_hidden_files.lower() == "n":
                        os.system("ls ")
                    else:
                        print("Invalid Response")
                if basic_choice == 3:
                    program_name = input("Enter the program name you want the location for: ")
                    os.system("which " + program_name)
    if location.lower() == "remote":
        if choice == 1:
            while True:
                print('''
    Enter 1 to Change Directory
    Enter 2 to list the files and folders in the Current Directory
    Enter 3 to Check the location of a program file
                ''')
                basic_choices = input("Enter All your choices separated by ',' to perform in your remote system together: ").strip().split(',')
                chosen = []
                if '1' in basic_choices:
                    path = input("Enter the Path Where you want to navigate: ")
                if '2' in basic_choices:
                    ask_hidden_files = input("Do you want to list hidden files and folders in the directory too? [yes/no] ")
                    if ask_hidden_files.lower() == "yes" or ask_hidden_files.lower() == "y":
                        chosen.append("ls -a " + path)
                    elif ask_hidden_files.lower() == "no" or ask_hidden_files.lower() == "n":
                        chosen.append("ls" + path)
                    else:
                        print("Invalid Response")
                if '3' in basic_choices:
                    program_name = input("Enter the program name you want the location for: ")
                    chosen.append("which " + program_name)

                os.system("ssh root@{0} ".format(remote_ip) + "&& ".join(chosen))