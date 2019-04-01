class Book():
    def __init__(self, _id, _name, _price):
        self.id = _id
        self.name = _name
        self.price = _price

    def __str__(self):
        return "id: %s name: %s price： %s" % (self.id,self.name,self.price)