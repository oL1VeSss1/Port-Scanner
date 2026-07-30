import socket
import concurrent.futures
from datetime import datetime
import time
import ipaddress





def main():
    socket.setdefaulttimeout(0.5)
    host = input('[*] Enter a host(Example: google.com): ')
    server = socket.gethostbyname(host)
    return server

def PortRange():
    while True:
            start_port = int(input('[*] Enter start_port: '))
            if start_port < 0 or start_port > 65535:
                print(f'[!] Not found start_port {start_port}! Please retry [!]')
                continue
            end_port = int(input('[*] Enter end_port: '))
            if end_port < 0 or end_port > 65535:
                print(f'[!] Not found end_port {end_port}! Please retry [!]')
                continue
            elif end_port <= start_port:
                print('[!] end_port must be greater than start_port [!]')
                continue
            else:
                return start_port, end_port         

def ScanRange(server):
    network = ipaddress.ip_network(f'{server}/24', strict=False)
    ips = []
    for ip in network.hosts():
        ips.append(str(ip))
    return ips
        

server = main()
start_port, end_port = PortRange()

start = time.perf_counter()




def ScanServer(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if not sock.connect_ex((ip, port)):
            print(f"[+] TCP PORT {port} IS OPEN ON {ip}")

        sock.close()

    except Exception:
        pass

ips = ScanRange(server)

with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
    result = []

    for ip in ips:
        for port in range(start_port, end_port + 1):
            result.append(
                executor.submit(ScanServer, ip, port)
            )

    for f in concurrent.futures.as_completed(result):
        f.result()



finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')





          

          





    
          
    
    






















    


