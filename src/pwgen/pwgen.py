import random
from dataclasses import dataclass


@dataclass
class CharsetMinSamples:
    charset: str
    n_samples: int

    def exclude(self, chars: str):
        self.charset = ''.join(c for c in self.charset if c not in set(chars))
        return self


def generate_password(length: int, charsets: list[CharsetMinSamples]) -> str:
    password = []
    for charset in charsets:
        password += random.choices(charset.charset, k=charset.n_samples)

    if len(password) < length:
        all_characters = "".join(charset.charset for charset in charsets)
        password += random.choices(all_characters, k=length - len(password))
    random.shuffle(password)
    return "".join(password)
