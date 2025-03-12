#promting user for greet and taking input
print("Greeting: ", end= "")
response = input()

if "Hello" in response:
    print("$0")
elif "Hey" in response or "How" in response or "How's" in response:
    print("$20")
elif "What's" in response:
    print("$100")