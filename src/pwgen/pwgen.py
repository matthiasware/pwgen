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
    # validate if password of given length is creatable
    fixed_length = sum(cs.n_samples for cs in charsets)
    if fixed_length > length:
        raise ValueError(f"Cannot create password of length '{length}' since the amount of specified mandadorty characters is {fixed_length}!")

    password = []
    for charset in charsets:
        password += random.choices(charset.charset, k=charset.n_samples)
    
    all_characters = "".join(charset.charset for charset in charsets)
    password += random.choices(all_characters, k=length - len(password))
    random.shuffle(password)
    return "".join(password)
