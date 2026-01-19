import yaml

def extract_data(path):
    with open (path, "r") as f:
        return yaml.safe_load(f)
    
# test = extract_data("pod.yaml")
# print(test)
