import math
from collections import Counter, defaultdict
import re

TOKEN = re.compile(r'([^\W\d]+|\d+|[^\w\s])')


def re_tokenize(text):
    chunks = TOKEN.findall(text)
    return find_substrings(chunks, text)


def find_substrings(chunks, text):
    offset = 0
    for chunk in chunks:
        start = text.find(chunk, offset)
        stop = start + len(chunk)
        yield chunk
        offset = stop


class SimpleSearcher:
    def __init__(self, k=1.5, b=0.75, max_freq=None, df=False, ngram_range=None):
        self.k = k
        self.b = b
        self.max_freq = max_freq
        self.df = df
        self.ngram_range = ngram_range

        self.texts = []
        self.owners = []
        self.text_frequencies = {}
        self.inverse_index = {}
        self.wf = {}
        self.text_lengths = {}
        self.avg_len = 1
        self.n_docs = 0

    def tokenize(self, text, stem=None):
        text = text.lower()
        words = list(re_tokenize(text))
        if self.ngram_range is None:
            return words
        ngrams = [
            text[i:(i + n)]
            for n in range(self.ngram_range[0], self.ngram_range[1] + 1)
            for i in range(0, max(0, len(text) - n))
        ]
        return ngrams + words

    def setup(self, texts, owners):
        """ texts: list of texts, owners: list of ids """
        self.texts = texts
        self.owners = owners
        paragraphs = {i: text for i, text in enumerate(texts)}
        self.fit(paragraphs=paragraphs)
        return self

    def fit(self, paragraphs):
        """" paragraphs: dict with ids as keys and texts as values """
        inverse_index = defaultdict(set)
        text_frequencies = Counter()
        text_lengths = Counter()
        wf = Counter()
        for p_id, p in (paragraphs.items()):
            tokens = self.tokenize(p)
            text_lengths[p_id] = len(tokens)
            for w in tokens:
                wf[w] += 1
                if self.max_freq and wf[w] >= self.max_freq:
                    inverse_index[w] = set()
                else:
                    inverse_index[w].add(p_id)

        self.text_frequencies = text_frequencies
        self.inverse_index = inverse_index
        self.wf = wf
        self.text_lengths = text_lengths
        self.avg_len = sum(text_lengths.values()) / len(text_lengths)
        self.n_docs = len(paragraphs)

    def trim(self, n):
        # remove "stopwords" - words with too many indices
        stopwords = {k for k, v in self.inverse_index.items() if len(v) > n}
        for k in stopwords:
            self.inverse_index[k] = set()

    def get_okapi_idf(self, w):
        n = self.wf[w]
        return math.log(max(1, self.n_docs - n + 0.5) / (n + 0.5))

    def get_okapi_tf(self, w, p_id):
        f = self.text_frequencies[(p_id, w)] if self.df else 1
        return f * (self.k + 1) / (f + self.k * (1 - self.b + self.b * self.text_lengths[p_id] / self.avg_len))

    def get_tf_idfs(self, query) -> Counter:
        words = self.tokenize(query)
        matches = [(w, d) for w in words for d in self.inverse_index[w]]

        tfidfs = Counter()
        for w, d in matches:
            tfidfs[d] += self.text_frequencies[(d, w)] / len(self.inverse_index[w])

        return tfidfs

    def get_okapis(self, query, normalize=False) -> Counter:
        words = self.tokenize(query)
        matches = [(w, d) for w in words for d in self.inverse_index[w]]

        tfidfs = Counter()
        for w, d in matches:
            tfidfs[d] += self.get_okapi_idf(w) * self.get_okapi_tf(w, d)

        return tfidfs
