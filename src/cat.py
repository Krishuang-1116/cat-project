from .dataloader import CatDataclass, BaseDataloader


class Cat:
    def __init__(
        self,
        name,
        age,
        breed,
        weight,
        body_temp,
        vomit,
        dataloader: BaseDataloader = None,
        index: int = 0
    ):

        if dataloader is None:
            self.name = name
            self.age = age
            self.breed = breed
            self.weight = weight
            self.body_temp = body_temp
            self.vomit = vomit if vomit is not None else []
        else:
            data: CatDataclass = dataloader.get_data(index)
            self.name = data.name
            self.age = data.age
            self.breed = data.breed
            self.weight = data.weight
            self.body_temp = data.body_temp
            self.vomit = data.vomit

    def update_stats(self, age, weight, body_temp, vomit):
        """
        Update the cat's basic information
        """
        self.age = age
        self.weight = weight
        self.body_temp = body_temp
        self.vomit = vomit

    def get_stats(self):
        """
        Return the basic stats of a cat
        """
        return f"Your Cat {self.name} is {self.age} years old, and weighs {self.weight} kg, has a body temperature of {self.body_temp} celcius degrees."
