from src.cat import Cat
from src.dataloader import JSONDataloader
from src.health_checker import Healthcheck
from src.gui import GUITkinter

if __name__ == "__main__":
    dataloader = JSONDataloader(file_path="data/mock_data.json")
    dataloader.load_data()
    dataloader.preprocess_data()
    print("Data preprocessing completed")

    print("Creating cat instance...")
    cat1 = Cat(None, None, None, None, None, None,
               dataloader=dataloader, index=0)
    print(f"Cat created: {cat1.name}")

    print("Creating healthcheck...")
    healthcheck1 = Healthcheck(cat1)
    print("Healthcheck created")

    gui = GUITkinter(cat1, healthcheck1)
    gui.show_welcome()
    gui.show_pet_info()
    gui.show_pet_health_check_result()
    gui.root.mainloop()