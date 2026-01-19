import yaml

def yaml_to_dict(file_path):
    with open(file_path, "r") as f:
        data = yaml.safe_load(f)
        return data
        
        
dict_output = yaml_to_dict("pod.yaml")
# print(konda)

def extract_data_from_dict(file_path):
    return file_path["kind"]

final_output = extract_data_from_dict(dict_output)
print(final_output)
    
    