import yaml
import numpy as np

data = yaml.safe_load(open('nlu\\train.yml', 'r', encoding='utf-8').read())

inputs, outputs = [], []

for command in data['commands']:
    inputs.append(command['input'])
    outputs.append('{}\{}'.format(command['entity'], command['action']))

#Processar texto: palavras, caracteres, byts, sub-palavras

chars = set()

for input in inputs + outputs:
    for ch in input:
        if ch not chars:
            chars.add(ch)

print('Número de chars:', len(chars))
#Criar dataset
chr2idx

print(inputs)
print(outputs)