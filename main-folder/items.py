
# Items class
class Item:
    def __init__(self, name: str, id: str, description: str, value: int):
        self.name = name
        self.id = id
        self.description = description
        self.value = value

# Healing items subclass
class HealItem(Item):
    def __init__(self, name: str, id: str, description: str, value: int, hpheal: int):
        super().__init__(name, id, description, value)
        self.hpheal = hpheal



items = {
't0 bandage': HealItem(name = 'Slime-Based Bandages', id = 't0 bandage',
description = 'bandages infused with specially treated slime, very effective in healing small wounds', 
value = 1, hpheal = 3),
'rag': Item(name = 'Rag', id = 'rag', description = 'a torn and dirty piece of rag', value = 1),


}