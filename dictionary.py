meal = {
    "drink": "water",
    "appetizer": "chips",
    "entree": "salmon",
    "dessert": "key lime pie",
    }

#print("This evening I will have a %s and %s for dinner" % (meal["drink"], meal["entree"]))

if "dessert" in meal:
    meal["dessert"] = "cake"
    print("Of couse! Dylan had %s for dessert.") % meal["dessert"]
else:
    meal["dessert"] = "key lime pie"
    print(meal)