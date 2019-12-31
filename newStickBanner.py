from PIL import Image
import sys
import math
import figures
import random

HEIGHT = 128

def getFigure(banner_space):
    img_size = -1
    img = None
    while img_size == -1 or img_size > banner_space:
        fig_temp = figures.getFigures()[random.randint(0, len(figures.getFigures()) - 1)]
        img = fig_temp.getImage()
        img_size = img.width
    
    return img

if __name__ == "__main__":
    
    if len(sys.argv) < 4:
        print("Please give an argument for:\nbanner width in pixels\nbanner height in row number\nscale factor (0-3)")
        exit(1)
    SCALE = int(sys.argv[3])
    ROWS = int(sys.argv[2])
    WIDTH = int(sys.argv[1])
    HEIGHT = ROWS * 128
    banner = Image.new("RGBA", (WIDTH, HEIGHT), (255, 255, 255, 255))
    padding = (WIDTH % 64) / 2
   
    for i in range(ROWS):
        banner_space = WIDTH - (2 * padding)
        
        while banner_space > 0:
            figure_img = getFigure(banner_space)
            banner.paste(figure_img, (int(WIDTH - banner_space - 1), i * 128), figure_img)
            banner_space -= figure_img.width
    new_w = int(banner.width // math.pow(2, SCALE))
    new_h = int(banner.height // math.pow(2, SCALE))
    banner = banner.resize((new_w, new_h))
    banner.show()

