import re

# li = ['公司名称：常州力马干燥科技有限公司 (营业执照已认证)\n公司地址：江苏 常州 常州市天宁区东青和平工业园\n公司邮编：213000\n公司传真：0519-88968686\n公司主页：http://www.chinalemar.com/\n联系人：周经理 （实名已验证）\n公司电话：0519-88968880-881\n移动电话：18136711288']
# result = "公司传真"
"""
li 一个待提取的列表
result 需要提取的信息
"""


def translate(li, result):

    a = str(li)
    a_str = a.replace('[', '').replace(']', '').replace("'",'')

    a_list = a_str.split("：")
    b_list = list()
    for i in a_list:
        li = i.split('\\n')
        for i in li:
            j = i.replace('', '')
            b_list.append(j)
    print(b_list)

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


# a = translate(li, result)
# print(a)
