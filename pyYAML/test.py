import yaml
from pprint import pprint

with open("./deploy.yaml", "r") as f:
    data = yaml.safe_load(f)
    pprint(data)
    
    data["kind"] = "pod"
    
    
    pprint(data)
    
with open("test-konda.yaml", "w") as f:
    final_data = yaml.safe_dump(data, f)