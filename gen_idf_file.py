import jieba
import jieba.analyse
from sklearn.feature_extraction.text import TfidfVectorizer


def gen_idf_file(in_path, out_path, stop_words_path):
    jieba.analyse.set_stop_words(stop_words_path)

    with open(in_path, 'r', encoding='utf-8') as file:
        text = file.readlines()

    # 分词
    corpus = [' '.join(jieba.lcut(line.strip())) for line in text]

    # 计算TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)

    # 获取词汇表和IDF值
    vocabulary = vectorizer.get_feature_names_out()
    idf_values = vectorizer.idf_

    # 保存结果到文件
    with open(out_path, 'w', encoding='utf-8') as file:
        for word, idf in zip(vocabulary, idf_values):
            file.write(f'{word} {idf}\n')


if __name__ == '__main__':
    raw = r'doc/语料.txt'
    out = r'doc/idf.txt'
    stop_words = r'doc/stop_words.txt'
    gen_idf_file(raw, out, stop_words)
