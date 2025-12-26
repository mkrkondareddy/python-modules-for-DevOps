import paramiko

HOST = "54.90.194.169"
USER = "ec2-user"
KEY_PATH = "./aws-key.pem"

commands = ["ls -la /home/ec2-user", "df -h", "free -m"]

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

key = paramiko.RSAKey.from_private_key_file(KEY_PATH)

client.connect(hostname=HOST, username=USER, pkey=key)


for command in commands:
     stdin, stdout, stderr = client.exec_command(command)
     print(stdout.read().decode())

client.close()
