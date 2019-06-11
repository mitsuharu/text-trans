import os
import sys
import random
import string
import seaborn as sns
import matplotlib.pyplot as plt

sys.path.append("../")

from texttrans.texttrans import TextTrans

en_file = "en_words.txt"
en_path = os.path.join(os.path.dirname(__file__), en_file)


def load_jr_high_school_en_words():
    print("load_jr_high_school_en_words")
    with open(en_path, "r") as f:
        for word in f.readlines():
            temp = word.strip()
            print(temp)
            yield temp


def load_random_en_words():

    count = sum(1 for _ in open(en_path))
    min_len = 3
    max_len = 6

    for _ in range(count):

        length = random.randint(min_len, max_len)
        rnd_str = ''.join(random.choices(string.ascii_letters, k=length))
        rnd_str = rnd_str.lower()

        yield rnd_str


def main():

    tt = TextTrans()

    correct_p = []
    for w in load_jr_high_school_en_words():
        print(w)
        correct_p += [tt.prob(w)]

    rand_p = []
    for w in load_random_en_words():
        print(w)
        rand_p += [tt.prob(w)]

    ax = sns.distplot(correct_p, kde=True)
    ax = sns.distplot(rand_p, ax=ax, kde=True)
    ax.set_xlim([0, 0.2])
    ax.set_xlabel("text transition prob")
    ax.legend(labels=['correct_en_words', 'random_en_words'])
    plt.show()


if __name__ == '__main__':
    main()
