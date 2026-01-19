import yaml
from pprint import pprint


# reading multiple YAML config from same file seperated with "---"
with open ("multi.yaml", "r") as f:
    data = list(yaml.safe_load_all(f))
    pprint(data)
    pprint(type(data))
    
    for i in data:
        print(i.get("metadata", {}).get("name", ""))