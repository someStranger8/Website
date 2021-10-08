
# imports
import os
import cobra as c

# banner
clear = lambda: os.system("clear")
clear()
print("")
print("\____)\______                    ______/(____/")
print("/--^____ __'<    SHARK ATTACK    >'__ ____^--\\")
print("       )/                            \(")
print("")

# while loop
i=1
while i < 10:
     shell=input("shark@attack:~$ ")
     if shell == "clear":
          clear()
     elif shell == "sqlinject":
          c.sqlinject()
     elif shell == "exploit":
          c.exploit()
     elif shell == "python":
          os.system("python3")
     elif shell == "hackwifi":
          c.hackwifi()
     elif shell == "fish":
          os.system("fish")
     elif shell == "VA":
          os.system("python3 VA.py")
     elif shell == "chdir":
          dir=input("[*] enter name of directory: ")
          os.chdir(dir)
     elif shell == "banner":
          print("\____)\______")
          print("/--^____ __'<")
          print("       )/")
     elif shell == "hackpasswd":
          usr=input("[*] enter username: ")
          wl=input("[*] enter wordlist: ")
          ip=input("[*] enter ip address: ")
          c.hackpasswd(usr, wl, ip)
     elif shell == "mitm":
          c.mitm()
     elif shell == "scan":
          nmap=input("[*] enter ip: ")
          c.scan(nmap)
     elif shell == "hackweb":
          c.hackweb()
     elif shell == "git":
          git=input("[*] enter github url: ")
          c.git(git)
     elif shell == "hackphone":
          c.hackphone()
     elif shell == "hackdrone":
          c.hackdrone()
     elif shell == "install":
          pkg=input("[*] enter the name of the package you want to install: ")
          c.install(pkg)
     elif shell == "payload":
          name=input("[*] enter file name: ")
          c.payload(name)
     elif shell == "ddos":
          attack=input("[*] enter ip address: ")
          c.ddos(attack)
     else:
          os.system(shell)
i+=1
