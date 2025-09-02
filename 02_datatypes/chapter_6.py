
chai_type = "ginger chai"
customer_name = "Amit"

print(f"Order for {customer_name}: {chai_type} please!")

chai_description = "Aromatic and Chai"
print(f"first word: {chai_description[0:8]}") 
print(f"first word: {chai_description[0:8:2]}")
print(f"first word: {chai_description[:8]}")
print(f"first word: {chai_description[9:]}")
print(f"first word: {chai_description[::-1]}")

lable_text = 'chai spècial'
print(f"nonencoded_text: {lable_text}")

ecoded_text = lable_text.encode('utf-8') 
print(f"encoded_text: {ecoded_text}")

decoded_text = ecoded_text.decode('utf-8')
print(f"decoded_text: {decoded_text}")






