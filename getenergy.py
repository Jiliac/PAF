import paramiko

f = open('ipadress.txt', 'r')
host = f.read()

def printres(stdout):
	lines = stdout.readlines()
	print lines

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(host, username='odroid', password='odroid')

stdin, stdout, stderr = client.exec_command('echo odroid | sudo -s insmod PAF/energy.ko')
printres(stdout)
stdin, stdout, stderr = client.exec_command('echo odroid | sudo -s /PAF/pt-energy')
printres(stdout)

client.close()