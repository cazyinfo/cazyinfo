import sys
import yaml

import pprint
pp = pprint.PrettyPrinter(indent=4).pprint

file="in.yml"
try:
    with open(file, 'r', encoding='utf-8') as f:
        obj = yaml.safe_load(f)
        pp(obj)
except Exception as e:
    print('Exception occurred while loading YAML...', file=sys.stderr)
    print(e, file=sys.stderr)
    sys.exit(1)

file=open("o", "a",  encoding='utf-8')
print("aaa", file=file)
print("bbb", file=file)
