from typing import NoReturn

import pytest

from hocho.tokenizer.impl import MeCabTokenizer


class TestMeCabTokenizer:
    class Test_生成について:
        def test_システム辞書ファイルパスとユーザー辞書ファイルパス指定でMeCabトーカナイザーを生成できる(self) -> NoReturn:
            try:
                MeCabTokenizer('', '')
            except Exception:
                pytest.fail('This code should be executed.')

    class Test_wakatiメソッドについて:
        def test_文字列指定で分かち書きする(self) -> NoReturn:
            tokenizer = MeCabTokenizer('', '')
            assert ['私', 'の', '名前', 'は', '佐藤', '太郎', 'です', '。'] == tokenizer.wakati('私の名前は佐藤太郎です。')
