from fabric import Connection

c = Connection(
    host="34.235.161.123",
    user="ec2-user",
    connect_kwargs={
        "key_filename": "../paramiko/aws-key.pem",
    },
)

result = c.run('sudo useradd konda')
print(result)

user_id = c.run("id -u konda")
print(user_id)
