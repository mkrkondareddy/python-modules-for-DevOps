from fabric import Connection

commands = ["ls -la /tmp", "cat /etc/passwd", "ls -la /tmp/"]

c = Connection(
    host="34.235.161.123",
    user="ec2-user",
    connect_kwargs={
        "key_filename": "../pramico/aws-key.pem",
    },
)

for command in commands:
    
    print(f"output of the command: {command}")
    result = c.run(command)
    print("#"*50)
    # print(result)
    