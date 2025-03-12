import emoji
query = input("Input: ")
arr = []
for i in range(len(query)):
    if query[i] == ":":
        arr.append(i)
print(arr)
start = ""
first = ""
secound = ""
third = ""
end = ""
if len(arr) == 2:
    if arr[0] == 0 and arr[1] == len(query) - 1:
        if query == ":thumbsup:":
            query = ":thumbs_up:"
        print("Output: " + emoji.emojize(query))
    elif arr[0] == 0 and arr[1] != len(query) - 1:
        start = query[arr[0]:arr[1]]
        end = query[arr[1]:len(query)]
        print("Output: " + emoji.emojize(start) + end)
    elif arr[0] != 0 and arr[1] == len(query) - 1:
        start = query[0:arr[0]]
        end = query[arr[0]:len(query)]
        if end == ":earth_asia:":
            end = "🌏"
            print("Output: " + start + end)
    else:
        start = query[0:arr[0]]
        first = query[arr[0]:arr[1]]
        end = query[arr[1]:len(query)]
else:
    print("output: " + emoji.emojize(query))