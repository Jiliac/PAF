import paramiko
import sys

f = open('ipadress.txt', 'r')
host = f.read()

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username='odroid', password='odroid')

def dijkstra(repeat, size):
	stdin, stdout, stderr = client.exec_command('./PAF/benchmarks/dijkstra-O3 ' + str(repeat) + ' ' + str(size))
	net_dump = stdout.readlines()
	time = net_dump[1].split()[1]
	print "time: " + time



if len(sys.argv) > 2:
	arg1 = sys.argv[1]
	arg2 = sys.argv[2]
else:
	arg1 = ''
	arg2 = ''
dijkstra(arg1, arg2);

client.close