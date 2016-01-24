import fileinput, sys
import subprocess
import time

bashCommandStopSSH = "launchctl stop com.openssh.sshd"
bashCommandStartSSH = "launchctl start com.openssh.sshd"
bashCommandBackup = "cp /etc/ssh/sshd_config /etc/ssh/sshd_config_old"

process = subprocess.Popen(bashCommandBackup,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
output, errors = process.communicate()

print "Back up original sshd_config file OK"

with open("/etc/ssh/sshd_config", "a") as f:
	f.write("\nKexAlgorithms curve25519-sha256@libssh.org,ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256,diffie-hellman-group14-sha1,diffie-hellman-group-exchange-sha1,diffie-hellman-group1-sha1\n")

process = subprocess.Popen(bashCommandStopSSH,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
output, errors = process.communicate()

print "Write new values OK"

print "Stopping com.openssh.sshd"

time.sleep(5)

print "Starting com.openssh.sshd"
process = subprocess.Popen(bashCommandStartSSH,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
output, errors = process.communicate()

time.sleep(5)

print output

print "Done!"