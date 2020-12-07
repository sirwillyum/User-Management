
from random import *



def numList(m):
    """
    This function creates a new text file containing a unique integer on each line. Each integer has an equal number of digits
    (1 is represented as 001). There can be no more than 9,999,999 values. Should a value greater than 9,999,999 be entered,
    the user will encounter significant errors.
    
    INPUTS:
    m: The minimum number of unique integers desired. The program will create the as many unique integers as there exist number
    combinations with the minimum number of digits to have at least m values. For example: if m=50, there will be 100 numbers,
    all 2 digits (from 00 to 99).
    
    OUTPUTS:
    Creates or overwrites the text file "numlist.txt"
    """
    
    for i in range(2, 7): #Scans powers of 10 from 2 to 6.
        j = 10**i         #Creates a variable equal to 10 to the power of the current for loop index.
        if (m <= j):      #Checks if the function input m is less than or equal to j.
            m = i         #If true, sets m equal to log_10(j), or the first number x such that 10^x is greater than the
                          #    original m.
            break         #If a sufficient power of 10 has been found, exit the for loop.
    
    nums = ""                    #Creates an empty string.
    for i in range(0, 10**m, 1): #Loops over all integers between 0 and 10^m.
        stri = str(i)            #Creates a temporary string equal to the string form of the loop index integer.
        
        if (len(stri) < m):                    #Checks if the length of the temporary string is less than m.
            for i in range(0, m-len(stri), 1): #If true, loops over the difference between the length of the string and m.
                stri = "0" + stri              #For every loop, add a 0 at the beginning of the string.
        
        nums = nums + stri     #Adds the temporary string to the empty string nums.
        if (i < ((10**m)-1)):  #Checks if the loop index has not reached the end.
            nums = nums + "\n" #If true, add a new line.
    
    f1 = open('numlist.txt', 'w').close() #Clear the file numlist.txt (potentially redundant).
    with open('numlist.txt', 'w') as f2:  #Temporarily opens numlist.txt.
        f2.write(nums)                    #Writes the string of values into numlist.txt.





def increase(n, m=0):
    """
    This function increases the number of integers in numlist.txt to the next power of 10 up.
    
    INPUTS:
    n: This input must be equal to the number of values previously created in numlist.txt. For example, if numlist.txt
    previously was intended to contain up to 100 values, n must be input as 100.
    
    m: This input defaults to 10*n, but may be reassigned to expand numlist.txt further.
    
    OUTPUTS:
    Modifies the file numlist.txt.
    """
    
    if (m==0):            #Determines if the value of m was specified in the function call.
        m = 10*n          #If m was not specified when the function was called, sets it equal to 10*n.
    for i in range(2, 7): #Scans powers of 10 from 2 to 6.
        j = 10**i         #Defines a variable as 10 to the power of i.
        if (m <= j):      #Checks if m is less than or equal to 10 to the power of i.
            m = i         #If so, set m to i.
            break         #Then exit the for loop.
    
    nums = "\n"           #Start a string with a new line to add to the old file.
    
    for i in range(10**(m-1), 10**m, 1):       #Loops from the first unused value to the new maximum.
        stri = str(i)                          #Creates a temporary string equal to the string form of the loop index integer.
        
        if (len(stri) < m):                    #Checks if the length of the temporary string is less than m.
            for i in range(0, m-len(stri), 1): #If true, loops over the difference between the length of the string and m.
                stri = "0" + stri              #For every loop, add a 0 at the beginning of the string.
        
        nums = nums + stri                     #Adds the temporary string to the empty string nums.
        if (i < ((10**m)-1)):                  #Checks if the loop index has not reached the end.
            nums = nums + "\n"                 #If true, add a new line.
    
    with open('numlist.txt', 'a+') as f:       #Opens numlist.txt temporarily in append mode.
        f.write(nums)                          #Writes the new values to the end of numlist.txt.





