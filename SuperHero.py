# Base class
class Superhero:
    def __init__(self, name, power, hometown, nemesis):
        self.name = name
        self.power = power
        self.hometown = hometown
        self.nemesis = nemesis
    
    def introduce(self):
        return f"I am {self.name}, defender of {self.hometown}!"

    def use_power(self):
        return f"{self.name} uses their {self.power} to fight evil!"

    def confront_nemesis(self):
        return f"{self.name} faces their nemesis: {self.nemesis}!"

# Derived class for a specific type of superhero
class TechHero(Superhero):
    def __init__(self, name, power, hometown, nemesis, tech_gadget):
        super().__init__(name, power, hometown, nemesis)
        self.__tech_gadget = tech_gadget  # Encapsulated attribute

    def reveal_gadget(self):
        return f"{self.name} reveals their advanced tech: {self.__tech_gadget}!"

    def use_power(self):
        # Polymorphism: Override the use_power method for a tech hero
        return f"{self.name} activates {self.power} with their {self.__tech_gadget}!"

# Another derived class for an elemental superhero
class ElementalHero(Superhero):
    def __init__(self, name, power, hometown, nemesis, element):
        super().__init__(name, power, hometown, nemesis)
        self.element = element

    def use_power(self):
        # Polymorphism: Override the use_power method for an elemental hero
        return f"{self.name} summons the power of {self.element} to unleash {self.power}!"

# Instantiate the base and derived classes
hero1 = Superhero("Shadow Knight", "stealth and combat skills", "Gotham", "Darklord")
tech_hero = TechHero("Circuit Breaker", "electromagnetic control", "Neo Tokyo", "Cyber Phantom", "Nano Blade")
elemental_hero = ElementalHero("Aqua Storm", "tsunami generation", "Atlantis", "Inferno", "water")

# Test methods
print(hero1.introduce())
print(hero1.use_power())
print(hero1.confront_nemesis())
print()
print(tech_hero.introduce())
print(tech_hero.use_power())
print(tech_hero.reveal_gadget())
print()
print(elemental_hero.introduce())
print(elemental_hero.use_power())
print(elemental_hero.confront_nemesis())