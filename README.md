# RTN_monitoring
Real-Time Network Monitoring Tool Python-Linux
# 🛰 Real-Time Network Monitoring Tool (Linux, Python)

A lightweight, real-time **network monitoring tool** built with **Python** for Linux.  
Tracks **bandwidth usage**, **active connections**, and **packet details** in a simple CLI dashboard.  

---

## ✨ Features
- 📡 Real-time bandwidth usage per network interface  
- 🔍 Packet capture & inspection (via `scapy`)  
- 🌐 List active TCP/UDP connections  
- 👨‍💻 Optional per-process bandwidth usage (via `psutil`)  
- 📊 Beautiful CLI dashboard using `rich`  
- 📂 Export logs to JSON/CSV  

---

## 🛠 Tech Stack
- **Language**: Python 3.x  
- **Libraries**:  
  - [`psutil`](https://pypi.org/project/psutil/) → Network stats & per-process I/O  
  - [`scapy`](https://scapy.net/) → Packet sniffing & parsing  
  - [`rich`](https://github.com/Textualize/rich) → CLI dashboard (colorful UI)  
  - [`Flask`](https://flask.palletsprojects.com/) (optional) → Web dashboard  

---

## UNDER PROGRESS !!
