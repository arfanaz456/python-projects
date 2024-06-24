menu = {
    "Pizza" : 200,
    "Biryani": 150,
    "Pulao" : 120,
    "Fries" : 100,
    "Tea" : 100,
    "Pasta" : 120,
    "Coffe" : 150,
    "Burger" : 120

}
#print(menu)
#Greeting
print("Welcome to our Resturant")
print("Pizza : Rs200\nBiryani : Rs150\nPulao : Rs120\nFries : Rs100\nTea : Rs100\nPasta : Rs120\nCoffe : Rs150\nBurge : Rs120")
order_total=0
item_1 = input("Enter the name of item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else: 
    print(f"order item {item_1} is not available yet")
another_order = input("Do you want to add another item? (Yes/No) ")
if another_order == "Yes":
    item_2=input("Enter the name of second order: ")
    if item_2 in menu:
        order_total += menu[item_2]
    else:
         print(f"order item {item_2} is not available yet")
print(f"The total amount of item to pay is {order_total}")


