import random
import string
from typing import List

DEFAULT_MAX = 1 << 12
DEFAULT_MIN = -DEFAULT_MAX
DEFAULT_SIZE = 10


class ValueException(Exception):
    pass


class TypeException(Exception):
    pass


def boolean() -> bool:
    return random.getrandbits(1) == 1

def booleans(size: int = DEFAULT_SIZE) -> List[bool]:
    if size < 1:
        raise ValueException('the size of a list must be at least 1')
    
    bools = []
    for _ in range(size):
        bools.append(boolean())
    return bools
    
def natural(min: int = 0, max: int = DEFAULT_MAX) -> int:
    if min < 0 or max < 0:
        raise ValueException('the natural number must be equal or bigger than 0')
    return random.randint(min, max)

def naturals(min: int = 0, max: int = DEFAULT_MAX, size: int = DEFAULT_SIZE) -> List[int]:
    if size < 1:
        raise ValueException('the size of a list must be at least 1')
    
    naturals = []
    for _ in range(size):
        naturals.append(natural(min, max))
    return naturals

def integer(min: int = DEFAULT_MIN, max: int = DEFAULT_MAX) -> int:
    return random.randint(min, max)

def integers(min: int = DEFAULT_MIN, max: int = DEFAULT_MAX, size: int = DEFAULT_SIZE) -> List[int]:
    if size < 1:
        raise ValueException('the size of a list must be at least 1')
    
    integers = []
    for _ in range(size):
        integers.append(integer(min, max))
    return integers

def floating(min: float = DEFAULT_MIN, max: float = DEFAULT_MAX, ndigits: int = 2) -> float:
    return round(random.uniform(min, max), ndigits)

def floatings(min: float = DEFAULT_MIN, max: float = DEFAULT_MAX, ndigits: int = 2, size: int = DEFAULT_SIZE) -> List[float]:
    if size < 1:
        raise ValueException('the size of a list must be at least 1')
    
    floatings = []
    for _ in range(size):
        floatings.append(floating(min, max, ndigits))
    return floatings

def char(pool: str = string.ascii_letters) -> str:
    if not isinstance(pool, str):
        raise TypeException('pool value must be str, not \'{}\''.format(type(pool)))
    
    return random.choice(pool)

def string(pool: str = string.ascii_letters, min: int = 3, max: int = 10) -> str:
    if min < 2:
        raise ValueException('The length of a string must ba at least 2')
    
    length = natural(min, max)
    return ''.join([char(pool) for _ in range(length)])