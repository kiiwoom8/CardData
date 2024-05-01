import json
from collections import defaultdict

data = {}
data['Dark Magician Girl'] = {}
data['Dark Magician Girl']['QCCU-KR191'] = {}
data['Dark Magician Girl']['QCCU-KR191']['SecretRare'] = []
# Accessing keys with nested structure creation
data['Dark Magician Girl']['QCCU-KR191']['SecretRare'].append({'price': 40.0, 'date': '2021-07-01'})

with open('filename.json', 'w') as f:
    json.dump(data, f)
