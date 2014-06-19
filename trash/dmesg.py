#!/usr/bin/python

from StringIO import StringIO
import paramiko 

f = open('ipadress.txt', 'r')
host = f.read()

class SshClient:
    "A wrapper of paramiko.SSHClient"
    TIMEOUT = .004

    def __init__(self, host, port, username, password, key=None, passphrase=None):
        self.username = username
        self.password = password
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if key is not None:
            key = paramiko.RSAKey.from_private_key(StringIO(key), password=passphrase)
        self.client.connect(host, port, username=username, password=password, pkey=key, timeout=2)

    def close(self):
        if self.client is not None:
            self.client.close()
            self.client = None

    def execute(self, command, sudo=False):
        feed_password = False
        if sudo and self.username != "root":
            command = "sudo -S -p '' %s" % command
            feed_password = self.password is not None and len(self.password) > 0
        stdin, stdout, stderr = self.client.exec_command(command)
        if feed_password:
            stdin.write(self.password + "\n")
            stdin.flush()
        return {'out': stdout.readlines(), 
                'err': stderr.readlines(),
                'retval': stdout.channel.recv_exit_status()}


if __name__ == "__main__":
    client = SshClient(host=host, port=22, username='odroid', password='odroid') 
    try:
       ret = client.execute('insmod PAF/energy.ko', sudo=True)
       print "  ".join(ret["out"]), "  E ".join(ret["err"]), ret["retval"]
       ret2 = client.execute('./PAF/pt-energy', sudo=True)
       print "  ".join(ret2["out"]), "  E ".join(ret2["err"]), ret2["retval"]
    finally:
       client.close() 