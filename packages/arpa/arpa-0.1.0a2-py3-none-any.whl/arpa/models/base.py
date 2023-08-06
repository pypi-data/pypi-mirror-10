from abc import ABCMeta, abstractmethod


class ARPAModel(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add_count(self, order, count):
        pass

    @abstractmethod
    def add_entry(self, ngram, p, bo=None, order=None):
        pass

    def log10_p(self, ngram):
        if not ngram:
            raise ValueError
        elif isinstance(ngram, str):
            ngram = self._str2tuple(ngram)
        elif isinstance(ngram, list):
            ngram = tuple(ngram)
        elif not isinstance(ngram, tuple):
            raise ValueError

        try:
            return self._log10_p(ngram)
        except KeyError:
            try:
                log10_bo = self._log10_bo(ngram[:-1])
            except KeyError:
                log10_bo = 0
            return log10_bo + self.log10_p(ngram[1:])

    def p(self, ngram):
        return 10 ** self.log10_p(ngram)

    # TODO: log10_s

    def log10_s(self, sentence, wrap=False):
        import math
        return math.log10(self.s(sentence, wrap))

    def s(self, sentence, wrap=False):
        # TODO: duplication
        if not sentence:
            raise ValueError
        elif isinstance(sentence, str):
            sentence = self._str2tuple(sentence)
        elif isinstance(sentence, list):
            sentence = tuple(sentence)
        elif not isinstance(sentence, tuple):
            raise ValueError

        result = 1
        for pos, word in enumerate(sentence):
            result *= self.p(sentence[:(pos + 1)])
        return result

    @abstractmethod
    def _log10_bo(self, ngram):
        pass

    @abstractmethod
    def _log10_p(self, ngram):
        pass

    @staticmethod
    def _str2tuple(s):
        return tuple(s.strip().split(" "))
