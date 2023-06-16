from snownlp import SnowNLP
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer


def get_n_words(s):
    return [w[0] for w in SnowNLP(s).tags if w[1] == 'n']


def get_a_words(s):
    return [w[0] for w in SnowNLP(s).tags if w[1] == 'a']



