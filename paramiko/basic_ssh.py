import paramiko

command = "df"

# Update the next three lines with your
# server's information

host = "<remote_host_IP_or_hostname>"
username = "<username>"
password = "<password>"

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
_stdin, _stdout,_stderr = client.exec_command("free -m")
print(_stdout.read().decode())
client.close()