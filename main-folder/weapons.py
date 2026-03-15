# Weapon class thingy
class Weapon:
    def __init__(self, name: str, id: str, type: str, dmg: int, value: int):
        self.name = name
        self.id = id
        self.type = type
        self.dmg = dmg
        self.value = value

# Weapons
weapons = {
'fists' : Weapon(name = 'Fists', id = 'fists', type = 'unarmed', dmg = 1, value = 0),

'wooden sword' : Weapon(name = 'Wooden Sword', id = 'wooden sword', type = 'blunt', dmg = 2, value = 1),

'weak bow' : Weapon(name = 'Weak Bow', id = 'weak bow', type = 'bow', dmg = 3, value = 3),

'rusty dagger' : Weapon(name = 'Rusty Dagger', id = 'rusty dagger', type = 'short blade', dmg = 2, value = 2),

'acid body' : Weapon(name = 'Acidic Body', id = 'acid body', type = 'acid', dmg = 2, value = 1),
}