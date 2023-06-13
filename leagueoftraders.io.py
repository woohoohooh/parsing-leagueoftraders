import requests
import json
import csv
count = 0
statttus = []
for i in range(10000):
    try:
        r = requests.get(f'https://api.leagueoftraders.io/v3/rank?e=&r=1000&l=&o={count}')
        d = r.json()
        e = d['data']
        while len(e) > 0:
            for i in e:
                name = i['name']
                status = i['status']
                with open('names.txt', encoding='utf8') as f:
                    a = f.read()
                if name not in a:
                    if status not in statttus:
                        statttus.append(status)
                        with open('names.txt', 'a', encoding='utf8') as f:
                            f.write(f'{name}\n')
                        print(name)
                        print()
                        print(str(status))
                        print('------------------------------------------------------------------------------------------------------')
                        with open('status.txt', 'a', encoding='utf8') as f:
                            f.write(f'{status}\n\n\n\n\n')
    except Exception as ex:
        count += 1
