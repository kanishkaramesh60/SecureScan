import socket

def grab_banner(sock):
    try:
        return sock.recv(1024).decode().strip()
    except:
        return "No banner"

def scan_port(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    
    try:
        result = s.connect_ex((target, port))
        
        if result == 0:
            banner = grab_banner(s)
            return "OPEN", banner
        elif result == 111:
            return "CLOSED", None
        else:
            return "FILTERED", None
    
    except:
        return "ERROR", None
    
    finally:
        s.close()