import docker
import time

client = docker.from_env()

response = client.images.pull('nginx') # pulling nginx image
print("Pulled image:", response)

time.sleep(2)

container = client.containers.run(
    image="nginx",
    name="nginx-python",
    detach=True,
    ports={"80/tcp": 8080}
)

print("Container started:", container.id)
