import json
with open('dados.json', 'r') as file:
    data = json.load(file)

print(data['valor']);