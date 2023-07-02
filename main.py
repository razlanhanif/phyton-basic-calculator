print("Basic Addition Calculator")

n1 = input("Enter your number:")
n2 = input("Enter another number:")
o1 = input("Choose a operation! (add, minus, mul): ")
addition = float(n1) + float(n2)
subs = float(n1) - float(n2)
multi = float(n1) * float(n2)

if o1 == "add":
    print(addition)
if o1 == "minus":
    print(subs)
if o1 == "mul":
    print(multi)
