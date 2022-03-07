import pickle
import pytest

@pytest.mark.parametrize("word, prob", [
    ('pen', 0.11640052876679541),
    ('apple', 0.07209677370095303),
])
def test_simple_char_transition_prob(word, prob):
    from .texttrans import TextTrans
    tp = TextTrans()
    assert tp.prob(word) == prob


@pytest.mark.parametrize("word, ngram", [
    ('apple', [('a', 'p'), ('p', 'p'), ('p', 'l'), ('l', 'e'), ('e', '\x00')]),
])
def test_sublines_for_ngram(word, ngram):
    from .texttrans import TextTrans
    tp = TextTrans()
    t = [x for x in tp.sublines_for_ngram(word)]
    assert t == ngram

def test_load_model():
    """""
    必要なデータ構造は以下
    mat: dict(key=遷移元alphabet, val=dict(key=遷移先alphabet, val=遷移確率))
    non_pattern_prob: 元データから遷移確率が計算できなかった場合に利用する遷移確率
    ngram: 文字通り渡されたwordを何文字の組に分割するか
    """""

    d = pickle.load(open('../data/en.pki', 'rb'))
    print(d)

def test_train():
    """
    wordが1行に1つ入っているファイルを読み込み、遷移確率行列を作る
    """
    from .texttrans import TextTrans
    tp = TextTrans('../examples/en_words.txt')
    assert False
