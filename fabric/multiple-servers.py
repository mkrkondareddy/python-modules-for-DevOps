from fabric import Connection 

hosts = ["34.235.161.123", "34.207.142.58"]
user = "ec2-user"
key_path = "../pramico/aws-key.pem"

for host in hosts:
    c= Connection(
        host=host,
        user=user,
        connect_kwargs={
            "key_filename": key_path,
        },
    )
    result = c.run('uname -s')
    print("{}: {}".format(host, result.stdout.strip()))

    c.close()

