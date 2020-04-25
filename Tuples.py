#example of Tuples
fullname = ('Grace','M','Hooper')

#a function to convert seconds to hrs, min * remaining seconds
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds -hours * 3600) //60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

result = convert_seconds(5000)
print(type(result))
print(result)
print("")

#Unpacking tuples
hours, minutes, seconds = result
print(hours, minutes, seconds)

print("")

#Unpacking tuples
hours, minutes, seconds = convert_seconds(1000)
print(hours, minutes, seconds)

#Create a tuple with a Filename and it's size
#Store the name and email address of a person
#Date & time and a general health of a system at any point in time 
