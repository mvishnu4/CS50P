sentance = input("Input: ")
substitute = ""
for i in range(len(sentance)):
    if (sentance[i] != 'a' and sentance[i] != 'e' and sentance[i] != 'i' and sentance[i] != 'o' and sentance[i] != 'u' and
        sentance[i] != 'A' and sentance[i] != 'E' and sentance[i] != 'I' and sentance[i] != 'O' and sentance[i] != 'U'):
        substitute += sentance[i]

print("Output: " + substitute)