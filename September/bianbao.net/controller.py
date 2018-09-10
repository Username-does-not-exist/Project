import requests
from lxml import etree


def construct():
    url_list = []
    for i in range(1, 12):
        url = "http://www.bianbao.net/sdList_page{}.html".format(i)
        url_list.append(url)
    return url_list


def get_company_url(url):
    response = requests.get(url)
    content = response.text
    html = etree.HTML(content)
    node_list = html.xpath('//*[@class="business_info"]/div/a/@href')
    company_url_list = []
    for node in node_list:
        company_url_list.append(node)
    return company_url_list


def save_url(company_url_list):
    for company_url in company_url_list:
        pass


def main():
    url_list = construct()
    print(url_list.__len__())
    for url in url_list:
        company_url_list = get_company_url(url)
        save_url(company_url_list)


