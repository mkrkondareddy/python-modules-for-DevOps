import docker

client = docker.from_env()

print("listing images .............")

images_list = client.images.list()
print (images_list)
for image in images_list:
    print(dir(image))
    print(image.tags)