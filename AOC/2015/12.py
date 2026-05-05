import json

def solve(filename='12.txt', solve_part_2=False):
    with open(filename, 'r') as file:
        data = json.loads(file.readline().strip())

    def process(data):
        if isinstance(data, int):
            return data
        
        if isinstance(data, list):
            return sum(process(ele) for ele in data)
        
        if isinstance(data, dict):
            if solve_part_2 and 'red' in data.values():
                return 0
            
            return sum(process(value) for value in data.values())
        
        return 0

    return process(data)