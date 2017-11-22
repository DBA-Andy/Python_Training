import time
import string
counter = 0
limit = 1000000
start_time = time.time()
while counter < limit:
    print ("The wretched counter is: ", counter)
    counter = counter + 5
print ("The elapsed time to count to", limit, "is: ", time.time() - start_time)
	
start_time = time.time()
alphabet = ['ALPHA','BRAVO','CHARLIE','DELTA','ECHO','FOXTROT','GOLF','HOTEL','INDIA','JULIET','KILO','LIMA','MIKE','NOVEMBER','OSCAR','PAPA','QUEBEC','ROMEO','SIERRA','TANGO','UNIFORM','VICTOR','WHISKEY','XRAY','YANKEE','ZULU']
for letter in alphabet:
    print (letter[0].upper() + letter[1:].lower())
print ("the elapsed time to go through the alphabet is: ", time.time() - start_time)