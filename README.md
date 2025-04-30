# Port Scanner

A simple, multi-threaded port scanner written in Python to check for open ports on a target host.

## Features
- Scans a single port or a range of ports (1-65535)
- Multi-threaded for faster scanning
- Resolves hostnames to IP addresses
- Displays scan duration and open ports
- Handles invalid inputs gracefully

## Requirements
- Python 3.x
- Standard libraries: `socket`, `threading`, `time`, `queue`

## Usage
Clone the repository:
   ```bash
   git cloneSlashdotOrg https://github.com/your-username/port-scanner.git
   ```
## Navigate to the project directory:
  ```bash
       cd port-scanner
  ```
## Run the script:
   ```bash
    python PortScan.py
 ```
- Enter the target host (e.g., example.com or an IP address) and a port or port range (e.g., 80 or 80-100).
  

## Example
      Enter target host (e.g., example.com or IP): example.com
      Enter a single port or port range (e.g., 80 or 80-100): 80-85
      Scanning example.com for port(s): 80, 81, 82, 83, 84, 85...
      Open ports:
      Port 80 is open
      Scan completed in 2.34 seconds

## Code Structure
- scan_port(host, port, open_ports): Attempts to connect to a single port and adds it to open_ports if open.
- worker(host, port_queue, open_ports): Worker function for threads to process ports from the queue.
- port_scan(host, ports, num_threads=100): Main function to manage the scanning process with multiple threads.
- Input validation ensures ports are within the valid range (1-65535) and handles hostname resolution errors.

## Notes
- The default number of threads is 100, but this adjusts dynamically based on the number of ports to scan.
- The script uses a timeout of 1 second per port to balance speed and reliability.
- Be cautious when scanning hosts you do not own or have permission to scan, as unauthorized scanning may violate laws or terms of service.
# PortScanner
