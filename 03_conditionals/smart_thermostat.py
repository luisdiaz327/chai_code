
device_status = "active"
temperature = 38

if device_status == "active":
    if temperature > 35:
        print("Warning: High temperature detected!")
    else:
        print("Device is operating within normal temperature range.")
else:
    print("Device is inactive.")
