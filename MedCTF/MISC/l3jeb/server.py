import os
import re
import socket

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def sanitize_path(user_input):
    sanitized = re.sub(r'\.\./', '', user_input)
    sanitized = re.sub(r'\.\.\\', '', sanitized)
    
    sanitized = sanitized.lstrip('/')
    sanitized = sanitized.lstrip('\\')
    
    sanitized = re.sub(r'/+', '/', sanitized)
    
    sanitized = re.sub(r'[^a-zA-Z0-9_\-./]', '', sanitized)
    
    return sanitized

def get_file_content(path):
    # Start from the public directory by default
    full_path = os.path.join(BASE_DIR, "public", path)
    
    # Basic security check
    if not full_path.startswith(BASE_DIR):
        return "Nice try! Access denied."
    
    try:
        if os.path.isdir(full_path):
            # List directory contents
            files = os.listdir(full_path)
            return "Directory contents:\n" + "\n".join(files)
        elif os.path.isfile(full_path):
            # Read file contents
            with open(full_path, 'r') as f:
                return f.read()
        else:
            return "File not found."
    except Exception as e:
        return f"Error accessing path: {str(e)}"

def handle_client(client_socket):
    try:
        client_socket.send(b"=== Path Traversal Challenge ===\n")
        client_socket.send(b"Enter a path to view (e.g. 'welcome.txt'): ")
        
        while True:
            # Receive client input
            data = client_socket.recv(1024).decode().strip()
            if not data:
                break
                
            # Log what was received and what it becomes after sanitization
            print(f"Received: {data}")
            sanitized_path = sanitize_path(data)
            print(f"Sanitized to: {sanitized_path}")
            
            # Get content for the sanitized path
            content = get_file_content(sanitized_path)
            
            # Send response
            # client_socket.send(f"\nAccessing: {sanitized_path}\n\n{content}\n\n".encode())
            client_socket.send(f"\content: {content}\n\n".encode())
            client_socket.send(b"Enter another path (or 'exit' to quit): ")
            
            if data.lower() == 'exit':
                break
                
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    host = '127.0.0.1'
    port = 9999
    
    server.bind((host, port))
    server.listen(5)
    print(f"[*] Listening on {host}:{port}")
    
    try:
        while True:
            client, addr = server.accept()
            print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
            handle_client(client)
    except KeyboardInterrupt:
        print("[*] Server shutting down")
    finally:
        server.close()

if __name__ == "__main__":
    start_server()

