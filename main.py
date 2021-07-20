from PIL import Image
from PIL import ImageDraw
class Img(): #класс обработки изображения
    def __init__(self, image):
        self.img = Image.open(image) #открыть изображение
        self.img_draw = ImageDraw.Draw(self.img) #инструмент для рисования
        self.width, self.height = self.img.size #получить ширину и высоту
        self.pixels = self.img.load() #получить все пиксели

def F(x, l):
    z = 0
    for i in range(x + 1):
         z+= l[i]
    return z

def main():
    im1 = Img("image.bmp")
    im2 = Img("image.bmp")
    im3 = Img("image.bmp")
    im4 = Img("image.bmp")
    im5 = Img("image.bmp")
    xmax = 0
    xmin = 999
    for i in range(im1.width):
        for j in range(im1.height):
            R = im1.pixels[i, j][0]
            if R >= xmax: #определяем максимум
                xmax = R
            if R < xmin: #определяем минимум
                xmin = R
    ymin = int(input('Введи ymin: '))
    ymax = int(input('Введи ymax: '))
    for i in range(im1.width): #линейное контрастирование
        for j in range(im1.height):
            R = im1.pixels[i, j][0]
            Y = int(((R - xmin) / (xmax - xmin)) * (ymax - ymin) + ymin)
            im1.img_draw.point((i, j), (Y, Y, Y))
    im1.img.save("img1.bmp", "bmp")
    ymin = 0
    ymax = 255
    k = 4 * (ymax - ymin) / ((xmax - xmin) ** 2)
    for i in range(im2.width): #соляризация
        for j in range(im2.height):
            R = im2.pixels[i, j][0]
            Y = int(k*R*(xmax-R))
            im2.img_draw.point((i, j), (Y, Y, Y))
    im2.img.save("img2.bmp", "bmp")
    for i in range(im3.width): #препарирование
        for j in range(im3.height):
            R = im3.pixels[i, j][0]
            if R <= xmax / 3: # отрезок1
                Y = ymax
            elif R > xmax /3 and R < 2*xmax/3: # отрезок2
                Y = 0
            else:
                Y = ymax
            im3.img_draw.point((i, j), (Y, Y, Y))
    im3.img.save("img3.bmp", "bmp")
    dig1 = list()
    dig2 = list()
    for i in range(256):
        dig1.append(0)
    for i in range(im4.width):
        for j in range(im4.height):
            R = im4.pixels[i, j][0]
            dig1[int(R)] += 1
    for i in range(256):
        dig2.append(dig1[i] / (im4.width * im4.height))
    ymin = 1
    ymax = 255
    for i in range(im4.width): #эквализация
        for j in range(im4.height):
            R = im4.pixels[i, j][0]
            Y = int((ymax - ymin) * F (int(R), dig2) + ymin)
            im4.img_draw.point((i, j), (Y, Y, Y))
    im4.img.save("img4.bmp", "bmp")
    for i in range(im5.width): #гиперболизации
        for j in range(im5.height):
            R = im5.pixels[i, j][0]
            Y = int(ymin * ((ymax / ymin) ** F(R, dig2)))
            im5.img_draw.point((i, j), (Y, Y, Y))
    im5.img.save("img5.bmp", "bmp")
if __name__ == '__main__':
    main()