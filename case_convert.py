"""
Simple case conversion functions to support cross language payloads
"""


def snake_to_kebab(s):
    return s.replace('_', '-').lower()


def kebab_to_snake(s):
    return s.replace('-', '_').lower()


def snake_to_camel(s):
    if not len(s):
        return s
    prefix = []
    res = []
    s = s.rstrip('_')
    for word in s.split('_'):
        if not word:
            prefix.append('_')
            continue
        formatted = word
        if len(res) > 0:
            formatted = formatted.title()
        res.append(formatted)
    return "{prefix}{var}".format(prefix=''.join(prefix), var=''.join(res))


def camel_to_snake(s):
    if len(s) and s[0].lower() != s[0]:
        raise Exception("Not a valid camel case string")
    res = []
    letters = []
    i = 0
    while i < len(s):
        if s[i].lower() == s[i]:
            letters.append(s[i])
        else:
            res.append(''.join(letters))
            letters = [s[i]]
        i += 1
    res.append(''.join(letters))
    return '_'.join(res).lower()

if __name__ == "__main__":
    print("Testing kebab_to_snake..."),
    kebab1 = ""
    kebab2 = "snake"
    kebab3 = "two-words"
    kebab4 = "snake-three-words"
    assert kebab_to_snake(kebab1) == ''
    assert kebab_to_snake(kebab2) == 'snake'
    assert kebab_to_snake(kebab3) == 'two_words'
    assert kebab_to_snake(kebab4) == 'snake_three_words'
    print("Passed!")

    print("Testing snake_to_camel..."),
    snake1 = ""
    snake2 = "snake"
    snake3 = "two_words"
    snake4 = "snake_three_words"
    snake5 = "_private"
    snake6 = "__private"
    assert snake_to_camel(snake1) == '', snake_to_camel(snake1)
    assert snake_to_camel(snake2) == 'snake'
    assert snake_to_camel(snake3) == 'twoWords'
    assert snake_to_camel(snake4) == 'snakeThreeWords'
    assert snake_to_camel(snake5) == '_private', snake_to_camel(snake5)
    assert snake_to_camel(snake6) == '__private', snake_to_camel(snake6)
    print("Passed!")

    print("Testing camel_to_snake..."),
    camel1 = ""
    camel2 = "snake"
    camel3 = "twoWords"
    camel4 = "snakeThreeWords"
    assert camel_to_snake(snake1) == ''
    assert camel_to_snake(snake2) == 'snake'
    assert camel_to_snake(snake3) == 'two_words'
    assert camel_to_snake(snake4) == 'snake_three_words'
    print("Passed!")
