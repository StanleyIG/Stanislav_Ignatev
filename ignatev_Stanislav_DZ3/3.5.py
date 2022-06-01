def get_jokes(nouns):
    from random import choice, sample
    shutka = []
    for i in range(n):
        jokes = f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'
        shutka.append(jokes)
    return shutka

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
n = int(input())
print(get_jokes(nouns))


