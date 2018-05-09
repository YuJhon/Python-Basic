#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'jiangy19'
__mtime__ = '2018/5/7'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
d = path.dirname(__file__)
# 读文本文件
text = open(path.join(d, 'data.txt')).read()
# 读取自定义图片
alice_coloring = np.array(Image.open(path.join(d, "turtle.png")))
# 你可以通过 mask 参数 来设置词云形状
wc = WordCloud(background_color="white",max_words=2000,
                mask=alice_coloring, max_font_size=60,random_state=102,scale=8,
                font_path="./opensans.ttf").generate(text)
wc.generate_from_text(text)
print('加载文本')
# 改变字体颜色
img_colors = ImageColorGenerator(alice_coloring)
# 字体颜色为背景图片的颜色
wc.recolor(color_func=img_colors)
# 显示词云图
plt.imshow(wc, interpolation="bilinear")
# 是否显示x轴、y轴下标
plt.axis('off')
plt.show()
# 获得模块所在的路径的
d = path.dirname(__file__)
# 将多个路径组合后返回
wc.to_file(path.join(d, "h16.jpg"))
print('生成词云成功!')