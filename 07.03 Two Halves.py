string = input("Enter a string: ")
mid = int((len(string)+1)/2)
first = string[:mid]
second = string[mid:]
print(second,first)
