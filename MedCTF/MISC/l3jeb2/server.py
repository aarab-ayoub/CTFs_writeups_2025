import os
import re
import socket
import random
import threading

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def sanitize_path(user_input):
    sanitized = re.sub(r'(\.\./|\.\.\\)', '', user_input)
    sanitized = sanitized.lstrip('/\\')
    sanitized = re.sub(r'[/\\]+', '/', sanitized)
    sanitized = re.sub(r'[^\w\-./\\]', '', sanitized)
    if sanitized.startswith('.') and not any(c in sanitized for c in ['/', '\\']):
        sanitized = sanitized.lstrip('.')
    
    return sanitized

def get_file_content(path):
    full_path = os.path.join(BASE_DIR, "public", path)
    
    if not os.path.abspath(full_path).startswith(os.path.abspath(BASE_DIR)):
        return "Access denied: Path traversal attempt detected."
    
    try:
        if os.path.isdir(full_path):
            files = [f for f in os.listdir(full_path) if not f.startswith('.') or path.endswith('/' + f)]
            if not files:
                return "Directory is empty or you don't have permission to view its contents."
            return "Directory contents:\n" + "\n".join(files)
        elif os.path.isfile(full_path):
            with open(full_path, 'r') as f:
                content = f.read()
                if "fake" in content.lower() and random.randint(0, 3) == 0:
                    return "File exists but content is hidden."
                return content
        else:
            if "flag" in path.lower() and random.randint(0, 2) == 0:
                return "File not found."
            return "Path exists but is neither a file nor directory you can access."
    except PermissionError:
        return "Permission denied."
    except Exception as e:
        return f"Error accessing path: {str(e)}"

def handle_client(client_socket):
    try:
        client_socket.send(b"=== Path Traversal Challenge ===\n")
        client_socket.send(b"Enter a path to view (e.g. 'welcome.txt'): ")
        
        while True:
            data = client_socket.recv(1024).decode().strip()
            if not data:
                break
                
            if data.lower() == 'exit':
                break
                
            print(f"Received: {data}")
            sanitized_path = sanitize_path(data)
            print(f"Sanitized to: {sanitized_path}")
            
            content = get_file_content(sanitized_path)
            
            # Obfuscate the response a bit
			
            response = f"\ncontent: {content}\n\n" if random.randint(0, 1) == 0 else f"\ndata: {content}\n\n"
            client_socket.send(f"\nAccessing: {sanitized_path}\n\n{content}\n\n".encode())
            client_socket.send(response.encode())
            client_socket.send(b"Enter another path (or 'exit' to quit): ")
            
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    host = '0.0.0.0'
    port = 9999
    
    server.bind((host, port))
    server.listen(5)
    print(f"[*] Listening on {host}:{port}")
    
    try:
        while True:
            client, addr = server.accept()
            print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
            
            client_thread = threading.Thread(target=handle_client, args=(client,))
            client_thread.daemon = True  
            client_thread.start()
    except KeyboardInterrupt:
        print("[*] Server shutting down")
    finally:
        server.close()

if __name__ == "__main__":
    start_server()