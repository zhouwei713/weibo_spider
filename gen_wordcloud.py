# coding = utf-8
"""
@author: zhou
@time:2019/8/1 18:45
@File: gen_wordcloud.py
"""

import jieba
import pandas as pd
from wordcloud import WordCloud
import numpy as np
from PIL import Image


font = r'C:\Windows\Fonts\FZSTK.TTF'
STOPWORDS = {"回复", }


def wordcloud(file, name, pic=None):
    df = pd.read_csv(file, usecols=[1])
    df_copy = df.copy()
    df_copy['comment'] = df_copy['comment'].apply(lambda x: str(x).split())  # 去掉空格
    df_list = df_copy.values.tolist()
    comment = jieba.cut(str(df_list), cut_all=False)
    words = ' '.join(comment)
    img = Image.open(pic)
    img_array = np.array(img)
    wc = WordCloud(width=2000, height=1800, background_color='white', font_path=font, mask=img_array,
                   stopwords=STOPWORDS, contour_width=3, contour_color='steelblue')
    wc.generate(words)
    wc.to_file(name + '.png')


if __name__ == '__main__':
    # wordcloud("1573790059comment.csv", "lixiaolu3", 'xinsui.jpg')
    wordcloud("1573796702comment.csv", "guozu", 'ciyun.jpg')
