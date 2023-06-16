from util.nlp_client import *
import jieba.analyse

# 获取jieba自带的停用词列表
stopwords = jieba.analyse.DEFAULT_STOP_WORDS

# 打印停用词列表
for word in stopwords:
    print(word)