class game_character:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    def attack(self, enemy):
        print(f"{self.name} attacks {enemy.name} for {self.atk} damage!")
        enemy.hp -= self.atk  # Fixed: changed 'health' to 'hp' to match your setup!

    def heal(self, amount):
        self.hp += amount
        print(f"{self.name} heals for {amount} HP! Current HP: {self.hp}")


# --- ACTIVE GAMEPLAY CODE (Move these completely to the left wall!) ---

player1 = game_character("Wira", 100, 20)
boss = game_character("Boss", 150, 25)

print("Battle Start!")
print(f"{player1.name} HP: {player1.hp}, {boss.name} HP: {boss.hp}")
print()

player1.attack(boss)
print(f"{boss.name} Boss HP: {boss.hp}")
boss.attack(player1)
print(f"{player1.name} Wira HP: {player1.hp}")
print()

player1.heal(15)