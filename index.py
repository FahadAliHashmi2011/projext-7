num=int(input("enter a number :"))
rev= 0
while num!=0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print("reversed number:",rev)




def calculate_change(total_amount, paid_amount):
    if paid_amount < total_amount:
        print("The amount paid is not enough!")
        return

    change = paid_amount - total_amount
    print(f"\nTotal Amount: ${total_amount:.2f}")
    print(f"Paid Amount:  ${paid_amount:.2f}")
    print(f"Change:       ${change:.2f}")

  
    denominations = [100, 50, 20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]
    change_breakdown = {}

    remaining = round(change, 2)
    for denom in denominations:
        count = int(remaining // denom)
        if count > 0:
            change_breakdown[denom] = count
            remaining = round(remaining - (denom * count), 2)

    print("\nChange Breakdown:")
    for denom, count in change_breakdown.items():
        if denom >= 1:
            print(f"${int(denom)} bills: {count}")
        else:
            print(f"{int(denom * 100)}¢ coins: {count}")


try:
    total = float(input("Enter total amount: $"))
    paid = float(input("Enter amount paid: $"))
    calculate_change(total, paid)
except ValueError:
    print("Please enter valid numbers.")