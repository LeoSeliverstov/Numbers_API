import requests

with open('./dataset_24476_3.txt') as f:
    line = f.read().split()
    for i in line:
        res = requests.get(f'http://numbersapi.com/{i}/math?json')

        data = res.json()

        if data['found']:
            print('Interesting')
        else:
            print('Boring')
