class Car_private:
    def __init__(self, brand, model):
        self._brand = brand   # protected
        self.__model = model # private

    def get_model(self):
        return self.__model

    def set_model(self, new_model):
        self.__model = new_model



