from fabric import Connection

# Connect to remote server
c = Connection(
    host="34.235.161.123",
    user="ec2-user",
    connect_kwargs={
        "key_filename": "../pramico/aws-key.pem",
    },
)

# copy file to remote server
result = c.put('myfiles.tgz', remote='/tmp/')
print(result)

# untar file 
c.run('tar -C /opt/mydata -xzvf /tmp/myfiles.tgz')