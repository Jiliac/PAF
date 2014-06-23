import paramiko
import sys
import time

f = open('ipadress.txt', 'r')
host = f.read()
f = open('frequency.txt', 'r')
frequency = float(f.read())


if len(sys.argv) > 3:
	program = sys.argv[1]
	arg1 = sys.argv[2]
	arg2 = sys.argv[3]
else:
	program = 'dijkstra-O3'
	arg1 = ''
	arg2 = ''

# name of record file
filename = program + '-' + str(float(arg1)/1000000) + 'M-' + arg2 + '-' + 'EnergyData-' + str(frequency/1000000) + 'Ghz.txt'


def runbenchmark(program):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(host, username='odroid', password='odroid')
	
	client.exec_command('./PAF/pt-energy | tr -d "[]"> ./PAF/data/' + filename)
	cmd = './PAF/benchmarks/' + program + ' ' + arg1 + ' ' + arg2
	stdin, stdout, stderr = client.exec_command(cmd)
	print program
	print stdout.read()
	
	time.sleep(3)
	client.exec_command('pkill pt-energy')
	client.close()

runbenchmark(program)