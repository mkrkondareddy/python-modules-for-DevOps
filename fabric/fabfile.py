from fabric import task

@task
def upload_and_unpack(c):  #here C is referencing to connection to remote server
    c.run("ls -la /tmp/")
    c.put('basic.py', '/tmp/')
    c.run("ls -la /tmp/")
    
    
# to cehck the available fab list use COMMAND: fab --list
# you will see ouput like below 

# fab --list
# Available tasks:
#   upload-and-unpack
    
## To manually execute this in remote server(100.48.12.233) as user(ec2-user) use the follwing command
# Command: fab -H ec2-user@100.48.12.233  --connect-kwargs="{'key_filename':'~/.ssh/aws.pem'}" upload-and-unpack

# To add automatic authentication to remote server(100.48.12.233). Add the below info to ~/.ssh/config file.
#############  ~/.ssh/config  #################################
# Host web1
#   HostName 100.48.12.233
#   User ec2-user
#   IdentityFile C:\Users\Konda Reddy Sagam\.ssh\aws-key.pem

#################################################################

## Once you added above conf to ~/.ssh/config file. Fabric will be able to read this config while connecting to remote server(100.48.12.233)
## NOw you can simply run below command to execute the code

## COMMAND: fab -H web1 upload-and-unpack

## If you want to execute this code in multiple remote servers, add the keys related to servers in ~/.ssh/config file.
## Then you can execute the code in multiple servers at the same time by using below command 

## COMMAND: fab -H web1,web2 upload-and-unpack


## if you want to enable the Parallel execution, run command like below
## COMMAND: fab -H web1,web2,web3 --parallel upload-and-unpack
