import jieba
from jieba import analyse
import os
import wordcloud


class Cloud(object):

    def construct_words(self):
        words = ''
        article = os.listdir('./ReadBookAtTenClock')
        for title in article:
            with open('./ReadBookAtTenClock/{}'.format(title), 'rb') as f:
                content = f.read().decode('utf-8')
                a_str = jieba.cut(content, cut_all=False)
                b_str =''.join(a_str)
                c_str = b_str.replace('\\n', '')
                d_str = c_str.replace("本站收录只为方便网友在电脑端阅读微信最新最热门的文章及朋友圈热文", "")
                e_str = d_str.replace("免责声明微信公众号(www.wxnmh.com)本站文章均来自网友的提交", "")
                f_str = e_str.replace("不对原文做任何更改或添加，版权归原作者所有，如有权益问题请及时与我们联系(邮箱 : puttyroot?163.com(问号换成@))处理。返回", "")
                g_str = f_str.replace("本文首发十点读书，转载请在后台回复“转载”", "").replace("作者 十点读书", "").replace("不对原文做任何更改或添加，版权归原作者所有，如有权益问题请及时与我们联系(邮箱 : puttyroot?163.com(问号换���@))处理。返回", "")
                t1 = ''
                print(g_str)
                for i in g_str:
                    if i is not None:
                        t1 += i
            words += t1 + "<|-----|>"
        return words

    def words_to_image(self):
        font = './SIMYOU.TTF'
        words = self.construct_words()
        print(words)
        # keywords = analyse.extract_tags(words)
        # print(keywords)
        # word = wordcloud.WordCloud(collocations=False, font_path=font, width=4096, height=2160, margin=2)
        # word.generate(words)
        # word.to_file('./pic4.png')


if __name__ == '__main__':
    cloud = Cloud()
    cloud.words_to_image()
