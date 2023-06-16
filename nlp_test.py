from snownlp import SnowNLP
import jieba.analyse

from service.nlp import Nlp

s1 = '小妍妍喜欢这歌吗'
s2 = '愉快的时光总是短暂的'

nlp = Nlp()
print(nlp.get_keywords(s1))
print(nlp.get_keywords(s2))
print(nlp.get_keywords(s1+s2))
