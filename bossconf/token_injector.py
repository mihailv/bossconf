import re


class TokenInjector:
    def __init__(self, tokens, token_fmt='%s'):
        self.tokens = dict([(token_fmt % t, v) for t, v in tokens.iteritems() if isinstance(v, basestring)])
        self.rx = re.compile('|'.join(map(lambda k: re.escape(k), self.tokens.keys())))

    def __call__(self, text):
        return self.rx.sub(lambda match: self.tokens[match.group(0)], text)
