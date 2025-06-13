import socket
import os

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 1234))  # Replace with server IP if needed
    
    while True:
        # Chat mode
        message = input("[CLIENT] Enter your message (or 'send file' / 'exit'): ")
        client.sendall(message.encode())
        
        if message.lower() == "exit":
            print("[CLIENT] Closing connection.")
            break
        
        elif message.lower() == "send file":
            # Check if server is ready
            response = client.recv(1024).decode()
            if response == "Ready for file":
                file_path = input("[CLIENT] Enter file path to send: ")
                
                if not os.path.exists(file_path):
                    print("[CLIENT] File not found!")
                    continue
                
                # Send file size first
                file_size = os.path.getsize(file_path)
                client.sendall(str(file_size).encode())
                
                # Send file in chunks
                with open(file_path, "rb") as f:
                    bytes_sent = 0
                    while bytes_sent < file_size:
                        chunk = f.read(4096)
                        client.sendall(chunk)
                        bytes_sent += len(chunk)
                        print(f"[CLIENT] Sent {bytes_sent}/{file_size} bytes")
                
                # Check server confirmation
                confirmation = client.recv(1024).decode()
                print(f"[SERVER]: {confirmation}")
        
        else:
            # Normal chat reply
            reply = client.recv(1024).decode()
            print(f"[SERVER]: {reply}")
            
            if reply.lower() == "exit":
                print("[CLIENT] Server closed the connection.")
                break
    
    client.close()
    print("[CLIENT] Connection closed.")

if __name__ == "__main__":
    start_client()