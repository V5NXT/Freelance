import sys #used to get commandline arguments
import re #used for regular expressions


def exists(hostname):
   
    if 'linux' in sys.platform:
        filename = '/etc/hosts'
    else:
        filename = 'c:\windows\system32\drivers\etc\hosts'
    f = open(filename, 'r')
    hostfiledata = f.readlines()
    f.close()
    for item in hostfiledata:
        if hostname in item:
            return True
    return False


def update(hostname):
  
    if 'linux' in sys.platform:
        filename = '/etc/hosts'
    else:
        filename = 'c:\windows\system32\drivers\etc\hosts'
    outputfile = open(filename, 'a')
    entry = "127.0.0.1" + " " + hostname + "\n"
    outputfile.writelines(entry)
    outputfile.close()




def isValidHostname(hostname):

    if len(hostname) > 255:
        return False
    if hostname[0].isdigit(): return False
    if hostname[-1:] == ".":
        hostname = hostname[:-1] # strip exactly one dot from the right, if present
    allowed = re.compile("(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)
    return all(allowed.match(x) for x in hostname.split("."))


def main():
   
    hostname = "demo009.saas-portal-10.local"
    
    if not isValidHostname(hostname): #checks the host name to see if it's valid.
        print(hostname, "is not a valid hostname. Usage: hostfileupdate.py [ipadddress] [hostmame]")
        sys.exit(2)

    if exists(hostname): #checks to see if the host name already exists in the host file and exits if it does.
        print(hostname, 'already exists in the hostfile.')
        sys.exit(2)

    update(hostname) #Calls the update function.


if __name__ == '__main__':
    main()
