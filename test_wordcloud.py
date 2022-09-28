import jieba
import wordcloud

text = "A B C D E F G H J K"
words = jieba.lcut(text)
new_text = " ".join(words)
print(new_text)

wc = wordcloud.WordCloud(width=1920, height=1080, background_color="white", )
wc.generate(new_text)
wc.to_file("test_wordcloud.png")