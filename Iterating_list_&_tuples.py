# #Iterating over list using for animals
# animals = ["Lion", "Zebra","Dolphin", "Monkey"]
# chars = 0
# #iterating over lists
# for animal in animals:

#     #gets each animals length and adds it to the total number of characters
#     chars = chars + len(animals)

# #prints the total and averge
# print("Total characters average length: {}, Average length: {}".format(chars, chars/len(animals)))


#using the enumerate fuction 
winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
    print("{}, {}".format(index + 1, person))



