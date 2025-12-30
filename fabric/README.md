Fabric Automation with Python

This repository demonstrates end-to-end usage of the Fabric Python module for running commands and automating tasks on remote Linux servers over SSH.

It covers:

What a fabfile is

How Fabric handles SSH authentication

How to run tasks on single and multiple servers

Practical examples and best practices

📌 What is Fabric?

Fabric is a high-level Python library built on top of Paramiko that simplifies SSH-based remote execution and automation.

Fabric allows you to:

Run commands on remote servers

Execute tasks across multiple hosts

Use SSH keys and SSH agent automatically

Orchestrate tasks using a CLI (fab)

📄 What is a fabfile?

A fabfile is a Python file (by convention named fabfile.py) where you define Fabric tasks.

Fabric automatically discovers tasks in fabfile.py and exposes them through the fab command-line tool.

Think of a fabfile as:

An Ansible playbook, but written in Python

A Makefile, but for remote servers

A reusable automation script for DevOps tasks

📂 Project Structure
.
├── fabfile.py
├── README.md
└── hosts.txt (optional)

🧱 Basic fabfile.py Example
from fabric import task

@task
def hello(c):
    c.run("hostname")

Explanation

@task makes the function executable via the Fabric CLI

c is a Connection object automatically created by Fabric

The function name becomes the CLI task name

▶️ Running Fabric Tasks
Run locally defined task
fab hello

Run on a single remote host
fab -H ec2-user@34.235.161.123 hello

Run on multiple hosts
fab -H ec2-user@host1,ec2-user@host2 hello


Fabric automatically:

Creates an SSH connection per host

Executes the task on each host

🔐 SSH Authentication (How It Works)

Fabric automatically uses your existing SSH setup, including:

SSH agent (ssh-add)

Keys in ~/.ssh/id_rsa, id_ed25519, etc.

~/.ssh/config

known_hosts for host verification

If the following works:

ssh ec2-user@server


Then this will work without extra configuration:

fab -H ec2-user@server hello

🔑 Forcing a Specific SSH Key

In environments like CI/CD or restricted systems, you may want to explicitly specify a key:

fab -H ec2-user@server \
  --connect-kwargs="{'key_filename':'~/.ssh/aws-key.pem'}" hello

🛠 Running Commands with sudo
@task
def update(c):
    c.sudo("yum update -y")


Run:

fab -H ec2-user@server update

📥 Passing Arguments to Tasks
@task
def disk(c, path="/"):
    c.run(f"df -h {path}")


Run:

fab -H server disk --path=/var

🧪 Running Multiple Commands in One Task
@task
def health(c):
    c.run("hostname")
    c.run("uptime")
    c.run("df -h")


Run:

fab -H host1,host2 health

⚡ Parallel Execution

Fabric can run tasks concurrently across multiple hosts:

fab -H host1,host2,host3 --parallel health

📁 File Upload and Download
@task
def deploy(c):
    c.put("app.conf", "/tmp/app.conf")
    c.sudo("mv /tmp/app.conf /etc/app.conf")
    c.sudo("systemctl restart app")

❗ Error Handling
from invoke.exceptions import UnexpectedExit

@task
def safe_run(c):
    try:
        c.run("false")
    except UnexpectedExit:
        print("Command failed, continuing execution")

📊 Fabfile vs Plain Python Script
Plain Python Script	Fabric Fabfile
Manual SSH handling	Automatic SSH handling
Manual loops	Built-in multi-host execution
Manual argument parsing	CLI-based arguments
Sequential only	Optional parallel execution
✅ When to Use a Fabfile

Use a fabfile when:

Running commands on multiple servers

Performing repeatable operational tasks

Automating DevOps or SRE workflows

You want CLI-based orchestration using Python

🧠 Summary

A fabfile is the core automation unit in Fabric

Fabric handles SSH connections, authentication, and host iteration

Tasks are written in Python and executed via the fab CLI

Fabric is ideal for ad-hoc automation, maintenance tasks, and orchestration