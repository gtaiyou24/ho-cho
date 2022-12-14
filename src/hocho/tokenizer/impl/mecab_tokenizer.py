import MeCab

from collections import namedtuple

from hocho.tokenizer import Tokenizer


class MeCabTokenizer(Tokenizer):

    def __init__(self, sys_dic_path='', user_dic_path=''):
        """
        システム辞書のパス、ユーザー辞書パス指定でMeCabトーカナイザーを生成できる。

        :param sys_dic_path:
        :param user_dic_path:
        """
        option = ''
        if sys_dic_path:
            option += ' -d {0}'.format(sys_dic_path)
        if user_dic_path:
            option += ' -u {0}'.format(user_dic_path)
        self._t = MeCab.Tagger(option)

    def wakati(self, sent):
        words = [token.surface for token in self.tokenize(sent)]
        return words

    def wakati_baseform(self, sent):
        words = [token.base_form if token.base_form != '*' else token.surface
                 for token in self.tokenize(sent)]
        return words

    def tokenize(self, text):
        self._t.parse('')
        chunks = self._t.parse(text.rstrip()).splitlines()[:-1]  # Skip EOS
        # surface : 形態素(単語)
        # pos : 品詞
        token = namedtuple('Token', 'surface, pos, pos_detail1, pos_detail2, pos_detail3,\
                                                                         infl_type, infl_form, base_form, reading, phonetic')
        for chunk in chunks:
            if chunk == '':
                continue
            surface, feature = chunk.split('\t')
            feature = feature.split(',')
            if len(feature) <= 7:  # 読みがない
                feature.append('')
            if len(feature) <= 8:  # 発音がない
                feature.append('')
            yield token(surface, *feature)

    def filter_by_pos(self, sent, pos=('名詞',)):
        tokens = [token for token in self.tokenize(sent) if token.pos in pos]
        return tokens
