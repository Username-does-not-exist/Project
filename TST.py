# distract = ['http://www.feijiu.net/FeiZhi/a1g1/', 'http://www.feijiu.net/FeiZhi/a2g1/', 'http://www.feijiu.net/FeiZhi/a3g1/', 'http://www.feijiu.net/FeiZhi/a4g1/', 'http://www.feijiu.net/FeiZhi/a5g1/', 'http://www.feijiu.net/FeiZhi/a6g1/', 'http://www.feijiu.net/FeiZhi/a7g1/', 'http://www.feijiu.net/FeiZhi/a8g1/', 'http://www.feijiu.net/FeiZhi/a9g1/', 'http://www.feijiu.net/FeiZhi/a10g1/', 'http://www.feijiu.net/FeiZhi/a11g1/', 'http://www.feijiu.net/FeiZhi/a12g1/', 'http://www.feijiu.net/FeiZhi/a13g1/', 'http://www.feijiu.net/FeiZhi/a14g1/', 'http://www.feijiu.net/FeiZhi/a15g1/', 'http://www.feijiu.net/FeiZhi/a16g1/', 'http://www.feijiu.net/FeiZhi/a17g1/', 'http://www.feijiu.net/FeiZhi/a18g1/', 'http://www.feijiu.net/FeiZhi/a19g1/', 'http://www.feijiu.net/FeiZhi/a20g1/', 'http://www.feijiu.net/FeiZhi/a21g1/', 'http://www.feijiu.net/FeiZhi/a22g1/', 'http://www.feijiu.net/FeiZhi/a23g1/', 'http://www.feijiu.net/FeiZhi/a24g1/', 'http://www.feijiu.net/FeiZhi/a25g1/', 'http://www.feijiu.net/FeiZhi/a26g1/', 'http://www.feijiu.net/FeiZhi/a27g1/', 'http://www.feijiu.net/FeiZhi/a28g1/', 'http://www.feijiu.net/FeiZhi/a29g1/', 'http://www.feijiu.net/FeiZhi/a30g1/', 'http://www.feijiu.net/FeiZhi/a31g1/', 'http://www.feijiu.net/FeiZhi/a32g1/', 'http://www.feijiu.net/FeiZhi/a33g1/', 'http://www.feijiu.net/FeiZhi/a34g1/']
# for url in distract:
#     print(url)
# print(len(distract))
import re

a_str = "http://wse888.fengj.com/detail/39363/info_39363011.html"


b_str = re.findall('http://\w+.fengj.com/detail/\d+/info_\d+.html', a_str)[0]

print(b_str)