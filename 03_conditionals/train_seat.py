
seat_type = input("Enter seat type (sleeper/AC/general/luxury)").lower()

match seat_type:
    case "sleeper":
        print("Seat price is $150")
    case "ac":
        print("Seat price is $300")
    case "general":
        print("Seat price is $100")
    case "luxury":
        print("Seat price is $500")
    case _:
        print("Invalid seat type")
    

