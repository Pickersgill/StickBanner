from PIL import Image
import sys
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
    
    if len(sys.argv) < 2:
        print("Please give an argument for banner width in pixels, e.g. 200")
        exit(1)

    WIDTH = int(sys.argv[1])
    banner = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    padding = (WIDTH % 64) / 2
    banner_space = WIDTH - (2 * padding)
        
    while banner_space > 0:
        figure_img = getFigure(banner_space)
        banner.paste(figure_img, (int(WIDTH - banner_space - 1), 0))
        banner_space -= figure_img.width

    banner.show()

