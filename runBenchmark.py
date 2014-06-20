import paramiko
import sys

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

def runbenchmark(program):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(host, username='odroid', password='odroid')
	
	client.exec_command('./PAF/pt-energy > ./PAF/data.txt')
	cmd = './PAF/benchmarks/' + program + ' ' + arg1 + ' ' + arg2
	stdin, stdout, stderr = client.exec_command(cmd)
	print program
	print stdout.read()
	
	client.close()
	
	client.connect(host, username='odroid', password='odroid')
	stdin, stdout, stderr = client.exec_command('cat ./PAF/data.txt | tr -d "[]"')
	energy_report = stdout.read()
	client.close()
	
	f = open('data/' + program + '-' + str(float(arg1)/1000000) + 'M-' + arg2 + '-' + 'EnergyData-' + str(frequency/1000000) + 'Ghz.txt', 'w')
	f.write(energy_report)

runbenchmark(program)