from abc import abstractmethod
import json
import random
from dataclasses import dataclass
from faker import Faker
import numpy as np

fake = Faker()  # need to instantiate a Faker object


@dataclass
class CatDataclass:
    name: str
    age: int
    breed: int
    weight: float
    body_temp: float
    vomit: list


class BaseDataloader:

    def __init__(self) -> None:
        pass

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def preprocess_data(self):
        pass

    @abstractmethod
    def get_data(self) -> CatDataclass:
        pass


class JSONDataloader(BaseDataloader):
    ''''
    Load cat data from my json file. 
    '''

    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self.data = None

    def load_data(self):
        with open(self.file_path, "r", encoding='utf-8') as f:
            self.data = json.load(f)
        print('Loading cat data...')

    def preprocess_data(self):
        '''
        Transform the data imported from json file into standard format
        '''
        if self.data:
            for cat in self.data:
                for key, value in cat.items():
                    if isinstance(value, str):
                        # Strip the white space and then capitalize each word
                        cat[key] = value.strip().title()
                    elif isinstance(value, float):
                        if key not in ['weight', 'body_temp']:
                            cat[key] = int(value)
                    elif isinstance(value, list):
                        cat[key] = [bool(v) for v in cat[key]]
        print('Preprocessing cat data...')

    def get_data(self, index=0):
        print(f"Getting cat data for index {index}")
        print(f"Data available: {len(self.data)} cats")

        if index >= len(self.data):
            raise ValueError(f"Cat index {index} is out of range")
        return CatDataclass(
            name=self.data[index]['name'],
            age=self.data[index]['age'],
            breed=self.data[index]['breed'],
            weight=self.data[index]['weight'],
            body_temp=self.data[index]['body_temp'],
            vomit=self.data[index]['vomit']
        )


# Alternative dataloader


class RandomDataloader(BaseDataloader):
    '''
    Generate random cat data
    '''

    def get_data(self):
        return CatDataclass(
            name=fake.first_name(),
            age=random.randint(1, 18),
            breed=random.choice(["Maine Coon", "Siamese", "Persian", "Bengal",
                                 "Ragdoll", "Abyssinian", "Sphynx", "British Shorthair"]),
            weight=np.random.uniform(4, 20),
            body_temp=np.random.uniform(36, 42),
            vomit=[random.choice([True, False]) for _ in range(5)]
        )


# To be defined in V1
class APIDataloader(BaseDataloader):
    '''
    Fetch cat data from an API,which will be defined in V1 or V2
    '''

    def __init__(self, url) -> None:
        self.url = url
        self.data = None

    def load_data(self):
        pass

    def preprocess_data(self):
        pass

    def get_data(self):
        return self.data
