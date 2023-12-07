############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller 
        self.name = name
        
        self.pairings = []


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code



def make_melon_types():
    """Returns a list of current melon types."""

    musk_melon = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    casaba = MelonType("cas", 2003, "orange", False, False, "Casaba")
    crenshaw = MelonType('cren', 1996, 'green', False, False, "Crenshaw")
    yellow_watermelon = MelonType('yw', 2013, 'yellow', False, True, "Yellow Watermelon")

    musk_melon.pairings.append("mint")
    casaba.pairings.append("strawberries")
    casaba.pairings.append("mint")
    crenshaw.pairings.append("prosciutto")
    yellow_watermelon.pairings.append("ice cream")
    
    all_melon_types = [musk_melon, casaba, crenshaw, yellow_watermelon]

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
   

    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f"-{pairing}")
        


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melons_by_code = {}
    
    for melon in melon_types:
       key = melon.code
       attributes = melon
       melons_by_code[key] =  attributes
             
    return melons_by_code
    # Fill in the rest

# # {"musk": {"color": "green",
#             "code": "musk"
# }
# }
############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape_rating, color_rating, from_field, harvester):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.from_field = from_field 
        self.harvester = harvester

    def is_sellable(self, shape_rating, color_rating, from_field):
        if from_field != 3:
            if shape_rating > 5 and color_rating > 5:
                return True
        return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melons_by_code = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melons_by_code['yw'], 8, 7, 2, "Sheila")
    melon_2 = Melon(melons_by_code['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melons_by_code['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melons_by_code['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melons_by_code['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melons_by_code['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melons_by_code['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melons_by_code['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melons_by_code['yw'], 7, 10, 3, 'Sheila')
    
    melons = [melon_1, 
              melon_2, 
              melon_3, 
              melon_4, 
              melon_5, 
              melon_6, 
              melon_7, 
              melon_8, 
              melon_9,]
    
    return melons
    

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable():
            print(f"Harvested by {melon.harvester} from Field {melon.from_field} (NOT SELLABLE)") 
        else:
            print(f"Harvested by {melon.harvester} from Field {melon.from_field} (CAN BE SOLD)")     
