import random
from models.rw_generator import RwGenerator

random.seed(1)

names = ["Enid", "Nixie", "Fawn", "Clarion", "Juno", "Tiana", "Korra", "Aine", "Ondine", "Ella", "Circe", "Jadis",
         "Endora", "Sybil", "Piper", "Nimue", "Tara", "Clio", "Iris", "Daria", "Kouzlo", "Yadu", "Sen", "Caerus",
         "Blythe", "Buyu", "Taika", "Aether", "Pontus", "Zephyr"]

random.shuffle(names)

if __name__ == "__main__":
    for i in range(1, 31):
        size = 800
        bg = (0, 0, 0)
        r = RwGenerator(size, bg, 1)
        r.draw_random_walk(steps=500, walks=3)
        r.save_image(f"rw_dream_{names[i - 1].lower()}")
        print(f"Random walk dream {names[i - 1]} created")
