class GameCharacter:
 
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def is_alive(self):
        return self.hp > 0

    def get_attacked(self, damage):
        if self.is_alive():
            self.hp -= damage if self.hp >= damage else 0
        else:
            print(f"{self.name}은 이미 죽었습니다.")
        
    def attack(self, other_character):
        if self.is_alive():
            other_character.get_attacked(self.power)

    def __str__(self):
        return self.name+"님의 hp는 "+str(self.hp)+"만큼 남았습니다."


character_1 = GameCharacter("Ww영훈전사wW", 200, 30)
character_2 = GameCharacter("Xx지웅최고xX", 100, 50)

character_1.attack(character_2)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)

print(character_1)
print(character_2)