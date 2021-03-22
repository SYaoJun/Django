import sys
from sys import path

import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
filename = "my_text.txt"
with open(filename, 'r', encoding='UTF-8') as f:
    mytext = f.read()
from PIL import Image

football = np.array(Image.open("yyqx.jpg"))
font = r'C:\Windows\Fonts\simfang.ttf'
wc = WordCloud(collocations=False, font_path=font,mask=football, width=1400, height=1400, margin=2).generate(mytext.lower())
plt.imshow(wc)
plt.axis("off")
plt.show()

# wc.to_file('show_Chinese.png')  # 把词云保存下来