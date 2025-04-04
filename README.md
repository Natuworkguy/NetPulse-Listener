# NetPulse Listener

**NetPulse Listener** is a minimalistic Python-based HTTP server built for quick response testing, diagnostics, and scripting use cases. It supports plain text responses, custom ports, and flexible runtime flags – making it perfect for local testing, IoT triggers, webhook simulations, and more.

---

## 🚀 Features

- 🛑 **Single-use or Continuous** — Handles one request and exits by default, or keeps listening with the `-c` flag.  
- 📂 **Custom Response Files** — Serve the contents of any `.txt`, `.json`, or other plain text file using the `-r` flag.  
- 🌐 **Custom Ports** — Listen on any port you choose via `-p`.  
- 🔀 **Flexible Flag Combinations** — Combine flags (`-cp 8080 -r file.txt`) for ultimate control.  
- 💡 **Zero Dependencies** — Runs on pure Python 3. Clean and fast.  

---

## ⚙️ Usage

### 🔧 Basic Syntax

```bash
python netpulse.py [-c] [-p <port>] [-r <file>]
```

### 🧪 Examples

| Command | Description |
|--------|-------------|
| `python netpulse.py` | Start the server on port 81. Stops after the first request. |
| `python netpulse.py -c` | Start on port 81 and stay active after each request. |
| `python netpulse.py -p 8080` | Start on port 8080. |
| `python netpulse.py -r response.txt` | Send `response.txt` as the response body. |
| `python netpulse.py -cp 8080 -r hello.txt` | Combine all features: custom port, continuous mode, and file response. |

---

## 📄 Default Response

```plaintext
NetPulse Listener works!
```

(Or the contents of a file if `-r <FILE>` is used.)

---

## ✅ Requirements

- Python 3.x  
### Modules
- colorama
- socket
---

## 📜 License

MIT License – free to use, modify, and share.

---

## ❤️ Author

Built by **Natuworkguy**
