#x = ["Now","we", "are", "cooking!"]
#print(type(x))
#print(x)
#print(len(x))
#print("are" in x)
#print("Today" in x)
#print(x[0])
#print(x[3])
#print(x[1:3])
#print(x[:2])
#print(x[2:])

# #fruit list 
# fruits = ["Pineapple","Banana", "Apple", "Melon"]

# #using append to add an item to the end of the array list
# fruits.append("Kiwi")


# #using insert to add an item in a particular position in an array list
# fruits.insert(0,"Orange")
# #using insert to add an item, higher than the cuurent length in an array list
# fruits.insert(25,"Peach") #Result ['Orange', 'Pineapple', 'Banana', 'Apple', 'Melon', 'Kiwi', 'Peach']

# #using remove to delete an item from the list
# fruits.remove('Melon')

# #using pop to delete an item from the list by passing an index
# fruits.pop(3)

# #changing an item in the list
# fruits[2] = "Strawberry"

# print(fruits)


# #Creates a list of multiples of 7 
# multiples = []
# for x in range(1,11):
#     multiples.append(x*7)

#     print(multiples)

#using list comprehension to print multiples
# multiples = [x*7 for x in range(1,11)]
# print(multiples)

#counts the total length of characters for each language
languages = ["Python", "Perl", "Ruby," "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths)

#print statement to create a break
print("")

#prints out multiples of 3 from 0 to 101
z = [x for x in range(0,101) if x % 3 == 0]
print(z)









