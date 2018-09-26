from selenium import webdriver
from PIL import Image
driver = webdriver.Firefox()
driver.get('https://mall.jd.com/shopLevel-43693.html')

driver.save_screenshot('bdbutton.png')
element = driver.find_element_by_xpath('//*[@class="verify"]/img')
print(element.location)                # 打印元素坐标
print(element.size)                    # 打印元素大小

left = element.location['x']
top = element.location['y']
right = element.location['x'] + element.size['width']
bottom = element.location['y'] + element.size['height']

im = Image.open('bdbutton.png')
im = im.crop((left, top, right, bottom))
im.save('bdbutton.png')