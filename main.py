from PIL import Image
from time import sleep
from matplotlib import pyplot as plt


def task1():
    image = Image.open("pic2.jpg")
    w, h = image.size
    myImage1 = Image.new("L", (w, h))
    myImage2 = Image.new("L", (w, h))
    diffImage = Image.new("L", (w, h))
    for x in range(w):
        for y in range(h):
            r, g, b = image.getpixel((x, y))
            val = int(0.299 * r + 0.587 * g + 0.114 * b)
            val2 = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
            myImage1.putpixel((x, y), val)
            myImage2.putpixel((x, y), val2)
            diffImage.putpixel((x, y), abs(val - val2))
    myImage1.show()
    #sleep(5)
    plt.stairs(myImage1.histogram())
    plt.show()
    #myImage2.show()
    #sleep(5)
    #diffImage.show()


def task2():
    # Антон вставь свой код сюда и потом сотри pass
    pass


if __name__ == '__main__':
    task1()
    task2()


