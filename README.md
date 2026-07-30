````markdown
# Python Port Scanner

A simple multithreaded TCP port scanner written in Python.

## About

This program scans TCP ports on all hosts in a `/24` network.

The scanner:

- Resolves a hostname to an IPv4 address
- Generates a `/24` subnet using the `ipaddress` module
- Scans a user-defined range of TCP ports
- Uses multithreading with `ThreadPoolExecutor`
- Displays all open TCP ports
- Measures the total scan time

## Modules

- socket
- concurrent.futures
- ipaddress
- time

## Usage

Run the program:

```bash
python Port_scanner.py
```

Example:

```text
[*] Enter a host (Example: google.com): google.com
[*] Enter start_port: 20
[*] Enter end_port: 100
```

Output:

```text
[+] TCP PORT 80 IS OPEN ON 142.250.xxx.xxx
[+] TCP PORT 443 IS OPEN ON 142.250.xxx.xxx

Finished in 2.34 second(s)
```

## Features

- Hostname resolution
- TCP port scanning
- Custom port range
- Scan an entire `/24` subnet
- Multithreaded scanning

## Future Improvements

- Better error handling
- Configurable thread count
- Command-line arguments
- Support for different subnet sizes
- Service detection
- Banner grabbing

## Disclaimer

This project was created for educational purposes.

Use it only on systems you own or have permission to test.
````
