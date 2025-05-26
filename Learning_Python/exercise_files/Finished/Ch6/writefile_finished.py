# LinkedIn Learning Python course by Joe Marini
# write files using the built-in Python file methods
#


# Open a file for writing and create it if it doesn't exist
sample_file = open("textfile.txt","w+")
sample_file.write("This is some sample text in our sample file.")
sample_file.close()

# Open the file for appending text to the end
sample_file = open("textfile.txt","a+")

# write some lines of data to the file
sample_file.write("This is more sample text in our sample file.")

# close the file when done
sample_file.close()
