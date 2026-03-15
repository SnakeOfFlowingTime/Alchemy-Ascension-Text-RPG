
# Armor class
class Armor:
    def __init__(self, name: str, id: str, type: str, defense: int, value: int):
        self.name = name
        self.id = id
        self.type = type
        self.defense = defense
        self.value = value


armors = {
'no armor': Armor(name = 'No Armor',
                  id = 'no armor',
                  type = 'none',
                  defense = 0,
                  value = 0
                  ),
'linen clothing': Armor(name = 'Linen Clothes',
                        id = 'linen clothing',
                        type = 'cloth',
                        defense = 0,
                        value = 2
                        ),
'weak wood armor': Armor(name = 'Weak Wood Armor',
                         id = 'weak wood armor',
                         type = 'wood',
                         defense = 1,
                         value = 10,
                         )



}