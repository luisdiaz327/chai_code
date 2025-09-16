
chai_order = dict(type="masala chai", size="large", sugar=2)

print(f"chai order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"recipe base: {chai_recipe}")

print(f"recipe base: {chai_recipe["base"]}")

del chai_recipe["liquid"]
print(f"recipe base: {chai_recipe}")

print(f"is sugar in the order? {'sugar' in chai_order}")

chai_order = {
    "type": "ginger chai",
    "size": "medium",
    "sugar": 1
}

print(f"order details keys: {chai_order.keys()}")
print(f"order details values: {chai_order.values()}")
print(f"order details items: {chai_order.items()}")

last_item = chai_order.popitem()
print(f"last item remove {last_item}")

essential_spices = {
    "cardamon": "crushed", 
    "ginger": "sliced"
    }

print(f"chai recipe: {chai_recipe}")

chai_recipe.update(essential_spices)

print(f"update recipe: {chai_recipe}")


chai_size = chai_order["size"]
print(f"chai size is: {chai_size}")

note = chai_order.get("note", "no note")
print(f"chai size is: {note}")

note = chai_order.get("type", "no type")
print(f"chai size is: {note}")


