
masala_spices = ("cumin", "coriander", "turmeric")

(spice1, spice2, spice3) = masala_spices

print(f"First three spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cadramon_ratio = 2, 1
print(f"Ginger to cardamom ratio: {ginger_ratio}:{cadramon_ratio}")

cadramon_ratio, ginger_ratio = ginger_ratio, cadramon_ratio
print(f"Cardamom to ginger ratio: {cadramon_ratio}:{ginger_ratio}")

#membership test

print(f"is ginger in masala spices? {'ginger' in masala_spices}")
print(f"is cumin in masala spices? {'cumin' in masala_spices}")

