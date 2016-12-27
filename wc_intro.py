#coding:utf-8
from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import jieba
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
sw1=['www','http','com','douban',u'在',u'是',u'人',u'的',u'不',u'也',u'我',u'自己',u'你',
u'喜欢',u'就',u'cn',u'有',u'会',u'就是',u'没有',u'都',u'和',u' ', u'-', u'/', u'，', u'.',
u'。', u'░', u'、', u':', u'\n', u'=', u'—', u'：', u'█', u'　', u'*', u'▓', u',', u'（', 
u'）', u'了', u')', u'(', u'》', u'《', u'！', u't', u'一个', u'~', u'+', u'·', u'_', u'★', 
u'与', u'我们', u'…', u'“', u'世界', u"'", u'；', u'■', u'”', u'↔', u'做', u'中', u'weibo', 
u'【', u'好', u'】', u'去', u'|', u'微博', u'对', u'而', u'I', u'什么', u'上', u'～', u'？', 
u'请', u'这', u'但', u'说', u'很', u'想', u'看', u'可以', u'不是', u'要', u'号', u'•', u'blog', 
u'豆瓣', u'着', u'多', u'如果', u'能', u'他', u'大师', u'关注', u'被', u'1', u'公众', u'不要', 
u'为', u'?', u'＝', u'&', u'因为', u'还', u'里', u'https', u'她', u'个', u'知道', u'又', 
u'让', u'到', u'地址', u'这个', u'那', u'年', u'"', u'小', u'最', u'给', u'@', u'像', 
u'它', u'把', u'更', u'之', u'所有', u'来', u'只是', u'大', u's', u'3', u'时候', u'还是', 
u'一切', u'却', u'一样', u'#', u'别人', u'The', u'→', u'过', u'一起', u'2', u'后', u'sina', 
u'事',  u'%', u'并', u'↑', u'不能', u'啊', u'吧', u'只', u'¨', u'地', u'▽', u'等', u'裏', 
u'写', u'得', u'≈', u'东西', u'这样', u'已经', u'╯', u'▶', u'√', u'没', u'无', u'!', u'其实', 
u'所以', u'不会', u'一种',  u'谁', u'或者', u'♥', u'只有', u'月', u'5', u'任何', u'地方', u'一',  
u'╰', u'group', u'bz', u'事情', u'site', u'dou', u'或', u'日', u'>', u'\r',u'\t',u'微信',u'新浪',
u'photos',u'需要',u'男', u'时', u'才', u'当', u'╭', u'那么', u'一直', u'他们', u'听', u'❤', u'╮', u'比', u'↓', u'觉得', 
u'Hong', u'」', u'〓', u'为了', u'再', u'走', u'用', u'Kong', u'可能', u'可', u'问题', u'你们', 
u'一次', u'年度', u'者', u'于', u'死', u'站', u'’', u'讨厌', u'subject', u'一些', u'心', 
u'「', u'u',  u'跟', u'但是', u'下', u'便', u'太', u'已', u'每个',u'...', u'叫', u'这里', u'很多', 
u'如', u'那个', u'想要', u'将', u'以', u'从', u'新', u'逼', u'－', u'━', u'4', u'那些', u'๑', 
u'带', u'应该', u'然后', u'如此', u'所', u'一定', u'无法', u'm', u'□', u'lofter', u'吗', 
u'呢', u'这些', u'♡', u';', u'吃', u'8', u'￣', u'相册', u'每', u'真的', u'7', u'自', 
u'doulist', u'各种', u'You', u'找到', u'每天', u'感觉', u'偶尔', u'小站', u'6', u'转载', 
u'X', u'女', u'[', u']', u'也许', u'加', u"\\", u'最后', u'不过', u'profile', u'以及', 
u'✂', u'起来', u'有人', u'＊', u'城市', u'容易', u'é', u'´', u'老', u'能够', u'●', u'爱好', 
u'非常', u'子', u'真正', u'了解', u'方式', u'由', u'拍', u'┃', u'更新', u'°', u'一只', 
u'关于', u'总是', u'别', u'真', u'平台', u'one', u'前', u'这么', u'9', u'女性', u'职业', 
u'以后', u'☠', u'And', u'', u'MAO', u'ID', u'我会', u'正', u'豆油', u'QQ', u'姑娘', 
u'丨', u'这是', u'认识', u'而是', u'net', u'淘宝', u'特别', u'可是', u'话', u'亦', u'注明', 
u'一条', u'推荐', u'找', u'变得', u'html', u'学', u'✿', u'您', u'event', u'̿', u'ω', u'只要', 
u'取消', u'重要', u'0', u'使', u'终于', u'系列', u'♣', u'不再', u'©', u'instagram', u'除了', 
u'目标', u'男人', u'◆', u'名字', u'作者',  u'开始', u'即使', u'其他', u'完', u'之间', u'不好', 
u'作为',  u'点', u'分享', u'若', u'A', u'账号', u'还有', u'只能', u'ღ', u'哦', u'º', u'曾', 
u'出', u'性别', u'鸟', u'起', u'id', u'一枚', u'变成', u'有些', u'topic',]
sw=STOPWORDS|set(sw1)

text = open(path.join(d, 'intro.txt')).read()
# jieba.analyse.set_stop_words('stopwords.txt') 
seg_list = jieba.cut(text)  # 默认是精确模式
txt_dic={}
for x in seg_list:
    if x in sw:
        continue
    if txt_dic.has_key(x):
        txt_dic[x]+=1
    else:
        txt_dic[x]=1
txt_freq= sorted(txt_dic.iteritems(), key=lambda d:d[1], reverse = True)
txt_freq=txt_freq[:1000]
txt_freq=tuple(txt_freq)
xx=0
for x in txt_freq:
    print "u'"+x[0]+"'"+",",
    if xx>400:
        break
    xx+=1
# read the mask / color image
# taken from http://jirkavinse.deviantart.com/art/quot-Real-Life-quot-Alice-282261010
# 设置背景图片
alice_coloring = imread(path.join(d, "a.png"))
wc = WordCloud(font_path="/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",background_color="white", #背景颜色max_words=2000,# 词云显示的最大词数
mask=alice_coloring,#设置背景图片
stopwords=sw,
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
