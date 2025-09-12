
ingredients = ["water", "milk", "black tea"]
print(ingredients)

ingredients.append("sugar")
print(ingredients)

ingredients.remove("water")
print(ingredients)

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"Chai ingredients: {chai_ingredients}")

chai_ingredients.insert(2, "black tea")
print(f"Chai ingredients: {chai_ingredients}")


last_ingredient = chai_ingredients.pop()
print(f"Chai ingredients: {chai_ingredients}")
print(f"Last ingredient: {last_ingredient}")

chai_ingredients.reverse()
print(f"Chai ingredients reverse : {chai_ingredients}")

chai_ingredients.sort()
print(f"Chai ingredients sorted : {chai_ingredients}")

print(f"is ginger in chai ingredients? {'ginger' in chai_ingredients}")
print(f"is cumin in chai ingredients? {'cumin' in chai_ingredients}")

print(f"Number of ingredients in chai: {len(chai_ingredients)}")

sugar_level = [1, 2, 3, 4, 5]
print(f"Maximum sugar level: {max(sugar_level)}")
print(f"Minimum sugar level: {min(sugar_level)}")
print(f"Sum of sugar levels: {sum(sugar_level)}")
print(f"Average sugar level: {sum(sugar_level) / len(sugar_level)}")
print(f"Sorted sugar levels: {sorted(sugar_level)}")
print(f"Reversed sugar levels: {list(reversed(sugar_level))}")
print(f"Sugar levels: {sugar_level}")


base_liquid = ["water", "milk"]
extra_flavors = ["ginger"]

full_liquid= base_liquid + extra_flavors
print(f"Full liquid ingredients: {full_liquid}")


strong_brew = ["black tea", "water"] * 3
print(f"Strong brew ingredients: {strong_brew}")


raw_data = bytearray(b"helloworld")
print(raw_data)

raw_data.replace(b"helloworld", b"goodbye")
print(raw_data)

raw_data = raw_data.replace(b"helloworld", b"goodbye")
print(raw_data)

