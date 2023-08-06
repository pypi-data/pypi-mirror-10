# crowd_pam #

Linux Pluggable Authentication Module (PAM) to allow Linux systems to 
authenticate end-users against Atlassian Crowd identity management 
systems.

Given an Atlassian Crowd server with either its internal user database 
or some other backend user management system (e.g. LDAP), this utility 
makes it possible to establish a single-sign-on environment for Linux 
systems whereby users can log into Linux systems with the same password
they use against other Crowd backed systems.

When a user attempts to log into a Linux system running crowd_pam.py,
the username is verified against Crowd and if the user exists in Crowd, 
a corresponding local Linux user account will be created.  Then if the 
user's username and password pass authentication, the user will be 
allowed to sign into the system.

If the user is a member of groups in Crowd that do not exist on the 
local Linux machine, crowd_pam.py will create the groups on the local 
Linux system.  If a user is removed from a group membership on Crowd, 
he/she will be removed from the user group on the local Linux system.


## Requirements ##
    - pam_python (Availible in ubuntu as libpam-python)
    - pip install Crowd
    - pip install requests

Use crowd_pam_configure to generate a config file to place in /etc/crowd_pam.conf