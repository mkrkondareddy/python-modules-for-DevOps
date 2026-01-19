import yaml
from pprint import pprint 


with open("deploy.yaml", "r") as f:  # open yaml file in read mode
    # data = f.read()
    data = yaml.safe_load(f)   # convert yanl into python dictionary and assign to data variable
    pprint(data)
    pprint(type(data))
    # pprint(dir(data))
    
    data["spec"]["template"]["spec"]["containers"][0]["image"] = "busybox"    # chnage image of deployemnt and save
    
with open("updated_deploy.yaml", "w") as f:     # open the file in write mode which truncate(delete) the existing content of file
    yaml.safe_dump(data, f)      # write updated data into this file and also convert python dict into yaml
    