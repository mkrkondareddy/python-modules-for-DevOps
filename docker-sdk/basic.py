# import docker

# client = docker.from_env()
# client.containers.run("ubuntu"), "echo hello world")

import docker

client = docker.from_env()

containers = client.containers.list(all=True)

print(containers)

for container in containers:
    # print(dir(container))
    print(f"{container.id}, | {container.name}, | {container.status}")
    
