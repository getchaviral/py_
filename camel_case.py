s = input("Enter a sentence: ")
words = s.split()

camel_case = words[0].lower()

for word in words[1:]:
    camel_case += word.capitalize()

print("CamelCase:", camel_case)
