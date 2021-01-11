# put your code here.
#Write a program, wordcount.py, that opens a file and counts how many times each space-separated word occurs in that file. Your program should then print those counts to the screen.

# open the file using open function 
def word_count(filename):
    poem_file = open(filename)
    
    word_counts = {}
    for line in poem_file:
        line = line.rstrip()
        words = line.split(" ")
        for idx, word in enumerate(words):
            #print( words[idx])
            word_counts[words[idx]] = word_counts.get(words[idx], 0) + 1

    return word_counts
    # write a function that counts each space-sewp word
# make empty dictionary
# use for loop with dict.get with counter
# returns print letter count

word_count("test.txt")