def createUsers(filelist, n):
    """
    This function creates a text file of usernames. All usernames are equal to someone's input first initial followed by the
    first word of their last name and a unique integer. The number of digits in the integer is equal to the minimum number of
    digits needed to have a unique integer for each username at the time of creation.
    
    INPUTS:
    filelist: A list of variables addressing open files that contain a full name on each line.
    
    n:        An integer corresponding to the maximum number of usernames the creator ever expects to have.
    
    OUTPUTS:
    Creates a text file containing unique usernames. Also calls numList().
    """
    
    users = open("usernames.txt", "w").close() #Clears the text file usernames.txt (potentially redundant).
    users = open("usernames.txt", "w") #Opens usernames.txt in write mode.
    
    namelist = []                      #Creates an empty list for names.
    for i in range(len(filelist)):     #Loops over the number of files input.
        f = filelist[i].readline()     #Reads the first line of the name list in the indexed file.
        while f:                       #Loop until the input line does not exist.
            namelist.append(f)         #Adds the input line to namelist.
            f = filelist[i].readline() #Reads in the next line of the list.
    
    numList(n) #Creates a text file with as many unique integers as the first power of 10 greater than the maximum number of
                   #desired names.
    
    with open("numlist.txt", "r") as numlist: #Opens numlist.txt temporarily in read mode.
        lines = numlist.readlines()           #Creates a list of every line in numlist.txt.
    
    for i in range(len(namelist)):      #Loops over the number of names.
        g = randrange(0, len(lines), 1) #Finds a random number between 0 and the number of possible random numbers.
        r = lines[g]                    #Creates a variable equal to a random line read from numlist.txt.
        del lines[g]                    #Deletes the now used line from the list read in from numlist.txt.
        
        with open("numlist.txt", "w") as numlist: #Opens numlist.txt temporarily in write mode.
            for line in lines:                    #Iterates over the lines list read in from numlist.txt.
                numlist.write(line)               #Writes numlist.txt over with each line remaining in lines.
        
        name = namelist[i].split()                    #we are telling python to split the first and last names as strings
        fn = name[0]                                  #fn is the variable for the first name or the string in position 0
        ln = name[1]                                  #ln is the variable for the last name or the string in position 0
        done = "".join(str(fn[0]) + str(ln) + str(r)) #the regex join function takes the content we've split and rebuilds o
        print(done)                                   #Prints the newly created username.
        users.write(done)                             #Writes the newly created username into usernames.txt.






def hire(hirelist, n):
    """
    This function adds usernames to a previously created text file of usernames, usernames.txt.
    
    INPUTS:
    hirelist: A list of strings representing full names.
    
    n:        An integer equal to the maximum number of elements contained in the previously created numlists.txt file.
    
    OUTPUTS:
    Modifies the text file usernames.txt. Also modifies numlist.txt. May call increase().
    """
    
    with open("numlist.txt", "r") as numlist: #Opens numlist.txt temporarily in read mode.
        lines = numlist.readlines()           #Creates a list containing every line in numlist.txt.
        
    with open("usernames.txt", "r") as users: #Opens usernames.txt temporarily in read mode.
        userlines = users.readlines()         #Creates a list containing every line in usernames.txt.
    
    if (len(hirelist) > len(lines)):              #Checks if the hirelist is longer than all remaining unique integers.
        increase(n)                               #If so, call increase() with the input being the previous maximum number of
                                                      #unique integers.
        with open("numlist.txt", "r") as numlist: #Opens numlist.txt temporarily in read mode.
            lines = numlist.readlines()           #Recreates a list containing every line in numlist.txt.
    
    for i in range(len(hirelist)):      #Loops over the number of names.
        g = randrange(0, len(lines), 1) #Finds a random number between 0 and the number of possible random numbers.
        r = lines[g]                    #Creates a variable equal to a random line read from numlist.txt.
        del lines[g]                    #Deletes the now used line from the list read in from numlist.txt.
        
        with open("numlist.txt", "w") as numlist: #Opens numlist.txt temporarily in write mode.
            for line in lines:                    #Iterates over the lines list read in from numlist.txt
                numlist.write(line)               #Writes numlist.txt over with each line remaining in lines.
        
        name = hirelist[i].split()                    #we are telling python to split the first and last names as strings
        fn = name[0]                                  #fn is the variable for the first name or the string in position 0
        ln = name[1]                                  #ln is the variable for the last name or the string in position 0
        done = "".join(str(fn[0]) + str(ln) + str(r)) #the regex join function takes the content we've split and rebuilds o
        print(done)                                   #Prints the newly created username.
        userlines.append(done)                 #Adds the newly created username to the list of lines read in from
                                                          #usernames.txt.
        
    with open("usernames.txt", "w") as users: #Opens usernames.txt temporarily in write mode.
        for line in userlines:                #Iterates over the lines list read in from usernames.txt.
            users.write(line)                 #Writes usernames.txt over with each line remaining in userlines.





user = open("UserNamesLvl1.txt","r") #reading the usernames from the given text file
user1 = open("UserNamesLvl2.txt","r")

filelist = [user, user1]

createUsers(filelist, 1000)


print(createUsers.__doc__)


#hirelist = ["Greg Gregson"]

#hire(hirelist, 100)







