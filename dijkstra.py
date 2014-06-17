import paramiko

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

dijkstra('', '');

client.close