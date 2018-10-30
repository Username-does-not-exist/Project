# from PIL import Image
# import os
#
#
# def get_captcha():
#     # 获取验证码图片上每一个像素点的RGB值
#     path = os.path.abspath(os.getcwd())
#     folder = path + "\\captcha"
#     image = Image.open(folder + '\\background06.png', )
#     pix = image.load()
#
#     width = image.size[0]
#     height = image.size[1]
#     print(width, height)
#     print("--------------")
#     piexl = []
#     coordinate = []
#     for x in range(width):
#         for y in range(height):
#             r, g, b, w = pix[x, y]
#             RGB = [r, g, b]
#             cdte = [x, y]
#             piexl.append(RGB)
#             coordinate.append(cdte)
#     info = []
#     for co, pi in zip(coordinate, piexl):
#             obj = {"cor": co, "pie": pi}
#             info.append(obj)
#     # 打印图片像素点个数
#     # print(len(info))
#     li = [info[i:i + 360] for i in range(0, len(info), 360)]
#     # 打印宽度为一像素长度为360的像素线的条数
#     # print(len(li))
#     info_list = list()
#     # 遍历像素列表 找出符合条件的像素点
#     confirm_piexl_list = list()
#     for i in range(len(li)):
#         line = li[i]
#         # 打印每一条像素线
#         # print(line)
#         co_line_list = []
#         for j in line:
#             # 打印每一个像素点的坐标以及及RGB值
#             # print(j)
#             m = j['cor']
#             n = j['pie']
#             if n[0] < 89 and n[1] < 89 and n[2] < 89:
#                 confirm_piexl_list.append(j)
#                 info_list.append(m)
#     # 从RGB值均小于89的像素点中筛选出符合条件的像素点的坐标
#     nodes = []
#     for idx in range(len(info_list)):
#         x1 = info_list[idx][0]
#         y1 = info_list[idx][1]
#         A = [x1, y1]
#         # print(info_list[idx])
#         Ruler = idx + 1
#         for Ruler in range(len(info_list)):
#             x2 = info_list[Ruler][0]
#             y2 = info_list[Ruler][1]
#             B = [x2, y2]
#             if x2-x1 == 39 and y2-y1 == 39:
#                 # print("符合条件的两个点坐标分别为({},{}),({},{})".format(x1, y1, x2, y2))
#                 nodes.append(A)
#                 nodes.append(B)
#                 break
#     for node in nodes:
#         for idex in info_list:
#             # print(node[1], idex[1])
#             if node[0] + 37 == idex[0] and node[1] == idex[1]:
#                 print(idex)
#
#     # (138,130),(99,91)
#             # print("坐标({},{})处的像素 - 红:{},绿:{},蓝:{}".format(x, y, r, g, b))
#             # r_list.append(r)
#             # g_list.append(g)
#             # b_list.append(b)
#     # lines = list()
#     # for r, g, b in zip(r_list, g_list, b_list):
#     #     # 每一个字典装一个像素点的RGB值
#     #     RGB = dict()
#     #     RGB['R'] = r
#     #     RGB['G'] = g
#     #     RGB['B'] = b
#     #     lines.append(RGB)
#     # # 将li里的像素分割成140条宽度为一个像素，长度为360个像素的直线
#     # li = [lines[i:i + 360] for i in range(0, len(lines), 360)]
#     # for i in range(len(li)):
#     #     line = li[i]
#     #     slide = []
#     #     # 遍历每一条宽度为一像素的线 判定每一个像素点是否符合条件
#     #     for j in line:
#     #         if j['R'] < 89 and j['G'] < 89 and j['B'] < 89:
#     #             # 如果调价符合 将元素添加到slide
#     #             slide.append(j)
#
#
# if __name__ == '__main__':
#     get_captcha()


a_str = """单电 微单相机 单反相机 摄像机 拍立得 运动相机 镜头 户外器材 影棚器材 冲印服务 数码相框
存储卡 读卡器 滤镜 闪光灯 手柄 相机包 三脚架 云台 相机清洁 贴膜 机身附件 镜头附件 电池 充电器 移动电源 数码支架
智能手环 智能手表 智能眼镜 运动跟踪器 健康监测 智能配饰 智能家居 体感车 其他配件 智能机器人 无人机
MP3 MP4 智能设备 耳机 耳麦 便携 无线音箱 音箱 音响 高清播放器 收音机 麦克风 专业音频 苹果配件
学生平板 点读机 笔 录音笔 电纸书 电子词典 复读机"""

b_str = a_str.replace(' ', ',')
li = b_str.split(',')
print(li)
