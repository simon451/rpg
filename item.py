class Item():
    def __init__(self, item_name):
        self._name = item_name
        self._description = None
        self._size = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, item_name):
        self._name = item_name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, item_description):
        self._description = item_description

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, item_size):
        self._size = item_size

    def describe(self):
        print("There is a " + self._name + " here. " + self._description)
        #print(self._size)