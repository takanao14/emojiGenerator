# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont

class String2emoji(object):
    """docstring for String2emoji"""
    def __init__(self, argText, argColor, argFontName):
        self.textList = argText
        self.fontName = argFontName
        self.color = argColor
        self.backColor = (255,255,255,0)
        self.imageSize = (128,128)

    def getFont(self,size):
        return ImageFont.truetype(self.fontName, size, encoding='utf-8')

    def cutEffectiveRange(self, text, width, height):
        pt = height * 2
        for i in range(8, pt):
            font = self.getFont(i)
            fw, fh = font.getsize(text)
            if ((fw > width) or (fh > height)):
                ox, oy, w, h = self.getStringRect(text, font, fw, fh)
                if ((w > width) or (h > height)):
                    print("over")
                    pt = i - 1
                    break;
        font = self.getFont(pt)
        fw, fh = font.getsize(text)
        ox, oy, w, h = self.getStringRect(text, font, fw, fh)
        print("ox=%d,oy=%d,w=%d,h=%d" % (ox, oy, w, h))
        return(pt, ox, oy, w, h)

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


    def getStringRect(self, text, font, fw, fh):
        img = Image.new("RGBA", (fw, fh), self.backColor)
        draw = ImageDraw.Draw(img)
        draw.text((0,0), text, fill=(0,0,0), font=font)
        x0 = self.getTopLeftX(img)
        y0 = self.getTopLeftY(img)
        x1 = self.getBottomRightX(img)
        y1 = self.getBottomRightY(img)
        return (x0, y0, x1 - x0, y1 - y0)


    def getEmoji(self):
        img = Image.new("RGBA", self.imageSize, self.backColor)
        draw = ImageDraw.Draw(img)
        #draw.rectangle([(0, 0), (128, 128)], outline=(255,0,0))

        textlen = []
        l = len(self.textList)
        for i in range(0, l):
            textlen.append(len(self.textList[i]))
        print(textlen)

        if (min(textlen) == max(textlen)):
            sameMode = True
        else:
            sameMode = False

        l = len(self.textList)
        width = 128
        height = int(128 / l)

        sizelist = []
        for i in range(0, l):
            (size, ox, oy, w, h) = self.cutEffectiveRange(self.textList[i], width, height)
            sizelist.append(size)
        if sameMode:
            size = min(sizelist)
            for i in range(0, l):
                sizelist[i] = size

        for i in range(0, l):
            text = self.textList[i]
            font = self.getFont(sizelist[i])
            fw, fh = font.getsize(text)
            (ox, oy, w, h) = self.getStringRect(text, font, fw, fh)
            x = int((width - w)/2)
            y = int((height - h)/2) + (height * i)
            #draw.rectangle([(x, y), (x+w, y+h)], outline=(0,0,255))
            draw.text((x - ox, y - oy), text, fill=self.color, font=font)

        return img

