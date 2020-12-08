#!/bin/bash

#Ascending order with line ranges to assign usernames with 4 split text files used for input below
sed -n '1,2p' /home/wtrue/Lab2/usernames.txt > admins.txt
sed -n '3,13p' /home/wtrue/Lab2/usernames.txt > devs.txt
sed -n '14,24p' /home/wtrue/Lab2/usernames.txt > staff.txt
sed -n '25,220p' /home/wtrue/Lab2/usernames.txt > temp.txt

file=/home/wtrue/Lab2/admins.txt #Declare text file to a variable
write=$(cat "$file") #Read text file and make that read equal to variable write
for i in $write #Loop until it finishes processing every line iteration
do useradd $i #Add users by processing each line
   adduser $i admin #Iterate the following users to the admin group
   adduser $i sudo #Also assign every admin to the sudo permissions group   
done	

file=/home/wtrue/Lab2/devs.txt #Declare text file to a variable
write=$(cat "$file") #Read text file and make that read equal to variable write
for i in $write #Loop until it finishes processing every line iteration
do useradd $i #Add users by processing each line
   adduser $i developers #Iterate the following users to the developers group
   usermod -s /bin/csh $i
done

file=/home/wtrue/Lab2/staff.txt #Declare text file to a variable
write=$(cat "$file") #Read text file and make that read equal to variable write
for i in $write #Loop until it finishes processing every line iteration
do useradd $i #Add users by processing each line
   adduser $i staff #Iterate the following users to the staff group
done

file=/home/wtrue/Lab2/temp.txt #Declare text file to a variable
write=$(cat "$file") #Read text file and make that read equal to variable write
for i in $write #Loop until it finishes processing every line iteration
do useradd $i #Add users by processing each line
   adduser $i temp  #Iterate the following users to the temp group
   
done


