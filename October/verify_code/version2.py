import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from PIL import Image
import time


def get_snap(driver):
    driver.save_screenshot('full_snap.png')
    page_snap_obj = Image.open('full_snap.png')
    return page_snap_obj


def get_bigimg(driver):
    captcha_url = driver.find_element_by_xpath('//*[@class="JDJRV-bigimg"]/img').get_attribute('src')
    from selenium import webdriver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome = webdriver.Chrome(chrome_options=chrome_options)
    chrome.get(captcha_url)
    captcha = chrome.find_element_by_xpath('//img')
    # 获取验证码坐标
    left = captcha.location['x']
    top = captcha.location['y']
    right = captcha.location['x'] + captcha.size['width']
    bottom = captcha.location['y'] + captcha.size['height']
    # 获取图片截图
    page_snap_obj = get_snap(chrome)
    im_obj = page_snap_obj.crop((left, top, right, bottom))
    return im_obj


def get_distance(image):
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


def get_tracks(distance):
    # 移动轨迹
    import random
    print(distance)
    # distance -= 25
    print("==========")
    print(distance)
    track = []
    n = 0
    while True:
        m = random.randint(0, 5)
        track.append(m)
        n += m
        if n >= distance:
            break
    if n == distance:
        return track
    else:
        de_distance = n - distance
        l = len(track)
        last = l - 1
        track[last] = de_distance
        return track


def crack(driver):  # 破解滑动认证
    # 1、获取有缺口的图片
    image = get_bigimg(driver)

    # 2、对比两种图片的像素点，找出位移
    distance = get_distance(image)
    print("缺口到图片最左边距离为{}像素".format(distance))

    # 3、模拟人的行为习惯，根据总位移得到行为轨迹
    tracks = get_tracks(distance)

    # 4、按照行动轨迹先正向滑动，后反滑动
    button = driver.find_element_by_xpath('//*[@class="JDJRV-slide-left"]')
    ActionChains(driver).click_and_hold(button).perform()

    # 5.正常人类总是自信满满地开始正向滑动，自信地表现是疯狂加速
    for track in tracks:
        ActionChains(driver).move_by_offset(xoffset=track, yoffset=0).perform()

    # 6,结果傻逼了，正常的人类停顿了一下，回过神来发现，卧槽，滑过了,然后开始反向滑动
    # time.sleep(0.5)
    # for back_track in tracks['back_tracks']:
    #     ActionChains(driver).move_by_offset(xoffset=back_track, yoffset=0).perform()

    # 7.小范围震荡一下，进一步迷惑极验后台，这一步可以极大地提高成功率
    ActionChains(driver).move_by_offset(xoffset=-3, yoffset=0).perform()
    ActionChains(driver).move_by_offset(xoffset=3, yoffset=0).perform()

    # 8.成功后，骚包人类总喜欢默默地欣赏一下自己拼图的成果，然后恋恋不舍地松开那只脏手
    time.sleep(0.1)
    ActionChains(driver).release().perform()


def login_cnblogs(username, password):
    driver = webdriver.Chrome()
    try:
        # 1、输入账号密码回车
        login_url = 'https://sz.jd.com/'
        driver.get(login_url)
        login_element = driver.find_element_by_xpath('//*[@class="header"]/div')
        login_element.click()
        driver.implicitly_wait(10)
        iframe = driver.find_element_by_id('dialogIframe')
        driver.switch_to.frame(iframe)
        login_method = driver.find_element_by_xpath('//*[@class="login-form"]/div[2]')
        login_method.click()
        user = driver.find_element_by_id("loginname")
        pwd = driver.find_element_by_id("nloginpwd")
        login_button = driver.find_element_by_xpath('//*[@class="login-btn"]')
        # 输入账号密码
        user.clear()
        pwd.clear()
        user.send_keys(username)
        pwd.send_keys(password)
        login_button.click()
        time.sleep(2)
        # 2、破解滑动认证
        crack(driver)
        path = os.path.abspath(os.getcwd())
        file = path + "\\full_snap.png"
        if os.path.exists(file):
            os.remove(file)
        time.sleep(10)  # 睡时间长一点，确定登录成功
    finally:
        pass
        driver.quit()


if __name__ == '__main__':
    login_cnblogs(username='12341234', password='13434122343')