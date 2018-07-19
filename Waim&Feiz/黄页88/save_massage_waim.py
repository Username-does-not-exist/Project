import re
import sys
sys.path.append('./')
from multiprocessing import Process, Queue



    def get_url( q):
        urls = rConn.hgetall('url_88wm')
        for i in urls:
            url = i.decode('utf-8')
            q.put(url)

    def translate( li, result):
        """
        解析数据
        :param li:
        :param result:
        :return:
        """

        a = str(li)
        a_str = a.replace('[', '').replace(']', '').replace("'", '')

        a_list = a_str.split("：")
        b_list = list()
        for i in a_list:
            li = i.split('\\n')
            for i in li:
                j = i.replace('', '')
                b_list.append(j)

        c_list = list()
        for i in b_list:
            if i == '':
                pass
            else:
                c_list.append(i)

        for i in c_list:
            try:
                item1 = re.findall(result, i)[0]
                item2 = c_list.index(item1)
                num = item2 + 1
                company = c_list[num]
                return company
            except:
                pass

    def get_data( q):
        """
        获取数据
        :param url:
        :param proxy:
        :return:
        """
        url = q.get()
        driver.get(url)
        driver.implicitly_wait(10)
        button = driver.find_element_by_xpath('//*[@class="meun"]/a[last()]|//*[@class="navigation"]/ul/li[last()]|//*[@class="nav"]/ul/li[last()-1]|//*[@class="vip_nav"]//li[3]')
        button.click()
        driver.implicitly_wait(5)
        data_list =start.driver.find_elements_by_xpath('//*[@class="site"]/ul|//*[@class="contact-text"]|//*[@class="address"]/ul|//*[@class="co_Details cf"]')
        massage = list()
        for data in data_list:
            item = data.text
            massage.append(item)

        items = dict()
        items['company'] = translate(massage, "公司名称")
        items['contact'] = translate(massage, '联系人')
        items['mobile'] = translate(massage, '移动电话')
        if items['mobile'] == None:
            items['mobile'] = translate(massage, "手机")
            if items['mobile'] == None:
                items['mobile'] = translate(massage, "手机号")

        items['number'] = translate(massage, '公司电话')
        if items['number'] == None:
            items['number'] = translate(massage, '电话')
        items['address'] = translate(massage, '公司地址')
        if items['address'] == None:
            items['address'] = translate(massage, '地址')
        items['wechat'] = translate(massage, '微信')
        if items['wechat'] == None:
            items['wechat'] = translate(massage, '微信咨询')
        items['qq'] = translate(massage, 'QQ')
        if items['qq'] == None:
            items['qq'] = translate(massage, "QQ咨询")
        items['fax'] = translate(massage, '传真')
        if items['fax'] == None:
            items['fax'] = translate(massage, '公司传真')
        items['post_number'] = translate(massage, "邮编")
        if items['post_number'] == None:
            items['post_number'] = translate(massage, "公司邮编")

        q.put(items)

    def save_data( q):
        """
        保存数据
        :param data:
        :return:
        """
        try:
            data = q.get()
            db = conn.hy88_wm3
            col = db.fz
            if data['contact'] == None:
                pass
            else:
                col.insert(data)
                count = col.count()
                print(data)
                print("<|---------------=================----------------|>")
                print("当前已抓取{}条数据".format(count))
        except Exception as e:
            print(e)

    def main(self):
        q = Queue()
        pool = list()
        p1 = Process(target=get_url, args=(q,))
        p2 = Process(target=get_data, args=(q,))
        p3 = Process(target=save_data, args=(q,))
        pool.append(p1)
        pool.append(p2)
        pool.append(p3)
        for i in pool:
            i.start()
            i.join()


# if __name__ == '__main__':
#     w = Waim()
#     w.main()



