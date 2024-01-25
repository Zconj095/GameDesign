"""The code defines several attributes for each ability, including its name, base cost, base cooldown, maximum level, current level, cooldown timer, and methods for upgrading, calculating the current cost, current cooldown, using the ability, applying a quantum effect, and reducing the cooldown.

The code also defines a class called Player that represents a player in the game. The player has a name, resource (mana or health points), and a list of abilities. The code defines methods for adding an ability to the player, updating the abilities, and using an ability.

The code includes an example usage of the Player and Ability classes, where a player is created with one ability (a fireball) and the ability is levelled up. The code then simulates using the ability 10 times, updating the abilities and using the fireball each time."""
import random
class Ability:
    def __init__(self, name, base_cost, base_cooldown, max_level):
        self.name = name
        self.base_cost = base_cost
        self.base_cooldown = base_cooldown
        self.level = 1
        self.max_level = max_level
        self.cooldown_timer = 0

    def upgrade(self):
        if self.level < self.max_level:
            self.level += 1
            print(f"{self.name} upgraded to Level {self.level}.")

    def current_cost(self):
        return self.base_cost / self.level  # Reduced cost with level

    def current_cooldown(self):
        return max(1, self.base_cooldown - self.level)  # Reduced cooldown with level

    def use(self, player):
        cost = self.current_cost()
        if player.resource >= cost and self.cooldown_timer == 0:
            self.apply_quantum_effect()
            player.resource -= cost
            self.cooldown_timer = self.current_cooldown()
            print(f"{player.name} used {self.name}!")
        else:
            print(f"{self.name} is not ready or insufficient resources.")

    def apply_quantum_effect(self):
        if random.random() < 0.1:  # 10% chance for a quantum effect
            print(f"A quantum effect occurred with {self.name}!")

    def reduce_cooldown(self):
        if self.cooldown_timer > 0:
            self.cooldown_timer -= 1

class Player:
    def __init__(self, name, resource):
        self.name = name
        self.resource = resource
        self.abilities = []

    def add_ability(self, ability):
        self.abilities.append(ability)

    def update_abilities(self):
        for ability in self.abilities:
            ability.reduce_cooldown()

    def use_ability(self, ability_name):
        for ability in self.abilities:
            if ability.name == ability_name:
                ability.use(self)
                break

# Example Usage
player = Player("Hero", 100)
fireball = Ability("Fireball", 20, 5, 3)
player.add_ability(fireball)

fireball.upgrade()  # Level up the ability

# Simulating use of abilities with enhanced features
for _ in range(10):
    player.update_abilities()
    player.use_ability("Fireball")