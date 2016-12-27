#coding:utf-8
from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import jieba
import sys   
reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入   
sys.setdefaultencoding('utf-8') 
# 获取当前文件路径
# __file__ 为当前文件, 在ide中运行此行会报错,可改为
# d = path.dirname('.')
d = path.dirname(__file__)

# 读取文本 alice.txt 在包文件的example目录下
#内容为
"""
Project Gutenberg's Alice's Adventures in Wonderland, by Lewis Carroll

This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Project Gutenberg License included
with this eBook or online at www.gutenberg.org
"""
text = open(path.join(d, 'place.txt'))
txt_dic={}
for x in text:
    x=x[:len(x)-1]
    x=unicode(x)
    if txt_dic.has_key(x):
        txt_dic[x]+=1
    else:
        txt_dic[x]=1
txt_freq= sorted(txt_dic.iteritems(), key=lambda d:d[1], reverse = True)
txt_freq=txt_freq[:100]
txt_freq=tuple(txt_freq)
for x in txt_freq:
    print x[0],",",x[1]
text.close()
# read the mask / color image
# taken from http://jirkavinse.deviantart.com/art/quot-Real-Life-quot-Alice-282261010
# 设置背景图片
alice_coloring = imread(path.join(d, "a.png"))
wc = WordCloud(font_path="/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",background_color="white", #背景颜色max_words=2000,# 词云显示的最大词数
mask=alice_coloring,#设置背景图片
stopwords=None,
max_font_size=40, #字体最大值
random_state=42)

# 生成词云, 可以用generate输入全部文本(中文不好分词),也可以我们计算好词频后使用generate_from_frequencies函数
#wc.generate(text)
# txt_freq=[(u'词a', 500),(u'词b', 90),(u'词c', 8),('douban', 8)]
wc.generate_from_frequencies(txt_freq)
# 从背景图片生成颜色值
image_colors = ImageColorGenerator(alice_coloring)

# 以下代码显示图片
plt.imshow(wc)
plt.axis("off")
# 绘制词云
plt.figure()
# recolor wordcloud and show
# we could also give color_func=image_colors directly in the constructor
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis("off")
# 绘制背景图片为颜色的图片
plt.figure()
plt.imshow(alice_coloring, cmap=plt.cm.gray)
plt.axis("off")
plt.show()
# 保存图片
wc.to_file(path.join(d, "名称.png"))
