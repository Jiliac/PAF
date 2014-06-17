import paramiko
import sys

f = open('ipadress.txt', 'r')
host = f.read()

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def setFreq(f, client):
	client.connect(host, username='root', password='odroid')
	stdin, stdout, stderr = client.exec_command('echo ' + str(f) + ' > /sys/devices/system/cpu/cpu0/cpufreq/scaling_setspeed')
	client.close()

def readFreq(client):
	client.connect(host, username='odroid', password='odroid')
	stdin, stdout, stderr = client.exec_command('cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq')
	net_dump = stdout.readlines()
	print 'frequency: ' + net_dump[0]
	client.close()

readFreq(client)

argv = sys.argv
if len(argv) > 0:
	argv.pop(0)
for arg in argv:
	setFreq(arg, client)
	readFreq(client)

