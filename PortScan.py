import socket
import threading
import time
from queue import Queue

def scan_port(host, port, open_ports):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    except Exception:
        pass

def worker(host, port_queue, open_ports):
    while not port_queue.empty():
        port = port_queue.get()
        scan_port(host, port, open_ports)
        port_queue.task_done()

def port_scan(host, ports, num_threads=100):
    print(f"Scanning {host} for port(s): {', '.join(map(str, ports))}...")
    start_time = time.time()
    
    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("Error: Could not resolve hostname")
        return
    
    port_queue = Queue()
    open_ports = []
    
    for port in ports:
        port_queue.put(port)
    
    threads = []
    for _ in range(min(num_threads, len(ports))):
        thread = threading.Thread(target=worker, args=(ip, port_queue, open_ports))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    
    open_ports.sort()
    if open_ports:
        print("\nOpen ports:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print("\nNo open ports found.")
    
    print(f"\nScan completed in {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    target_host = input("Enter target host (e.g., example.com or IP): ")
    port_input = input("Enter a single port or port range (e.g., 80 or 80-100): ")
    
    try:
        if '-' in port_input:
            start_port, end_port = map(int, port_input.split('-'))
            if start_port < 1 or end_port > 65535 or start_port > end_port:
                print("Invalid port range. Ports must be between 1 and 65535, and start_port must be less than or equal to end_port.")
                exit(1)
            ports = range(start_port, end_port + 1)
        else:
            single_port = int(port_input)
            if single_port < 1 or single_port > 65535:
                print("Invalid port. Port must be between 1 and 65535.")
                exit(1)
            ports = [single_port]
        
        port_scan(target_host, ports)
    except ValueError:
        print("Invalid input. Please enter a valid port number or range (e.g., 80 or 80-100).")