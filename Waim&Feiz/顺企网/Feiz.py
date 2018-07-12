"""
项目准备
用requests抓取
两个类别的数据个一千条 共两千条
http://b2b.11467.com/search/-59168d38670d9970.htm

详情页url对应的xpath
//*[@class="companylist"]/li/div[2]/h4/a/@href
下一页url对应的url
url_list = list()

for i in range(1,21):
url = "http://b2b.11467.com/search/-5e9f7eb8-pn{}.html".format(i)
url_list.append(url)
return url_list


信息提取 xpath
公司名称 //*[@class="boxcontent"]/table//tr[1]/td[2]
联系人	//*[@class="boxcontent"]/dl/dd[3]
联系人电话号码 //*[@class="boxcontent"]/dl/dd[4]
固定电话 //*[@class="boxcontent"]/dl/dd[2]
邮政编码 //*[@class="boxcontent"]/dl/dd[5]
传真号码 //*[@class="boxcontent"]/dl/dd[6]
公司地址 //*[@class="boxcontent"]/dl/dd[1]

"""
class FeiZ(object):

    def __init__(self):
        pass

    def get_page_url(self):
        """
        构建需要抓取的页面的url列表
        :return:
        """
        url_list = list()

        for i in range(1, 21):
            url = "http://b2b.11467.com/search/-5e9f7eb8-pn{}.html".format(i)
            url_list.append(url)
        return url_list

    def get_detail_url(self):
        """
        获取详情页的url
        :return:
        """
        pass

    def get_data(self):
        """
        提取数据
        :return:
        """
    def save_data(self):
        """
        保存数据
        :return:
        """
    def main(self):
        """
        处理主要逻辑
        :return:
        """


if __name__ == '__main__':
    fz = FeiZ()
    fz.main()



















