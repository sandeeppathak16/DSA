import re

with open('14.txt', 'r') as file:
    inputs = {}
    for line in file.readlines():
        name = line.strip().split(' ', maxsplit=1)[0]
        speed, till, rest = re.findall(r"\d+", line)
        inputs[name] = {
            'speed': int(speed),
            'distance': 0,
            'current_till': int(till),
            'current_rest': int(rest),
            'till': int(till),
            'rest': int(rest),
            'points': 0
        }


for _ in range(2503):
    new_inputs = {}
    for key, value in inputs.items():
        if value['current_till'] > 0:
            value = {
                **value,
                'current_till': value['current_till'] - 1,
                'distance': value['distance'] + value['speed']
            }
        elif value['current_till'] == 0 and value['current_rest'] > 0:
            value = {
                **value,
                'current_rest': value['current_rest'] - 1,
            }
        elif value['current_till'] == 0 and value['current_rest'] == 0:
            value = {
                **value,
                'current_till': value['till'] - 1,
                'distance': value['distance'] + value['speed'],
                'current_rest': value['rest']
            }

        new_inputs[key] = value

    inputs = new_inputs

    maxDistance = float('-inf')
    name = None

    for key, value in inputs.items():
        if value['distance'] > maxDistance:
            maxDistance = value['distance']
            name = key

    inputs[name] = {
        **inputs[name],
        'points': inputs[name]['points'] + 1
    }


maxPoints = float('-inf')
maxDistance = float('-inf')

for key, value in inputs.items():
    if value['distance'] > maxDistance:
        maxDistance = value['distance']

    if value['points'] > maxPoints:
        maxPoints = value['points']

print(maxDistance, maxPoints)
