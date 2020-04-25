#The get_word function returns the {n}th word from a passed sentence
#Example get_word("This is a lesson about lists", 4) should return "lesson"

def get_word(sentence, n):
    #Only proceed if n is positive
    if n > 0:
        words = sentence.split(" ")
        #Only proceed if n is not more than the number of words
        if n <= len(words):
            return(words[n-1])
        return("")

print(get_word("This is a lesson about lists", 4)) #lesson
print(get_word("This is a lesson about lists", -4)) #Nothing
print(get_word("Now we are cooking!", 1)) #Now
print(get_word("Now", 5)) #Nothing
