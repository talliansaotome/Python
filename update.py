#!/usr/bin/python

# Script for updating fleet from defined file

# Import required modules
import fileinput
import paramiko
import os

# Check Root status - ROOT ONLY
if os.geteuid() != 0:
    exit("You need root permissions to execute this script!\nPlease try again as root or execute with sudo!")

# Define static variables
HOSTLIST = '/data/masters/clientlist'
USER = 'root'

# Build list of systems from file defined in HOSTLIST
with open(HOSTLIST) as f:
    hosts = [line.rstrip('\n') for line in f]

# Configure paramiko ssh usage
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Main Logic
for host in hosts:
    ssh.connect(host, username=USER)
    stdin, stdout, stderr = ssh.exec_command('yum update -y')
    output = stdout.read()
    print 'Update log for ' + host +':'
    print output
