import abc


class Tokenizer(abc.ABC):
    @abc.abstractmethod
    def wakati(self, sent):
        pass

    @abc.abstractmethod
    def wakati_baseform(self, sent):
        pass

    @abc.abstractmethod
    def tokenize(self, text):
        pass

    @abc.abstractmethod
    def filter_by_pos(self, sent, pos=('名詞',)):
        pass
