Canara_bankstatement = {"name": "nithish", "bank": "canara", "accno": 12345, "phone_no": 98776544444}

# Remove the 'phone_no' key from the dictionary
if "phone_no" in Canara_bankstatement:
    Canara_bankstatement.pop("phone_no")
    print("Removed 'phone_no' from Canara_bankstatement")
else:
    print("'phone_no' not found in Canara_bankstatement")

# Print the updated dictionary
print("Updated Canara_bankstatement:", Canara_bankstatement)

Canara_bankstatement.update({"test":"demo"})
print(Canara_bankstatement)