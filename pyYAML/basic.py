import yaml
from pprint import pprint

with open ("config.yaml", "r") as f:
    result = yaml.safe_load(f)
    pprint(result)
    print(type(result))