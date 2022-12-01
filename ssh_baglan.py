import paramiko

ip = "10.10.1.124"
kullanici = "root"
sifre = "123456"
komut = "ls -al"
port = 22

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip,port,kullanici,sifre,timeout = 10)

stdin,stdout,stderr = ssh.exec_command(komut)
sonuc = stdout.read()
print(sonuc.decode("utf-8"))

ssh.close()
