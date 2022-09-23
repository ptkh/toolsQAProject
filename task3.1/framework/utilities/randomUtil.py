import random
import string


class RandomUtil:
    """Utility class for generation random data"""
    @staticmethod
    def get_random_string(length_range: tuple[int, int]):
        return ''.join([random.choice(string.ascii_lowercase) for _ in range(random.randint(*length_range))])

