class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"The {self.brand} {self.model} engine has started")

    def stop_engine(self):
        print(f"The {self.brand} {self.model} engine has stopped")



