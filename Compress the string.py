s = input("Enter string: ")

compressed = ""
count = 1

for i in range(len(s)):
    if i + 1 < len(s) and s[i] == s[i + 1]:
        count += 1
    else:
        compressed += s[i] + str(count)
        count = 1

print("Compressed string:", compressed)
