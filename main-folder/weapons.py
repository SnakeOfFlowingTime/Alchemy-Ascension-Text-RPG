# Weapon class thingy
class Weapon:
    def __init__(self, name: str, type: str, dmg: int, value: int):
        self.name = name
        self.type = type
        self.dmg = dmg
        self.value = value

# Weapons
fists = Weapon(name  = 'Fists',
               type  = 'unarmed',
               dmg   = 1,
               value = 0)

wooden_sword = Weapon(name  = 'Wooden Sword',
                      type  = 'blunt',
                      dmg   = 2,
                      value = 1)

weak_bow = Weapon(name  = 'Weak Bow',
                  type  = 'bow',
                  dmg   = 3,
                  value = 3)

rusty_dagger = Weapon(name  = 'Rusty Dagger',
                      type  = 'short blade',
                      dmg   = 2,
                      value = 2)
acid_body = Weapon(name  = 'Acidic Body',
                   type  = 'acid',
                   dmg   = 2,
                   value = 1)