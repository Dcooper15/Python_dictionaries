phonebook_dict = {
    "Alice": "703-493-1834",
    "Bob": "857-384-1234",
    "Elizabeth": "484-584-2923", 
}

print(phonebook_dict["Elizabeth"])

# adding "Kareen to the dictionary"
if "Kareem" in phonebook_dict:
    print("Kareem is already in the dictionary")
else:
    phonebook_dict["Kareen"] = "567-987-2222"

# Changing Bob's phone number
phonebook_dict["Bob"] = "527-555-2321"

# removing Alice from the dictionary
del phonebook_dict ["Alice"]


print(phonebook_dict)


