class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.disposable_cups = 9
        self.money = 550

    def run(self):
        done = False
        while not done:
            action = input("Write action (buy, fill, take, remaining, exit):")
            if action == "buy":
                CoffeeMachine.buy(self)
            elif action == "fill":
                CoffeeMachine.fill(self)
            elif action == "take":
                CoffeeMachine.take(self)
            elif action == "remaining":
                CoffeeMachine.remaining(self)
            elif action == "exit":
                done = True
            else:
                print("invalid choice")

    def remaining(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.coffee, "of coffee beans")
        print(self.disposable_cups, "of disposable cups")
        print(f"$ {self.money} of money")

    def buy(self):
        drink = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if drink == "back":
            return
        elif drink == '1':  # espresso
            if CoffeeMachine.check_supply(self, 250, 0, 16):
                self.water -= 250
                self.coffee -= 16
                self.money += 4
                self.disposable_cups -= 1
        elif drink == '2':  # latte
            if CoffeeMachine.check_supply(self, 350, 75, 20):
                self.water -= 350
                self.milk -= 75
                self.coffee -= 20
                self.money += 7
                self.disposable_cups -= 1
        elif drink == '3':  # cappuccino
            if CoffeeMachine.check_supply(self, 200, 100, 12):
                self.water -= 200
                self.milk -= 100
                self.coffee -= 12
                self.money += 6
                self.disposable_cups -= 1
        else:
            print('invalid choice')
            return CoffeeMachine.buy(self)

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk += int(input("Write how many ml of milk do you want to add:"))
        self.coffee += int(input("Write how many grams of coffee beans do you want to add:"))
        self.disposable_cups += int(input("Write how many disposable cups of coffee do you want to add:"))

    def take(self):
        print(f"I gave you $ {self.money}")
        self.money = 0

    def check_supply(self, needed_water, needed_milk, needed_coffee):
        if self.water < needed_water:
            print('Sorry, not enough water!')
            return False
        if self.milk < needed_milk:
            print('Sorry, not enough milk!')
            return False
        if self.coffee < needed_coffee:
            print('Sorry, not enough beans!')
            return False
        if self.disposable_cups < 1:
            print('Sorry, not enough cups\n')
            return False
        print('I have enough resources, making you a coffee!\n')
        return True


machine = CoffeeMachine()
machine.run()
