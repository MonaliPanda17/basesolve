from config import Configs

def get_subset(string, start=None, length=None):
    start = start if start else Configs.CHROMO_START_INDEX
    length = length if length else Configs.CHROMO_LENGTH_COUNT
    end = start + length

    subset = string[start:end]
    return str(subset)

def reverse(string):
    reversed_str = string[::-1]
    return str(reversed_str)
