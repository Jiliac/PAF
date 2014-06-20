import paramiko
import sys

f = open('ipadress.txt', 'r')
host = f.read()


def getFreq(client):
	stdin, stdout, stderr = readclient.exec_command('cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq')
	net_dump = stdout.readlines()
	print 'frequency: ' + net_dump[0]
	frequency = int(net_dump[0])
	f = open('frequency.txt', 'w')
	f.write(str(frequency))

def setFreq(f, client):
	stdin, stdout, stderr = client.exec_command('echo ' + str(f) + ' > /sys/devices/system/cpu/cpu0/cpufreq/scaling_setspeed')

readclient = paramiko.SSHClient()
readclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
readclient.connect(host, username='odroid', password='odroid')
getFreq(readclient)

if len(sys.argv) > 1:
	writeclient = paramiko.SSHClient()
	writeclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	writeclient.connect(host, username='root', password='odroid')
	argv = sys.argv
	argv.pop(0)
	for arg in argv:
		setFreq(arg, writeclient)
		getFreq(readclient)
	writeclient.close()

readclient.close()
