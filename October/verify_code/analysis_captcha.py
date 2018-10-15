from io import BytesIO
import requests
from PIL import Image
import numpy as np
import cv2
import os


def get_captcha():
    # 获取验证码图片上每一个像素点的RGB值
    path = os.path.abspath(os.getcwd())
    folder = path + "\\captcha"
    image = Image.open(folder + '\\background07.png', )
    pix = image.load()

    width = image.size[0]
    height = image.size[1]
    print(width, height)
    r_list = []
    g_list = []
    b_list = []
    for x in range(width):
        for y in range(height):
            r, g, b, w = pix[x, y]
            # print(r, g, b)
            r_list.append(r)
            g_list.append(g)
            b_list.append(b)
    L = len(r_list)
    i = 0
    while i <= L:
        if r_list[i] > 2.5 * r_list[i + 1] and g_list[i] > 2.5 * g_list[i + 1] or b_list[i] > 2.5 * b_list[i + 1]:
            distance = int(i / height)
            print(distance)
            return distance
        i += 1

    # for x in range(width):
    #     for y in range(height):
    #         r, g, b, w = pix[x, y]
    #         # print(r, g, b)
    #         r_list.append(r)
    #         g_list.append(g)
    #         b_list.append(b)
    # lines = list()
    # for r, g, b in zip(r_list, g_list, b_list):
    #     RGB = dict()
    #     RGB['R'] = r
    #     RGB['G'] = g
    #     RGB['B'] = b
    #     lines.append(RGB)
    #
    # li = [lines[i:i + 360] for i in range(0, len(lines), 360)]
    # for i in range(len(li)):
    #     line = li[i]
    #     print("----{}----".format(i))
    #     print(line)
        # for j in line:
        #     print(j)
    # L = len(r_list)
    # i = 0
    # while i <= L:
    #     if r_list[i] > 2.5*r_list[i+1] and g_list[i] > 2.5*g_list[i+1] and b_list[i] > 2.5*b_list[i+1]:
    #         distance = int(i/height)
    #         print(distance)
    #         break
    #     i += 1


if __name__ == '__main__':
    get_captcha()


# def CannyThreshold(lowThreshold):
#     # 获取验证码图片轮廓
#     detected_edges = cv2.GaussianBlur(gray, (3, 3), 0)
#     detected_edges = cv2.Canny(detected_edges, lowThreshold, lowThreshold*ratio, apertureSize=kernel_size)
#     dst = cv2.bitwise_and(img, img, mask=detected_edges)  # just add some colours to edges from original image.
#     cv2.imshow('canny demo', dst)
#
#
# lowThreshold = 0
# max_lowThreshold = 100
# ratio = 3
# kernel_size = 3
#
# path = os.path.abspath(os.getcwd())
# folder = path + "\\captcha"
# file = folder + '\\background04.png'
# print(file)
# img = cv2.imread(file)
#
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.namedWindow('canny demo')
# cv2.createTrackbar('Min threshold', 'canny demo', lowThreshold, max_lowThreshold, CannyThreshold)
#
# CannyThreshold(100)  # initialization
# if cv2.waitKey(0) == 27:
#     cv2.destroyAllWindows()