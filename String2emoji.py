# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont

class String2emoji(object):
    """docstring for String2emoji"""
    def __init__(self, argText,argFontName):
        self.textList = argText
        self.fontName = argFontName
        self.backColor = (255,255,255,0)
        self.imageSize = (128,128)

    def getFont(self,size):
        return ImageFont.truetype(self.fontName, size, encoding='utf-8')

    def cutEffectiveRange(self, text, width, height):
        pt = height * 2
        for i in range(8, height*2):
            font = self.getFont(i)
            w, h = font.getsize(text)
            if ((w > width) or (h > height)):
                x0, y0, x1, y1 = self.getStringRect(text, font, w, h)
                if (((x1-x0) > width) or ((y1-y0) > height)):
                    print("over")
                    pt = i - 1
                    break;
        font = self.getFont(pt)
        w, h = font.getsize(text)
        x0, y0, x1, y1 = self.getStringRect(text, font, w, h)
        print("%d,%d,%d,%d" % (x0, y0, x1, y1))
        return(pt, x0, y0, x1, y1)

    def getTopLeftY(self, img):
        w = img.width
        h = img.height
        for cy in range(0, h):
            for cx in range(0, w):
                color = img.getpixel((cx, cy))
                if color != self.backColor:
                    return cy
        return -1

    def getTopLeftX(self, img):
        w = img.width
        h = img.height
        for cx in range(0, w):
            for cy in range(0, h):
                color = img.getpixel((cx, cy))
                if color != self.backColor:
                    return cx
        return -1

    def getBottomRightY(self, img):
        w = img.width
        h = img.height
        for cy in range(h-1, -1, -1):
            for cx in range(0, w):
                color = img.getpixel((cx, cy))
                if color != self.backColor:
                    return cy
        return -1

    def getBottomRightX(self, img):
        w = img.width
        h = img.height
        for cx in range(w-1, -1, -1):
            for cy in range(0, h):
                color = img.getpixel((cx, cy))
                if color != self.backColor:
                    return cx
        return -1


    def getStringRect(self, text, font, w, h):
        img = Image.new("RGBA", (w, h), self.backColor)
        draw = ImageDraw.Draw(img)
        draw.text((0,0), text, fill=(0,0,0), font=font)
        x0 = self.getTopLeftX(img)
        y0 = self.getTopLeftY(img)
        x1 = self.getBottomRightX(img)
        y1 = self.getBottomRightY(img)
        return (x0, y0, x1, y1)





    def getEmoji(self):
        img = Image.new("RGBA", self.imageSize, self.backColor)
        draw = ImageDraw.Draw(img)
        #draw.rectangle([(0, 0), (128, 128)], outline=(255,0,0))

        l = len(self.textList)
        width = 128
        height = int(128 / l)

        for i in range(0,l):
            print("loop=%d" % i)

            (size, x0, y0, x1, y1) = self.cutEffectiveRange(self.textList[i], width, height)
            print("size=%d, %d, %d, %d, %d" % (size, x0, y0, x1, y1))
            font = self.getFont(size)
            w = x1 - x0
            h = y1 - y0

            ox = int((width - w)/2)
            oy = int((height - h)/2) + (height * i)
            x = ox - x0
            y = oy - y0

            #draw.rectangle([(ox, oy), (ox+w, oy+h)], outline=(0,0,255))
            draw.text((x, y), self.textList[i], fill=(0, 0, 0), font=font)

        return img
