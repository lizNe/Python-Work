#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#


def main():  
    # Open a file for writing and create it if it doesn't exist
    # Writing info to textfile
    # w - write access to the file. + python should create the file if it doesnt exist
    # myfile = open("textfile.txt", "w+") 
    
    # Open the file for appending text to the end
    # a - append data to the file so adding
    # myfile = open("textfile.txt", "a+") 
    

    # write some lines of data to the file
    # for i in range(10):
    #     myfile.write("This is some new text\n")
    
    # close the file when done
    # myfile.close()

    
    # Open the file back up and read the contents
    myfile = open("textfile.txt", "r")
    if myfile.mode == 'r': #if file has been correctly opened
        # contents = myfile.read() 
        # print(contents)
        fl = myfile.readlines(100) # if you enter a parameter it limits number of bytes contained in the textfile
        for x in fl:
            print(x)
    
if __name__ == "__main__":
    main()
