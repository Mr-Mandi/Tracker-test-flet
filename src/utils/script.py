import random

options = [
    {"label": 'Option 1', "value": ""},
    {"label": 'Option 2', "value": ""},
    {"label": 'Option 3', "value": ""},
    {"label": 'Option 4', "value": ""},
    {"label": 'Option 5', "value": ""},
    {"label": 'Option 6', "value": ""}
]


def get_random_options():
    selects = []
    for _ in range(5):
        selects.append(random.choice(options))
    return random.choice(selects)


def get_random_text_options():
    dict_random = {}
    results = ''
    while True:
        results = get_random_options()
        valor = results['value']
        if valor in dict_random:
            dict_random[valor] += 1
        else:
            dict_random[valor] = 1

        if dict_random[valor] == 10:
            break

    max_key = max(dict_random, key=dict_random.get)
    return max_key
