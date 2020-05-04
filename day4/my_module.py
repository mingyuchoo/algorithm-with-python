def check_validation(word: str) -> bool:
    if word is None:
        raise TypeError
    if len(word) > 100000:
        return False
    if not word.isalpha():
        return False
    return True


def check_anagram(word_a: str, word_b: str) -> bool:
    if check_validation(word_a) and check_validation(word_b):
        sorted_a = "".join(sorted(word_a.lower())).strip()
        sorted_b = "".join(sorted(word_b.lower())).strip()
        if sorted_a == sorted_b:
            return True
        else:
            return False
    else:
        return False


def my_function(word_a, word_b):
    return check_anagram(word_a, word_b)