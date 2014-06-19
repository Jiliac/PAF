import paramiko
import sys

f = open('ipadress.txt', 'r')
host = f.read()

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username='odroid', password='odroid')

rootclient = paramiko.SSHClient()
rootclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
rootclient.connect(host, username='odroid', password='odroid')

#rootclient.exec_command('echo "dijkstra start" > /dev/kmsg')
client.exec_command('./PAF/pt-energy > ./PAF/data.txt')
stdin, stdout, stderr = client.exec_command('./PAF/benchmarks/dijkstra-O3')
# Deux façon d'avoir le tps d'execution
"""
rootclient.exec_command('echo "dijkstra end" > /dev/kmsg')
stdin, stdout, stderr = client.exec_command('dmseg | grep dijkstra')
t1 = int(stdout.readlines()[0].split[1])
t2 = int(stdout.readlines()[1].split[1])
time = t2 - t1
"""

time = int(stdout.readlines()[1].split()[1])
nbdatalines = int(time / 200000)

client.close()
rootclient.close()

stdin, stdout, stderr = client.exec_command('cat ./PAF/data.txt')
energy_data = stdout.readlines()[:nbdatalines].join()
f = open('dijkstraEnergyData.txt', 'w')
f.write(energy_data)