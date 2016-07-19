# -*- coding: utf-8 -*-
import sys
from String2emoji import String2emoji
import argparse

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('messages', type=str, nargs='+', help='emoji message')
    parser.add_argument('-f', '--font', type=str, nargs='?', help='set font (default=meiryob.ttc)')
    parser.add_argument('-o', '--out', type=str, nargs='?', help='output image file (default=test.png)')
    parser.set_defaults(font='meiryob.ttc', out='test.png')

    args = parser.parse_args()

    argv = args.messages
    argc = len(argv)

    fontFile = args.font
    imageFile = args.out

    text = []
    for num in range(0, argc):
        text.append(argv[num])

    emoji = String2emoji(text, fontFile)

    img = emoji.getEmoji()

    img.save(imageFile)

if __name__ == '__main__':
    main()
