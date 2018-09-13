"""
获取企业url对应的xpath://*[@id="list_item"]/div[1]/div/div/div[3]/h2/a

联系方式页面url = company_url + "contactusNews.aspx"


"""


class Crawl(object):

    def __init__(self):
        self.start_url = "http://www.feijiu.net/gq/s/g1p{}k%b7%cf%d6%bd/"

    def construct_url(self):
        url_list = []
        for i in range(1, 20):
            url = self.start_url.format(i)
            url_list.append(url)
        return url_list

    def get_company_url(self, url):
        """
        获取公司详情页联系方式的url
        :param url:
        :return:
        """

    def login_and_cookies(self):
        """
        处理登陆逻辑
        :return:
        """

    def get_contact_info(self, url, cookies):
        """
        获取公司信息
        :param url:
        :param cookies:
        :return:
        """

    def save_data(self, data, contact_info_picture):
        """
        保存数据
        :param data:
        :param contact_info_picture:
        :return:
        """

    def main(self):
        """
        处理抓取逻辑
        :return:
        """


if __name__ == '__main__':
    crawl = Crawl()
    crawl.main()