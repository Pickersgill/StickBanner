import random
from PIL import Image

class Figure():
    def __init__(self, images=None):
        self.images = []
        for url in images:
            temp_img = Image.open(url)
            self.images.append(temp_img)
        
    def getImage(self):
        return self.images[0]

class PlankFigure(Figure):
    def __init__(self):
        super().__init__(["./plankLeft.png", "./plankMid.png", "./plankRight.png"])

    def getImage(self):
        plank_len = random.randint(0, 4) + 2
        plankImage = Image.new("RGBA", (plank_len * 64, 128))
        plankImage.paste(self.images[0])

        for i in range(plank_len):
            plankImage.paste(self.images[1], (64 + (64 * i) - 1, 0))

        plankImage.paste(self.images[2], (int(plankImage.width - 1 - 64), 0))
        return (plankImage)

box = Figure(["./box.png"])
walk = Figure(["./walk.png"])
roll = Figure(["./roll.png"])
plank = PlankFigure()

def getFigures():
    return [box, walk, roll, plank]


