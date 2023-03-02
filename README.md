# Keylogger via Socket + Rubber Ducky (optional)

The goal of this project is made by steps :
1. Starting a python Web server
2. Starting socket server, waiting for keylogger connection
3. Key is powered up
4. The Key install a keyboard driver on the victim computer
5. The key download the VBS Script available on the web server
6. Execute VBS Script :
    a. Download & Install Python and Modules (pywin32 and pynput)
    b. Download keylogger to Windows startup folder, so it will launch everytime the victim start his PC
    C. Execute keylogger
7. Keylogger communicate with the socket server

This project has been done with a Raspberry pi zero as a Rubber Ducky

### 1. Starting a python webserver
```
python3 -m http.server
```

### 2. Starting socket server, waiting for keylogger connection
```
python3 Striker/server.py
```

### 3. Key is powered up (if using Rubber Ducky)
Key configuration :
- P4wnPi (OS) : https://github.com/RoganDawes/P4wnP1
- DuckyScript : ducky.txt (Module used : hid_keyboard.txt)

### 4. The Key install a keyboard driver on the victim computer (if using Rubber Ducky)
Modify : 
- P4wnP1/setup.cfg : USE_HID=true
- P4wnP1/setup.cfg : #PAYLOAD=network_only.txt
- P4wnP1/setup.cfg : PAYLOAD=hid_keyboard.txt

### 5. Start keylogger
```
python3 Target/keylogger.py
```