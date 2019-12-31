import random
import math
from PIL import Image

W_DIM = 64 
H_DIM = 128

class Figure():
    def __init__(self, images=None):
        self.images = []
        for url in images:
            temp_img = Image.open(url)
            self.images.append(temp_img)
        
    def getImage(self, scale=0):
        return self.getSizedImage(self.images[0], scale)
    
    def getSizedImage(self, img, scale):
        scale_val = int(math.pow(2, scale))
        w = img.width
        h = img.height
        return img.copy().resize((w // scale_val, h // scale_val))

class PlankFigure(Figure):
    def __init__(self):
        super().__init__(["./plankLeft.png", "./plankMid.png", "./plankRight.png"])

    def getImage(self, scale=0):
        plank_len = random.randint(0, 4) + 2
        plankImage = Image.new("RGBA", (plank_len * W_DIM, H_DIM))
        plankImage.paste(self.images[0])

        for i in range(plank_len):
            plankImage.paste(self.images[1], (W_DIM + (W_DIM * i) - 1, 0))

        plankImage.paste(self.images[2], (int(plankImage.width - 1 - W_DIM), 0))
        return self.getSizedImage(plankImage, scale)
    

box = Figure(["./box.png"])
walk = Figure(["./walk.png"])
roll = Figure(["./roll.png"])
plank = PlankFigure()

def getFigures():
    return [box, walk, roll, plank]


