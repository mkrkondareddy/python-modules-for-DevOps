import docker

client = docker.from_env()

response = client.images.build(path=".", tag="my_image:latest")

print(response)