# SambaBF
Tool for brute-forcing samba logins. bf_smb_tmux.py is meant to be executed from computers with little amount of RAM.<br>
- The script does not use much more RAM than the wordlist it uses to crack the password.
**NB!** This script does not work since we could not store the output to a variable, just print it to stdout.
## Functions:
### connect_smb()
This function opens a pseudo terminal and executes a command that attempts a login at smb on port 445 and checks the output of the command.
If the login is successful the script will exit with code 0.
If the login is unsuccessful the loop will continue and another password attempt will 'take place'.

### get_next_pw()
This function fetches the password guess from wl.txt and returns it as a string. 
