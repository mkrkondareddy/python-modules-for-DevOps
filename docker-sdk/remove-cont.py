import docker 

client = docker.from_env()

response = client.containers.get("4d0e6ccd0956")
response.remove(force=True)
print(response)