import socket
import threading
import time

# Function to handle client connections
def handle_client(client_socket, address):
    print(f"Accepted connection from {address}")

    while True:
        # Send stock value to the client
        client_socket.send(str(stock_value).encode())

        # Sleep for 2 minutes before updating stock value
        time.sleep(120)

# Function to update stock value
def update_stock_value():
    global stock_value
    while True:
        # Simulate updating stock value
        stock_value += 1
        print(f"Updated stock value: {stock_value}")

        # Sleep for 2 minutes
        time.sleep(120)

# Server configuration
host = "127.0.0.1"
port = 8888

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)
print(f"Server listening on {host}:{port}")

# Global variable for stock value
stock_value = 100

# Start a thread to update stock value
update_thread = threading.Thread(target=update_stock_value)
update_thread.start()

while True:
    # Accept a connection from a client
    client_socket, addr = server_socket.accept()

    # Start a new thread to handle the client
    client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_handler.start()
