import socket

def start_server():
    # Setup server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 1234))
    server.listen(1)
    print("[SERVER] Waiting for a client to connect...")

    conn, addr = server.accept()
    print(f"[SERVER] Connected to {addr}")

    while True:
        # Chat mode
        print("\n[SERVER] Waiting for a message or file...")
        data = conn.recv(1024).decode()
        
        if data.lower() == "exit":
            print("[SERVER] Client requested exit. Closing connection.")
            break
        
        elif data.lower() == "send file":
            print("[SERVER] Client wants to send a file. Preparing to receive...")
            conn.sendall(b"Ready for file")
            
            # Receive file size first
            file_size = int(conn.recv(1024).decode())
            print(f"[SERVER] Expecting file of size: {file_size} bytes")
            
            # Receive file data
            file_data = b""
            received = 0
            
            while received < file_size:
                chunk = conn.recv(4096)
                if not chunk:
                    break
                file_data += chunk
                received += len(chunk)
                print(f"[SERVER] Received {received}/{file_size} bytes")
            
            # Save the file
            with open("received_file.jpg", "wb") as f:
                f.write(file_data)
            
            print("[SERVER] File received and saved as 'received_file.jpg'")
            conn.sendall(b"File received successfully")
        
        else:
            print(f"[CLIENT]: {data}")
            response = input("[SERVER] Enter your reply (or 'exit' to quit): ")
            conn.sendall(response.encode())
            
            if response.lower() == "exit":
                print("[SERVER] Closing connection.")
                break
    
    conn.close()
    server.close()
    print("[SERVER] Server shut down.")

if __name__ == "__main__":
    start_server()