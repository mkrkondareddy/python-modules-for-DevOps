import docker

client = docker.from_env()
response=client.images.pull('nginx') # pulling nginx image

print(response)

