from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt  #绘制图像的模块
import jieba                    #jieba分词
import numpy as np

path_txt='nuc.txt'
f = open(path_txt,'r',encoding='UTF-8').read()

# 结巴分词，生成字符串，wordcloud无法直接生成正确的中文词云

mask = np.array(Image.open("nuc.png"))
cut_text = " ".join(jieba.cut(f))

wordcloud = WordCloud( mask=mask, font_path="C:/Windows/Fonts/simfang.ttf", background_color="white",width=1000,height=880).generate(cut_text)

plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()