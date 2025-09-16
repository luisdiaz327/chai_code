
essential_spices = {"cardamon", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices

print(f"all:  {all_spices}")

common_spices = essential_spices & optional_spices
print(f"common : {common_spices}")

only_in_essential = essential_spices - optional_spices
print(f"only in essential : {only_in_essential}")

print(f"is 'cloves' in essential {"cloves" in essential_spices}")
print(f"is 'cloves' in oprional {"cloves" in optional_spices}")



