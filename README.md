````markdown
# 🔍 Python Port Scanner

A multithreaded TCP port scanner written in Python.

This project scans an entire **/24 subnet** for open TCP ports using Python's `socket` module and `ThreadPoolExecutor` for concurrent scanning.

---

## ✨ Features

- 🌐 Resolve a hostname to its IP address
- 📡 Scan every host in a **/24 network**
- 🔎 Scan a custom range of TCP ports
- ⚡ Multithreaded scanning with `ThreadPoolExecutor`
- ⏱ Measure total scan time
- 🛠 Simple command-line interface

---

## 📚 Technologies

- Python 3
- socket
- concurrent.futures
- ipaddress
- time

---

## 📂 Project Structure

```text
Port_scanner.py
```

---

## 🚀 Usage

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

Example output:

```text
[+] TCP PORT 80 IS OPEN ON 142.250.xxx.xxx
[+] TCP PORT 443 IS OPEN ON 142.250.xxx.xxx

Finished in 2.34 second(s)
```

---

## ⚙️ How It Works

1. The program asks for a hostname.
2. The hostname is resolved to an IPv4 address.
3. A `/24` network is generated using the `ipaddress` module.
4. Every host in the subnet is scanned.
5. Every selected TCP port is checked using `socket.connect_ex()`.
6. Open ports are displayed.
7. The total execution time is printed.

---

## 📌 Current Limitations

- TCP scanning only
- IPv4 only
- Fixed `/24` subnet
- No banner grabbing
- No service detection
- Command-line interface only

---

## 🔮 Planned Improvements

- [ ] Banner grabbing
- [ ] Service/version detection
- [ ] UDP scanning
- [ ] CIDR support (`/16`, `/24`, `/28`, etc.)
- [ ] Save results to JSON/CSV
- [ ] Command-line arguments (`argparse`)
- [ ] Configurable thread count
- [ ] Colored terminal output
- [ ] Better exception handling
- [ ] Progress bar

---

## 📖 Educational Purpose

This project was created to practice:

- Python networking
- Multithreading
- TCP sockets
- IP addressing
- Concurrent programming

---

## 📜 License

This project is intended for **educational and authorized security testing only**.

Please use it responsibly and only on systems you own or have permission to test.
````
