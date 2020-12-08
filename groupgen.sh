#!/bin/bash

#create groups and give admins sudo abilities
groupadd admin
groupadd developers
groupadd staff
groupadd temp

#making new directory folders for each group preferably in the /usr directory
mkdir /usr/admin
mkdir /usr/developers
mkdir /usr/staff
mkdir /usr/temp

#make read only folders and place them in the new group folders
mkdir /usr/admin/readme
mkdir /usr/developers/readme
mkdir /usr/staff/readme
mkdir /usr/temp/readme

#create policy files by moving into the readme file.
cd /usr/admin/readme 
touch policies.txt
cd /usr/developers/readme
touch policies.txt
cd /usr/staff/readme
touch policies.txt
cd /usr/temp/readme

#give the readme folders read only permissions
chmod 444 /usr/admin/readme
chmod 444 /usr/developers/readme
chmod 444 /usr/staff/readme
chmod 444 /usr/temp/readme

#change the default group from root to their assigned folders 
chgrp admin /usr/admin
chgrp developers /usr/developers
chgrp staff /usr/staff
chgrp temp /usr/temp
