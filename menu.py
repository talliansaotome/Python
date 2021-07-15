#!/usr/bin/python3
## includes
import csv
import subprocess


class VPNTunnel:

  def __init__(self, line):
    self.menu_text = line[0]
    self.ip = line[1]
    self.user = line[2]  # or wherever it is
    self.connection_string = f"ssh {self.user}@{self.ip}"

  #def connect(self):
  #  self.ssh_process = subprocess.run(self.connection_string, shell=True)



servers = []

with open('file.csv') as csvfile:    
  csvReader = csv.reader(csvfile)    
  for row in csvReader:
    servers.append(VPNTunnel(row))

##Menu to select choices
#0 out counter
i = 0
#iterate through
for server in servers:
  i += 1
  print(f"{i}): {server.menu_text}")
  

server_choice = input()

#servers[int(server_choice)].connect
#print(servers[1].connection_string)

x = subprocess.run(servers[0].connection_string, shell=True)
