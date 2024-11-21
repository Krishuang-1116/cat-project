from src.cat import Cat
from src.dataloader import JSONDataloader
from src.gui import GUITkinter

if __name__ == "__main__":

    dataloader = JSONDataloader(file_path="data/mock_data.json")
    dataloader.load_data()
    dataloader.preprocess_data()
    print("Data preprocessing completed")

    print("Creating cat instance...")
    cats = []
    for i in range(len(dataloader.data)):
        cat = Cat(None, None, None, None, None, None,
                  dataloader=dataloader, index=i)
        cats.append(cat)
    print(f"Cat created: {cat.name}")

    gui = GUITkinter(cats, check_health=True)
    gui.show_welcome()
    gui.root.mainloop()
