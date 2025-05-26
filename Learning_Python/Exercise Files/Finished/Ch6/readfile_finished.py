#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#

    
# Open the file and read the contents
sample_file = open("textfile.txt","r")
if sample_file.mode == 'r': # check to make sure that the file was opened
    # use the read() function to read the entire file
    # contents = sample_file.read()
    # print(contents)
    
    file_lines = sample_file.readlines() # readlines reads the individual lines into a list
    for line in file_lines:
        print (line)
