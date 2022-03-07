import pytest

@pytest.mark.parametrize("word, prob", [
    ('pen', 0.11640052876679541),
    ('apple', 0.07209677370095303),
])
def test_hello(word, prob):
    from .texttrans import TextTrans
    tp = TextTrans()
    assert tp.prob(word) == prob
