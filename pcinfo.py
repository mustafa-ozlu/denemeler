import platform
import time
import shutil
import ctypes as ct
import psutil
libc = ct.cdll.msvcrt
import cpuinfo
cpu=cpuinfo.cpu.info[0]["ProcessorNameString"]

s="SİSTEM BİLGİLERİ\n"
s+=(f"PC Adı: {platform.node()}")+"\n"
s+=(f"Makine Tipi: {platform.machine()}")+"\n"
s+=(f"CPU : {platform.processor()}")+"\n"
s+=(f"CPU : {cpu}")+"\n"
s+=(f"Platform : {platform.platform()}")+"\n"
s+=(f"OS : {platform.system()}")+"\n"
s+=(f"OS Rel.: {platform.release()}")+"\n"
s+=(f"OS Vers: {platform.version()}")+"\n"
s+=(f"Arch: {platform.architecture()}")+"\n"
s+=(f"RAM : {round(psutil.virtual_memory().total/(1024*1024*1024), 2)} GB")+"\n"
#Available RAM
print(s)

#sub.call(['cmd', '/c', 'dir', '/b'])
now=time.time()
gmt=time.gmtime()

print("Tarih \t\t:",time.strftime("%d.%m.%Y",gmt))
print("Saat  \t\t:",time.strftime("%H:%M:%S",gmt))
#print(time.strftime("%x %X", now))

drives = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
drivelist = libc._getdrives()
for n in range(26): 
    mask = 1 << n # use left bit shifting to build a mask 
    if drivelist & mask: 
        total,used,free=shutil.disk_usage(drives[n]+":")
        
#        return free_bytes.value
        print (drives[n], "Diski \t:","Toplam Alan :",(total//(2**30)),"GB ","Boş Alan : ",(free//(2**30))," GB")                                   
