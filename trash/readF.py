import paramiko

def setFreq(f, ssh):
	stdin, stdout, stderr = ssh.exec_command(str(f) + '> /sys/devices/system/cpu/cpu0/cpufreq/scaling_setspeed')
	net_dump = stdout.readlines()
	print net_dump

def readFreq(ssh):
	stdin, stdout, stderr = ssh.exec_command('cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq')
	net_dump = stdout.readlines()
	print net_dump[0]

ssh = paramiko.SSHClient()
print "start ssh"
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.1.21', username='odroid', password='odroid')

readFreq(ssh)

ssh.close()
print "end"

