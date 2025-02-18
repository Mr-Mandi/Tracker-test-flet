import random


def get_random_options(options):
    selects = []
    for _ in range(5):
        selects.append(random.choice(options))
    return random.choice(selects)


def get_random_text_options(list_options: list = []) -> str:
    dict_random: dict = {}
    results: str = ''
    options: list = []
    if len(list_options) > 0:
        options = list_options
    else:
        options = [
            {"label": 'Option 1', "value": "Medical App"},
            {"label": 'Option 2', "value": "Helpers"},
            {"label": 'Option 3', "value": "Studying"},
            {"label": 'Option 4', "value": "memory"}
        ]
    while True:
        results = get_random_options(options)
        valor = results['value']
        if valor in dict_random:
            dict_random[valor] += 1
        else:
            dict_random[valor] = 1

        if dict_random[valor] == 10:
            break

    max_key = max(dict_random, key=dict_random.get)
    if max_key == 'Studying':
        return get_random_text_options([
            {"label": 'Option 1', "value": "Ingles"},
            {"label": 'Option 2', "value": "Matematica"},
            {"label": 'Option 3', "value": "Fisica"},
            {"label": 'Option 4', "value": "Node"}
        ])

    return max_key
