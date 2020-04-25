#a list comprehension function the prints a range of n odd numbers
def odd_numbers(n):
    return[x for x in range(n+1) if x % 2 != 0]

print(odd_numbers(5))
print(odd_numbers(10))
print(odd_numbers(11))
print(odd_numbers(1))
print(odd_numbers(-1))