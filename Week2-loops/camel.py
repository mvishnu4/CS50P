#prompting user for camelCased word
word = input("camelCase: ")
snake_case = ""
#converting Uppercase letter to _ followed by corresponding lowercase letter as in snake_case representation
for i in range(len(word)):
    if word[i].islower():
        snake_case += word[i]
    elif word[i].isupper():
        snake_case += ("_" + word[i].lower())

print("snake_case: " + snake_case)