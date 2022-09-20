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
    image = Image.open('pic2.jpg')
    w, h = image.size
    red_image = Image.new("RGB", (w, h))
    green_image = Image.new("RGB", (w, h))
    blue_image = Image.new("RGB", (w, h))

    for x in range(w):
        for y in range(h):
            r, g, b = image.getpixel((x, y))
            red_image.putpixel((x, y), (r, 0, 0))
    red_image.show()
    plt.stairs(red_image.histogram())
    plt.show()

    for x in range(w):
        for y in range(h):
            r, g, b = image.getpixel((x, y))
            green_image.putpixel((x, y), (0, g, 0))
    #green_image.show()
    #plt.stairs(red_image.histogram())
    #plt.show()

    for x in range(w):
        for y in range(h):
            r, g, b = image.getpixel((x, y))
            blue_image.putpixel((x, y), (0, 0, b))
    #blue_image.show()
    #plt.stairs(red_image.histogram())
    #plt.show()


if __name__ == '__main__':
    task1()
    task2()


