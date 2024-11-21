from .cat import Cat
from .gui import GUITerminal, GUITkinter
from .health_checker import Healthcheck
import argparse


def main(args: argparse.Namespace):
    pet = Cat("Killua", 3.5, 7.7, 38)
    health_checker = Healthcheck(pet)

    if args.gui == "terminal":
        gui = GUITerminal(pet, health_checker)
    elif args.gui == "tk":
        gui = GUITkinter(pet, health_checker)

    gui.show_welcome()
    gui.show_pet_info()
    gui.show_pet_health_status()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the pet health checker")
    parser.add_argument("--gui", type=str,
                        help="Type of the GUI", default="terminal")
    parser.add_argument(
        "--dataloader", type=str, help="Type of the Dataloader", default="json"
    )

    args = parser.parse_args()

    main(args)
