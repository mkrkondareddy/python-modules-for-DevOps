import yaml

data = {
    "app": {"name": "order-service", "version": "2.0"},
    "replicas": 2,
    "ports": [8080, 8443]
}

# read data from dictionary and write to file called out.txt in yaml.
with open("out.yaml", "w") as f:
    yaml.safe_dump(data, f)
    # print(result)