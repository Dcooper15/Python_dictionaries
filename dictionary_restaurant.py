menu = {
    "Brunch": {
        "Steak and Eggs": 16.99,
        "Three Egg Breakfast": 8.99,
        "Egg Benedict": 11.99,
        "Biscuit and Gravy": 7.99,
        "Chicken Fingers": 10.99,
        "Chicken Wrap": 8.99,
        "Steak Salad": 1.99
    },
    "Drinks": {
        "Soft Drink": 1.99,
        "Coffee": 1.99,
        "Orange Juice": 0.99,
        "Milk": 0.55,
        "Water": 0.00
    }
}

# changing the value of "Steak Salad" from 1.99 to 15.99
menu["Brunch"]["Steak Salad"] = 15.99

menu["Specials"] = {
    "Soup of the Day": 8.99,
    "Catch of the Day": 14.99,
    "Chef Specail": 15.99 
}
menu["Brunch"]["Three Egg Breakfast - Without Bacon"] = 8.99
menu["Brunch"]["Three Egg Breakfast - With Bacon"] = 9.99
del menu["Brunch"]["Three Egg Breakfast"]
#print(menu)

#table-1 Guest1: (Egg Benedict,Coffee) Guest2: (Biscuit and Gravy, Coffee) Guest3: (Steak and Eggs, Soft Drink)
guest1_food = menu["Brunch"]["Egg Benedict"]
guest1_drink = menu["Drinks"]["Coffee"]
guest2_food = menu["Brunch"]["Biscuit and Gravy"]
guest2_drink = menu["Drinks"]["Coffee"]
guest3_food = menu["Brunch"]["Steak and Eggs"]
guest3_drink = menu["Drinks"]["Soft Drink"]

#Calculating the total of the price of the bill, the taxes and total.
price = (guest1_food + guest1_drink + guest2_food + guest2_drink + guest3_food + guest3_drink)
taxes = (price * .07)
total = (price + taxes)

#tip calculations
tip_high = (price * .25)
tip_mid = (price * .20)
tip_low = (price * .15)



#terminal receipt
print("Eggs Benedict" + "            $" + str(guest1_food))
print("Coffee" + "                   $" + str(guest1_drink))
print("Biscuit and Gravy" + "        $" + str(guest2_food))
print("Coffee" + "                   $" + str(guest2_drink)) 
print("Steak and Eggs" + "           $" + str(guest3_food))
print("Soft Drink" + "               $" + str(guest3_drink)) 
print("                                                    ")
print("                    Price:   $" + str(price))
print("                    Taxes:   $" + str(round(taxes, 2)))
print("                    Total:   $" + str(round(total, 2)))
print("**Suggested Tip**")
print("Tip 25%:   " + str(round(tip_high,2)))
print("Tip 20%:   " + str(round(tip_mid,2)))
print("Tip 15%:   " + str(round(tip_low,2)))