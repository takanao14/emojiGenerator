# -*- coding: utf-8 -*-
import sys
from String2emoji import String2emoji
import argparse


def main():

    def convColor(colorString):
        """ convert #RRGGBB to (r, g, b) tuple"""
        if len(colorString) != 6:
            return None
        r, g, b = colorString[:2], colorString[2:4], colorString[4:]
        r, g, b = [int(n, 16) for n in (r, g, b)]
        return (r, g, b)

    parser = argparse.ArgumentParser()
    parser.add_argument('messages', type=str, nargs='+', help='emoji message')
    parser.add_argument('-f', '--font', type=str, nargs='?', help='set font (default=meiryob.ttc)')
    parser.add_argument('-o', '--out', type=str, nargs='?', help='output image file (default=test.png)')
    parser.add_argument('-c', '--color', type=convColor, nargs='?', help='draw color #RRGGBB (default=#000000)')
    parser.set_defaults(font='NotoSansJP-Bold.otf', out='test.png', color='000000')

    args = parser.parse_args()

    argv = args.messages
    argc = len(argv)

    fontFile = args.font
    imageFile = args.out
    color = args.color
    if color is None:
        parser.error("color")
    print(color)

    text = []
    for num in range(0, argc):
        text.append(argv[num])

    emoji = String2emoji(text, color, fontFile)

    img = emoji.getEmoji()

    img.save(imageFile)

if __name__ == '__main__':
    main()
