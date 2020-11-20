import json
import random


data = []

with open(r'C:\Users\R\Desktop\Advanseret programering 2020\Eksamens projekt\lite2\Wiches.json') as f:
    for line in f:
        data.append(json.loads(line))

print(data)
'''
for user in data['Wiches']:
    print(Wiches['User'])
'''


'''    

weekdays = # hent den første dag i den valgte mdr

choices = # hent data om de der ønsker vagt den dag

def choose_random_candidate():
    return [random.choice(choices for choice in choices]

'''