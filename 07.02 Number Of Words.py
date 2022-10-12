s = input("Enter a string: ")

count = 0
if len(s) > 0:
    count = 1
    for ch in s:
        if ch == ' ':
            count += 1

print(count, "words")