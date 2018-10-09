from PIL import Image
import numpy as np
import cv2
import os


def get_captcha():
    path = os.path.abspath(os.getcwd())
    folder = path + "\\captcha"
    image = Image.open(folder + '\\background06.png', )
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
            r_list.append(r)
            g_list.append(g)
            b_list.append(b)
    L = len(r_list)
    i = 0
    while i <= L:
        if r_list[i] > 2.5*r_list[i+1] and g_list[i] > 2.5*g_list[i+1] and b_list[i] > 2.5*b_list[i+1]:
            distance = int(i/height)
            print(distance)
            break
        i += 1


if __name__ == '__main__':
    get_captcha()

# def CannyThreshold(lowThreshold):
#     detected_edges = cv2.GaussianBlur(gray, (3, 3), 0)
#     detected_edges = cv2.Canny(detected_edges, lowThreshold, lowThreshold*ratio, apertureSize=kernel_size)
#     dst = cv2.bitwise_and(img, img, mask=detected_edges)  # just add some colours to edges from original image.
#     cv2.imshow('canny demo', dst)
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
#
# cv2.namedWindow('canny demo')
#
# cv2.createTrackbar('Min threshold', 'canny demo', lowThreshold, max_lowThreshold, CannyThreshold)
#
# CannyThreshold(82)  # initialization
# if cv2.waitKey(0) == 27:
#     cv2.destroyAllWindows()
#
# # coding=utf-8
# import cv2
# import numpy
#
# img = cv2.imread(file)
#
# img = cv2.GaussianBlur(img, (3, 3), 0)
# edges = cv2.Canny(img, 50, 150, apertureSize=3)
# print(edges)
# lines = cv2.HoughLines(edges, 1, numpy.pi / 180, 118)  # 这里对最后一个参数使用了经验型的值
# print(lines)
# result = img.copy()
# for line in lines[0]:
#     rho = line[0]  # 第一个元素是距离rho
#     theta = line[1]  # 第二个元素是角度theta
#     print(rho)
#     print(theta)
# #     print
#     rho
#     print
#     theta
#     if (theta < (np.pi / 4.)) or (theta > (3. * np.pi / 4.0)):  # 垂直直线
#         # 该直线与第一行的交点
#         pt1 = (int(rho / np.cos(theta)), 0)
#         # 该直线与最后一行的焦点
#         pt2 = (int((rho - result.shape[0] * np.sin(theta)) / np.cos(theta)), result.shape[0])
#         # 绘制一条白线
#         cv2.line(result, pt1, pt2, (255))
#     else:  # 水平直线
#         # 该直线与第一列的交点
#         pt1 = (0, int(rho / np.sin(theta)))
#         # 该直线与最后一列的交点
#         pt2 = (result.shape[1], int((rho - result.shape[1] * np.cos(theta)) / np.sin(theta)))
#         # 绘制一条直线
#         cv2.line(result, pt1, pt2, (255), 1)
#
# cv2.imshow('Canny', edges)
# cv2.imshow('Result', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# from selenium import webdriver
# from PIL import Image
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from PIL import Image
# import time
#
#
# def get_snap(driver):
#     driver.save_screenshot('full_snap.png')
#     page_snap_obj = Image.open('full_snap.png')
#     return page_snap_obj
#
# #
# # def get_smallimg(driver):
# #     img1 = driver.find_element_by_xpath('//*[@class="JDJRV-smallimg"]/img')
# #     img2 = driver.find_element_by_xpath('//*[@class="JDJRV-bigimg"]/img')
# #     time.sleep(2)
# #     location = img1.location
# #     size = img1.size
# #
# #     left = location['x']
# #     top = location['y']
# #     right = left + size['width']
# #     bottom = top + size['height']
# #
# #     page_snap_obj = get_snap(driver)
# #     image_obj = page_snap_obj.crop((left, top, right, bottom))
# #     # image_obj.show()
# #     return image_obj
#
#
# def get_bigimg(driver):
#     img2 = driver.find_element_by_xpath('//*[@class="JDJRV-bigimg"]/img')
#     time.sleep(2)
#     location = img2.location
#     size = img2.size
#
#     left = location['x']
#     top = location['y']
#     right = left + size['width']
#     bottom = top + size['height']
#
#     page_snap_obj = get_snap(driver)
#     image_obj = page_snap_obj.crop((left, top, right, bottom))
#     # image_obj.show()
#     return image_obj
#
#
# def get_distance(image):
#     # start = 57
#     # threhold = 60
#     #
#     # for i in range(start, image1.size[0]):
#     #     for j in range(image1.size[1]):
#     #         rgb1 = image1.load()[i, j]
#     #         rgb2 = image2.load()[i, j]
#     #         res1 = abs(rgb1[0] - rgb2[0])
#     #         res2 = abs(rgb1[1] - rgb2[1])
#     #         res3 = abs(rgb1[2] - rgb2[2])
#     #         # print(res1,res2,res3)
#     #         if not (res1 < threhold and res2 < threhold and res3 < threhold):
#     #             return i - 7
#     # return i - 7
#     # self.driver.get(license_url)
#     # self.driver.implicitly_wait(5)
#     # time.sleep(1)
#     # # 创建目录
#     # path = os.path.abspath(os.path.dirname(os.getcwd()))
#     # folder = path + "\\captcha"
#     # if not os.path.exists(folder):
#     #     os.mkdir(folder)
#     # # 获取验证码截图
#     # self.driver.save_screenshot(folder + '/{}.png'.format(shop))
#     # element = self.driver.find_element_by_xpath('//*[@class="verify"]/img')
#     # # 获取验证码坐标
#     # left = element.location['x']
#     # top = element.location['y']
#     # right = element.location['x'] + element.size['width']
#     # bottom = element.location['y'] + element.size['height']
#     # # 保存截图
#     # im = Image.open(folder + '/{}.png'.format(shop))
#     # im = im.crop((left, top, right, bottom))
#     # im.save(folder + '/{}.png'.format(shop))
#     #
#     pix = image.load()
#     width = image.size[0]
#     height = image.size[1]
#     print(width, height)
#     r_list = []
#     g_list = []
#     b_list = []
#     for x in range(width):
#         for y in range(height):
#             r, g, b, w = pix[x, y]
#             r_list.append(r)
#             g_list.append(g)
#             b_list.append(b)
#     L = len(r_list)
#     i = 0
#     while i <= L:
#         if r_list[i] > 2.5 * r_list[i + 1] and g_list[i] > 2.5 * g_list[i + 1] and b_list[i] > 2.5 * b_list[i + 1]:
#             distance = int(i / height)
#             return distance
#         i += 1
#
#
# def get_tracks(distance):
#     distance += 20  # 先滑过一点，最后再反着滑动回来
#     v = 0
#     t = 0.2
#     forward_tracks = []
#
#     current = 0
#     mid = distance * 3 / 5
#     while current < distance:
#         if current < mid:
#             a = 2
#         else:
#             a = -3
#
#         s = v * t + 0.5 * a * (t ** 2)
#         v = v + a * t
#         current += s
#         forward_tracks.append(round(s))
#
#     # 反着滑动到准确位置
#     back_tracks = [-3, -3, -2, -2, -2, -2, -2, -1, -1, -1]  # 总共等于-20
#
#     return {'forward_tracks': forward_tracks, 'back_tracks': back_tracks}
#
#
# def crack(driver):  # 破解滑动认证
#     # 1、点击按钮，得到没有缺口的图片
#     # button = driver.find_element_by_class_name('geetest_radar_tip')
#     # button.click()
#
#     # 2、获取没有缺口的图片
#     # image1 = get_smallimg(driver)
#     # print(image1)
#
#     # 3、点击滑动按钮，得到有缺口的图片
#     # button = driver.find_element_by_class_name('geetest_slider_button')
#     # button.click()
#
#     # 4、获取有缺口的图片
#     image2 = get_bigimg(driver)
#     print(image2)
#     # 5、对比两种图片的像素点，找出位移
#     distance = get_distance(driver)
#     print(distance)
#
#     # 6、模拟人的行为习惯，根据总位移得到行为轨迹
#     tracks = get_tracks(distance)
#     print(tracks)
#
#     # 7、按照行动轨迹先正向滑动，后反滑动
#     button = driver.find_element_by_xpath('//*[@class="JDJRV-slide-left"]')
#     ActionChains(driver).click_and_hold(button).perform()
#
#     # 正常人类总是自信满满地开始正向滑动，自信地表现是疯狂加速
#     for track in tracks['forward_tracks']:
#         ActionChains(driver).move_by_offset(xoffset=track, yoffset=0).perform()
#
#     # 结果傻逼了，正常的人类停顿了一下，回过神来发现，卧槽，滑过了,然后开始反向滑动
#     time.sleep(0.5)
#     for back_track in tracks['back_tracks']:
#         ActionChains(driver).move_by_offset(xoffset=back_track, yoffset=0).perform()
#
#     # 小范围震荡一下，进一步迷惑极验后台，这一步可以极大地提高成功率
#     ActionChains(driver).move_by_offset(xoffset=-3, yoffset=0).perform()
#     ActionChains(driver).move_by_offset(xoffset=3, yoffset=0).perform()
#
#     # 成功后，骚包人类总喜欢默默地欣赏一下自己拼图的成果，然后恋恋不舍地松开那只脏手
#     time.sleep(0.5)
#     ActionChains(driver).release().perform()
#
#
# def login_cnblogs(username, password):
#     driver = webdriver.Chrome()
#     try:
#         # 1、输入账号密码回车
#         # driver.implicitly_wait(3)
#         # driver.get('https://passport.cnblogs.com/user/signin')
#         login_url = 'https://sz.jd.com/'
#         driver.get(login_url)
#         login_element = driver.find_element_by_xpath('//*[@class="header"]/div')
#         login_element.click()
#         driver.implicitly_wait(10)
#         iframe = driver.find_element_by_id('dialogIframe')
#         driver.switch_to.frame(iframe)
#         login_method = driver.find_element_by_xpath('//*[@class="login-form"]/div[2]')
#         login_method.click()
#         user = driver.find_element_by_id("loginname")
#         pwd = driver.find_element_by_id("nloginpwd")
#         login_button = driver.find_element_by_xpath('//*[@class="login-btn"]')
#         # while True:
#         user.clear()
#         pwd.clear()
#         user.send_keys(username)
#         pwd.send_keys(password)
#         login_button.click()
#         time.sleep(2)
#         # smallimg = driver.find_element_by_xpath('//*[@class="JDJRV-smallimg"]/img')
#         # bigimg = driver.find_element_by_xpath('//*[@class="JDJRV-bigimg"]/img')
#         # slide = driver.find_element_by_xpath('//*[@class="JDJRV-slide-left"]')
#         # 2、破解滑动认证
#         crack(driver)
#         time.sleep(10)  # 睡时间长一点，确定登录成功
#
#     finally:
#         driver.close()
#
#
# if __name__ == '__main__':
#     login_cnblogs(username='12341234', password='13434122343')
#
