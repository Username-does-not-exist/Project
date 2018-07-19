from selenium import webdriver


class Driver(object):

    def __init__(self):
        pass

    def driver():
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        return driver


if __name__ == '__main__':
    driver = Driver()