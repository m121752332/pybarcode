#!/usr/bin/env python
# -*- coding: utf-8 -*-

import barcode
from barcode.writer import ImageWriter
from barcode.codex import Code39
from PIL import Image, ImageDraw, ImageFont, ImageWin
import io


def testEan():
    imagewriter = ImageWriter()
    # 保存到图片中
    # add_checksum : Boolean   Add the checksum to code or not (default: True)
    ean = Code39("1234567890", writer=imagewriter, add_checksum=False)
    # 不需要写后缀，ImageWriter初始化方法中默认self.format = 'PNG'
    ean.save('image')
    img = Image.open('image.png')
    img.show()


if __name__ == '__main__':
    testEan()
