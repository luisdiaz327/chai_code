
is_boiling = True
stri_count = 5

total_actions = stri_count + is_boiling #upcasting boolean to integer
print(f"total_actions: {total_actions}")


milk_present = 0 
print(f"milk_present: {bool(milk_present)}") #downcasting integer to boolean


water_hot = True
tea_added = True

can_server = water_hot and tea_added #logical and operation
print(f"can_server: {can_server}")



