#Pizza order program 

print("Welcome to Python Pizza Derivaries")
size = input("What size pizza do you want? S, M, or L ") 
pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill +=15
    if pepperoni == "Y":
        bill +=2
    else:
        print(f"Your bill is {bill}")
    if extra_cheese == "Y":
        bill +=1
        print(f"Your total bill is {bill}")
    else:
        print(f"your total bill is {bill}")
if size == "M":
    bill +=20
    if pepperoni == "Y":
        bill +=3
    else:
        print(f"Your bill is {bill}")
    if extra_cheese == "Y":
        bill +=1
        print(f"Your total bill is {bill}")
    else:
        print(f"your total bill is {bill}")

if size == "L":
    bill +=25
    if pepperoni == "Y":
        bill +=3
    else:
        print(f"Your bill is {bill}")
    if extra_cheese == "Y":
        bill +=1
        print(f"Your total bill is {bill}")
    else:
        print(f"your total bill is {bill}")


else:
    print("Order no processed")