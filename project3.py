# cafe management system
# aa
menu = {
    "momos":30,
    "burger":25,
    "pasta":40,
    "shake":35,
    "samosa":15
}
order ={}
print("*****WELCOME TO OUR PYTHON CAFE******")
print("Here is menu\nmomos: 30\nburger: 25\npasta: 40\nshake: 35\nsamosa: 15")
order_total = 0
while True:
    item = input("enter the item you want to order ").lower()
    try:
     quantity = int(input("enter the quantity of order " ))
    except Exception as e:
        print("invalid option")
        continue
    if item in menu:
        order[item] = order.get(item, 0) + quantity
        order_total += menu[item]*quantity
        print(f"your item {item} added successfully")
        ask = input("do you want to add more something(yes/no) ").lower()
        if(ask=="no"):
            break
        
    else:
        print("please add item which is available in menu")
    

# print(f"the total amount of order is to pay {order_total}")


print("========BIL==========")
for item, quantity in order.items():
    amount = menu[item] * quantity
    print(f"{item} x {quantity} = ₹{amount}")
print("========================")
print(f"total = ₹{order_total}")
