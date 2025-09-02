class Chai:
    def __init__(self, sweetness, milk_level):
        self.sweetness = sweetness
        self.milk_level = milk_level

    def sip(self):
        print("Sipping the chai...")

    def add_sugar(self, amount):
        print("adding sugar...")

my_chai = Chai(sweetness="medium", milk_level="high")

my_chai.add_sugar(2)
my_chai.sip()