#Dictionaries
# x = {}
# print(type(x))
 
file_counts = {"jpg":10, "txt":14, "csv":2, "py": 23}
print(file_counts)

#prints the stored value associated with the txt key
print(file_counts["txt"])

#T or F for keys in the file_counts dictionary
print("jpg" in file_counts)
print("html" in file_counts)

#adds a new key to the file_counts dictionary
file_counts["cfg"] = 8
print(file_counts)

# #adds a key that already exist
file_counts["csv"]= 17
print(file_counts)

#deleting a key
del file_counts["cfg"]
print(file_counts)