class Item:
    def __init__(self, room_number, i_description, i_name):
        self.room_number = room_number
        self.i_description = i_description
        self.i_name = i_name

def populate_items():
    item_list = []
    key = Item(3, "A glass key. Brittle. It will definitely break after use. Get the key?", "key")
    item_list.append(key)

    elixir = Item(2, "A healing elixir. It will restore your HP, but can only be used once. Get the elixir?",
                  "elixir")
    item_list.append(elixir)

    mirror = Item(1, "A pocket mirror is lying on the ground. Get the mirror?", "mirror")
    item_list.append(mirror)
    """Charm is set to -3 instead of -2, the typical out of play value. 
    This is for the sake of setting wizard's attack properly post-battle."""
    charm = Item(-3, 'A charm of some sort is present. '
                     'Just standing near it makes you feel stronger. Get the charm?', 'charm')
    item_list.append(charm)

    talisman = Item(14, 'A talisman of some sort is present. Just standing near it '
                        'invigorates you. Get the talisman?', 'talisman')
    item_list.append(talisman)
    blessing = Item(15, 'The dragon offers you its blessing. Get blessing?', 'blessing')
    item_list.append(blessing)
    return item_list