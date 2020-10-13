"""
### __main__.REQUIREMENTS ###

- Can enter an updated recipe, rate it. Analyze what was changed
    give potential pros and cons of the changes.
    Tagline: Want a leg up at next year's chili cook-off? Use /this app/
    to mathematically learn how to improve your chili for any type of audience.
    Match with your friends. Get their ratings
    Honesty is the key.

"""


class Recipe(object):

    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def add_ingredient(ingredient):
        pass


class Ingredient(object):
    """
    Represent a type of food or spice.
    Has details about nutrition.
    Can have a measure attacched
    - Want to have an interface with the ability to calculate the
    calories in a dish/serving /calories /serving/no/serving list
    
    """
    
    def __init__(self, name):   
        self._name = name

    
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    @property
    def amount(self):
        return self.amount

    @amount.setter
    def amount(self, amount):
        self.amount = amount
    
    
class Measure(object):
    
    def __init__(self, amount, unit):
        # UI Question: '84 cups' can I split on a space, or just regex it?
        # 
        self.inp_amount = amount
        self.inp_unit = unit

    
        
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    @property
    def name(name):
        return self._name

    def set_name(self):
        pass



if __name__ == '__main__':
    rec_1 = Recipe('Thai Curry')
    ing_1 = Ingredient('Onion')
    print(ing_1.amount)
    
