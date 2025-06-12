import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Creates TCP socket using IPv4 adddressing

server.bind(('0.0.0.0',1234))# binds all available ipaddress to port of the server,1234 #
server.listen(1) #waits for and accepts a client connection,deliver to 1 connection at a time
print("Hello, waiting.")# displays the message

conn, addr = server.accept()# connection line
print(f"Connection from {addr}")# Prints client address when connected

size_data = conn.recv(1024)
picture_size = int(size_data.decode()) #translates from computer language to human language
print(f"Picture size;{picture_size} bytes")
conn.sendall(b"Ready for picture")
picture_data = b"" 
bytes_received = 0

while bytes_received < picture_size:
    chunck = conn.recv(4096) #Receives picture data in chunks, 4096 bytes at a time
    if not chunck:
     break
    picture_data += chunck
    bytes_received += len(chunck)
    print(f"Received{bytes_received} bytes out of {picture_size} bytes")
    print("Picture received successfully")

with open("received_picture.jpg", "wb") as f:
    f.write(picture_data) # writes the received data to received_picture.jpg

print("Picture saved as 'received_picture.jpg'")
conn.sendall(b"Picture received successfully")
conn.close()

# Create an open chatroom with the client , closes the communication and share files