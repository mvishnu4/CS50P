import validators
email = input("What's your email address? ")

end = email.split(".")
start = email.split("@")
if len(end) == 2 and len(start) == 2 and end[1] in ["com" , "edu", "org", "net", "uk", "us"]:
    mid1 = start[1].split(".")
    mid2 = end[0].split("@")
    #print(mid1, mid2, end = " ")
    if mid1[0] == mid2[1] and start[0] == mid2[0] and end[1] == mid1[1]:
        print("Valid")
    else:
        print("Invalid")
elif len(end) == 3:
    mid1 = start[1].split(".")
    mid2 = end[0].split("@")
    if mid1[0] + mid1[1] == mid2[1] + end[1] and start[0] == mid2[0] and end[2] == mid1[2]:
        print("Valid")
    else:
        print("Invalid")
else:
    print("Invalid")

