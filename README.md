# 🛡️ Security Toolkit

A lightweight desktop security and developer utility application built with **Python and PySide6 (Qt for Python)**.

Security Toolkit is a learning-focused project designed to explore how modern Windows desktop applications can be built with Python, while providing several practical security and networking utilities.

## ✨ Features

### 🔍 Port Scanner

Scan TCP ports on a system you own or are authorized to test.

* Enter an IP address or hostname
* Specify ports to scan
* Detect open and closed TCP ports
* Basic hostname resolution
* Input validation

### #️⃣ Hash Tool

Generate cryptographic hashes from text.

Supported algorithms:

* MD5
* SHA-1
* SHA-224
* SHA-256
* SHA-384
* SHA-512

### 🌐 IP Lookup

Resolve a hostname to an IP address using Python's networking capabilities.

Example:

```text
example.com → IP address
```

### 🖥️ Desktop GUI

The application uses **PySide6 / Qt** for its graphical interface.

The interface includes:

* Sidebar navigation
* Multiple application pages
* Input fields
* Buttons
* Result panels
* Dark theme support through Qt Style Sheets

### 🚀 Windows Portable Executable

The application can be packaged into a standalone Windows executable using **PyInstaller**.

A one-file build can be distributed as:

```text
SecurityToolkit.exe
```

Python does not need to be installed on the user's computer.

The application also uses a PyInstaller splash screen to provide visual feedback while the one-file executable is being extracted and started.

---

# 🧱 Project Architecture

The project separates the graphical interface from the actual application logic.

```text
SecurityToolkit
│
├── main.py
│
├── ui/
│   ├── main_window.py
│   ├── dashboard_page.py
│   ├── port_scanner_page.py
│   ├── hash_tool_page.py
│   ├── ip_lookup_page.py
│   └── settings_page.py
│
├── tools/
│   ├── port_scanner.py
│   ├── hash_tool.py
│   └── ip_lookup.py
│
└── styles/
    └── theme.qss
```

### Architecture

```text
                main.py
                   │
                   ▼
              MainWindow
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
    Dashboard   Port Scan   Hash Tool
                   │          │
                   ▼          ▼
             port_scanner  hash_tool
                 .py          .py

                   │
                   ▼
               IP Lookup
                   │
                   ▼
              ip_lookup.py
```

The `ui/` directory contains Qt interface components, while `tools/` contains the underlying Python functionality.

This separation makes it easier to add new tools without turning the main application into one large file.

---

# 🛠️ Technologies Used

| Technology            | Purpose                                            |
| --------------------- | -------------------------------------------------- |
| Python                | Application logic                                  |
| PySide6               | Qt GUI framework                                   |
| Qt Widgets            | Desktop interface                                  |
| Qt Style Sheets (QSS) | Application styling                                |
| `socket`              | Network communication and hostname resolution      |
| `hashlib`             | Hash generation                                    |
| PyInstaller           | Windows executable packaging                       |
| Pillow                | Image processing for the PyInstaller splash screen |

---

# 📦 Installation

## Run from source

Make sure Python is installed, then install the dependencies:

```bash
pip install PySide6 Pillow
```

Run the application:

```bash
python main.py
```

---

# 🪟 Build the Windows EXE

Install PyInstaller:

```bash
python -m pip install pyinstaller
```

Build the portable executable:

```bash
python -m PyInstaller --windowed --onefile --name SecurityToolkit --add-data "styles;styles" --splash "splash.png" --icon "icon.ico" main.py
```

The executable will be created at:

```text
dist/SecurityToolkit.exe
```

The `--onefile` option packages the application into a single executable, making it convenient to carry or distribute.

---

# 🎯 Use Cases

Security Toolkit can be used for:

* Learning Python desktop development
* Learning PySide6 and Qt
* Understanding GUI architecture
* Practicing network programming
* Testing TCP connectivity on authorized systems
* Generating hashes
* Performing basic hostname/IP resolution
* Learning application packaging for Windows

This project is primarily intended as a **learning and development project**.

### ⚠️ Responsible Use

Only use networking and scanning functionality against systems you own or have explicit permission to test.

Do not use the port scanner against systems or networks without authorization.

---

# 🧠 What This Project Teaches

This project was built to learn the fundamentals of creating a real desktop application with Python.

Topics covered include:

* Python application structure
* Object-oriented programming
* PySide6 widgets
* Qt layouts
* Signals and slots
* Event-driven programming
* Component separation
* UI and logic separation
* Network sockets
* Hashing
* Input validation
* Qt Style Sheets
* Windows application icons
* Splash screens
* PyInstaller packaging
* Portable Windows executables

---

# 🔮 Future Improvements

Possible future features include:

* Dark/light theme switching
* DNS lookup
* Subnet calculator
* Password generator
* File hash calculator
* Base64 encoder/decoder
* HTTP request tester
* System information
* Better port scanner with background workers
* Scan progress indicators
* Export scan results
* More polished UI
* Windows installer
* Application settings
* Logging


# 📄 License

This project is available under the MIT License.
