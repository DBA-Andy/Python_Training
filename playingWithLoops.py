import time
counter = 0
start_time = time.time()
while counter < 1000000000:
    print ("The wretched counter is: ", counter)
    counter = counter + 5
print ("The elapsed time to count to 1000000000 is: ", time.time() - start_time)
	
start_time = time.time()
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for letter in alphabet:
    print (letter.lower())
print ("the elapsed time to go through the alphabet is: ", time.time() - start_time)