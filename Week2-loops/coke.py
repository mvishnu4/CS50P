#prompting user amount of coke
amountDue = 50
print("Amount Due: " + str(amountDue))
#calculating the inserted amount and residual amount
while (amountDue != 0):
    insertedAmount = int(input("Inserted Coin: "))
    if insertedAmount == 25 or insertedAmount == 10 or insertedAmount == 5:
        amountDue -= insertedAmount
        if amountDue > 0:
            print("Amount Due: " + str(amountDue))
        elif amountDue < 0:
            amountDue = -(amountDue)
            break
    else:
        print("Amount Due: " + str(amountDue))

print("Change Owed: " + str(amountDue))