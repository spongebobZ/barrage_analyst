import jieba.analyse
import jieba

from config.file_config import FileConfig


class Nlp:
    def __init__(self):
        jieba.analyse.set_stop_words(FileConfig.stop_words_path)
        jieba.load_userdict(FileConfig.user_dict_path)
        self.all_user_sentences = dict()

    def get_keywords(self, u, s):
        if u in self.all_user_sentences:
            self.all_user_sentences[u] += '\n' + s
        else:
            self.all_user_sentences[u] = s
        return jieba.analyse.extract_tags(self.all_user_sentences[u], topK=5)
