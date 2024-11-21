from abc import abstractmethod
import tkinter as tk

from .cat import Cat
from .health_checker import Healthcheck


class BaseGUI:

    def __init__(self, cats, check_health) -> None:
        pass

    @abstractmethod
    def show_welcome(self):
        pass

    @abstractmethod
    def show_pet_info(self):
        pass

    @abstractmethod
    def show_pet_health_check_result(self):
        pass


class GUITkinter(BaseGUI):
    '''
    Use Tkinter to show the information. For V0 and V1.
    '''

    def __init__(self, cats, check_health: Healthcheck, current_index=0,) -> None:
        super().__init__(cats, check_health)
        print("Initializing GUI...")

        self.cats = cats
        self.current_index = current_index
        self.current_cat = self.cats[self.current_index]
        self.check_health = Healthcheck(self.current_cat)

        self.root = tk.Tk()
        self.root.title("Cat Health Checker")
        self.root.geometry("800x600")

        self.display_label = tk.Label(self.root, text="Welcome to your cat health checker!",
                                      font=("Helvetica", 24, "bold"))
        self.display_label.pack(pady=50)

        print("Creating buttons...")
        self.info_button = tk.Button(self.root, text="Show your cat's information",
                                     command=self.display_pet_info,
                                     font=("Helvetica", 12),
                                     padx=20, pady=10,
                                     width=20, height=2)
        self.info_button.pack(pady=10)

        self.check_button = tk.Button(self.root,
                                      text="Check cat's health status",
                                      command=self.display_health_check_result,
                                      padx=20, pady=10,
                                      font=("Helvetica", 12),
                                      width=20, height=2)
        self.check_button.pack(pady=10)

        self.next_button = tk.Button(self.root, text="Next cat",
                                     command=self.next_cat,
                                     padx=20, pady=10,
                                     font=("Helvetica", 12),
                                     width=20, height=2)
        self.next_button.pack(pady=10)

        self.prev_button = tk.Button(self.root, text="Previous cat",
                                     command=self.prev_cat,
                                     padx=20, pady=10,
                                     font=("Helvetica", 12),
                                     width=20, height=2)
        self.prev_button.pack(pady=10)

        self.counter_label = tk.Label(self.root, text=f"Displaying cat {self.current_index +1 } of {len(self.cats)} cats",
                                      font=("Helvetica", 12))
        self.counter_label.pack(pady=10)
        print("GUI initialization completed")

    def show_welcome(self):
        print("Showing welcome...")  # Debug print
        self.display_label.config(
            text="Welcome to your cat health checker!",
            font=("Helvetica", 24, "bold")
        )

    def display_pet_info(self) -> None:
        print("Displaying pet info for {self.current_cat}...")  # Debug print
        self.display_label.config(
            text=str(self.current_cat.get_stats()),
            font=("Helvetica", 16)
        )

    def display_health_check_result(self):
        print("Displaying health check...")  # Debug print
        self.display_label.config(
            text=str(self.check_health.health_status()),
            font=("Helvetica", 16)
        )

    def next_cat(self):
        self.current_index = (self.current_index + 1) % len(self.cats)
        self.current_cat = self.cats[self.current_index]
        self.check_health = Healthcheck(self.current_cat)
        self.counter_label.config(
            text=f"Displaying cat {self.current_index +1 } of {len(self.cats)} cats",
            font=("Helvetica", 12)
        )
        self.display_pet_info()

    def prev_cat(self):
        self.current_index = (self.current_index - 1) % len(self.cats)
        self.current_cat = self.cats[self.current_index]
        self.check_health = Healthcheck(self.current_cat)
        self.counter_label.config(
            text=f"Displaying cat {self.current_index + 1} of {len(self.cats)} cats")
        self.display_pet_info()


""" class GUITerminal(BaseGUI):
    '''
    Use terminal to show the information. To be done in V1 or V2
    '''

    def __init__(self, pet: Cat, health_checker: Healthcheck) -> None:
        super().__init__()
        self.pet = pet
        self.hc = health_checker

    def show_welcome(self):
        print("Welcome to the pet health checker!")

    def show_pet_info(self):
        print(
            f"Your pet is {self.pet.age} years old, weighs {self.pet.weight} kg, and has a body temperature of {self.pet.body_temp}"
        )

    def show_pet_health_status(self):
        print(self.hc.health_status())
 """
