import paramiko

import paramiko 

HOST = "54.90.194.169"
USER = "ec2-user"
KEY_PATH = "./aws-key.pem"

# Establish the SSH client
client = paramiko.SSHClient() 
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Automatically add host keys (not secure for production)
key = paramiko.RSAKey.from_private_key_file(KEY_PATH)
client.connect(hostname=HOST, username=USER, pkey=key)

# Open an SFTP session
sftp = client.open_sftp()

# Upload a file
local_file_path = './basic_ssh.py'
remote_file_path = '/tmp/basic_ssh.py'
sftp.put(local_file_path, remote_file_path)

# Close the connections
sftp.close()
client.close()