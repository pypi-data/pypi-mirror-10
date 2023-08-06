crowd_pam.py
=============

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