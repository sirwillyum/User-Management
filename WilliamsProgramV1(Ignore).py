"""This script takes 2 text files assuming they have names, and combines them into 1 output of all usernames"""

import re #enable use of python's regex module
from random import * #This is python's random generator

user = open("UserNamesLvl1.txt", "r") #Reading the usernames from the given text file.
user1 = open("UserNamesLvl2.txt", "r")
users = open("usernames.txt", "w") #This is the output file which will overwritten every time the script is ran.
usernames = [user, user1] #Adding both username files into a list.

namelist = [] #Creates an empty list for employee names.
for i in range(len(usernames)): #Iterate by length of usernames list.
    f = usernames[i].readline() #Reads the first line of the name list.
    while f: #While the input line exists.
        namelist.append(f) #Adds the input line to namelist.
        f = usernames[i].readline() #Reads in the next line of the list.
r1 = [*range(1000,len(namelist)+1000,1)] #Creates a list of integers from 1000 to 1000 + the # of names.

for i in range(len(namelist)):  #For loop will iterate based on the length of namelist.
    g = randrange(0, len(r1), 1) #Finds random index between 0-# of names yet to be processed.
    r = r1[g] #Grabs value in r1 corresponding to the value index of g.
    r1.remove(r1[g]) #Removes the already used value from the list of values.
    name = namelist[i].split()#We are telling python to split the first and last names as strings.
    fn = name[0]            #fn is the variable for the first name or the string in position 0.
    ln = name[1]            #ln is the variable for the last name or the string in position 0.
    done = "".join(str(fn[0]) + str(ln) + str(r)) #the regex join function brings
    print(done)
    users.write(done)
    users.write("\n")






