class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
    
    def eat(self):
        print(f"{self.name} is eating...")
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
    
    def play(self):
        if self.energy <= 0:
            print(f"{self.name} is too tired to play!")
            return
        
        print(f"{self.name} is playing...")
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 3)
        self.hunger = min(10, self.hunger + 1)
    
    def sleep(self):
        print(f"{self.name} is sleeping...")
        self.energy = min(10, self.energy + 5)
    
    def train(self, trick):
        if self.energy >= 2:
            self.tricks.append(trick.lower())
            self.energy -= 2
            print(f"{self.name} learned '{trick}'!")
        else:
            print(f"{self.name} is too tired to train!")
    
    def get_status(self):
        print(f"\n{self.name}'s current status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        print(f"Tricks: {self.tricks}")
    
    def show_tricks(self):
        if not self.tricks:
            print(f"{self.name} doesn't know any tricks yet!")
        else:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")