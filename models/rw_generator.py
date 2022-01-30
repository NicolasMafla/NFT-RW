import random
import numpy as np
from PIL import Image, ImageDraw


class RwGenerator:
    def __init__(self, size, bg_color, seed):
        self.size = size
        self.image = Image.new(mode="RGB", size=(size, size), color=bg_color)

    def draw_random_walk(self, steps, walks):
        draw = ImageDraw.Draw(self.image)

        step_shape = (steps, 2)

        repeat = walks

        while repeat > 0:
            center = np.array([np.random.normal(self.size / 2, 25, 2)])
            steps = np.random.choice(a=[-15, -10, 0, 10, 15], size=step_shape)
            path = np.concatenate([center, steps]).cumsum(0)

            min_x, min_y = path.min(axis=0)
            max_x, max_y = path.max(axis=0)
            delta_x = (min_x + max_x - self.size) / 2
            delta_y = (min_y + max_y - self.size) / 2
            path[:, 0] = path[:, 0] - delta_x
            path[:, 1] = path[:, 1] - delta_y

            thickness = range(1, 6)
            line_color = (np.random.randint(255), np.random.randint(255), np.random.randint(255))

            for i in range(len(path) - 1):
                l1 = line_color[0] + (np.random.randint(36) * random.choice([1, -1]))
                l2 = line_color[1] + (np.random.randint(36) * random.choice([1, -1]))
                l3 = line_color[2] + (np.random.randint(36) * random.choice([1, -1]))
                new_line_color = (l1, l2, l3)
                initial = tuple(path[i])
                final = tuple(path[i + 1])
                line = (initial, final)
                draw.line(line, fill=new_line_color, width=random.choice(thickness))

            repeat -= 1

    def save_image(self, name):
        self.image.save(f"./outputs/{name}.png")
