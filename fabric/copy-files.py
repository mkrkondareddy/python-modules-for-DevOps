from fabric import Connection

c = Connection(
    host="34.235.161.123",
    user="ec2-user",
    connect_kwargs={
        "key_filename": "../pramico/aws-key.pem",
    },
)

result = c.put('basic.py', remote='/tmp/')
print(result)