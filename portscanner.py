import socket

def scan_ports(target):
    open_ports = []
    
    print(f"Scanning ports on {target}...")
    
    # Ask user if they want to scan specific ports or all ports
    user_choice = input("Do you want to scan specific ports (1) or all ports (2)? Enter 1 or 2: ").strip()

    if user_choice == "1":
        # Scan specific ports
        ports = []
        print("Specify the ports you want to scan.")
        
        while True:
            try:
                # Get port from user
                port = int(input("Enter a port to scan (0-65535): "))
                
                # Check if the port is valid
                if 0 <= port <= 65535:
                    ports.append(port)  # Add port to list
                else:
                    print("Invalid port. Please enter a number between 0 and 65535.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
            
            # Ask user if they want to add more ports
            cont = input("Do you want to add another port? (yes/no): ").strip().lower()
            if cont == "no":  # Break loop if user says no
                break
        
        # Scan the specified ports
        for port in ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)  # Set timeout for faster scanning
                result = sock.connect_ex((target, port))  # Attempt to connect to the port
                if result == 0:
                    print(f"Port {port} is open.")
                    open_ports.append(port)
                sock.close()
            except socket.error as e:
                print(f"Error scanning port {port}: {e}")
    
    elif user_choice == "2":
        # Scan all ports from 0 to 65535
        print("Scanning all ports from 0 to 65535...")
        
        for port in range(0, 65536):  # Scan from port 0 to 65535
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)  # Timeout for faster scanning
                result = sock.connect_ex((target, port))  # Attempt to connect to the port
                if result == 0:
                    print(f"Port {port} is open.")
                    open_ports.append(port)
                sock.close()
            except socket.error as e:
                print(f"Error scanning port {port}: {e}")
    
    else:
        print("Invalid choice. Please enter 1 or 2.")

    print("Scan complete.")
    if open_ports:
        print(f"Open ports: {open_ports}")
    else:
        print("No open ports found.")

# Main execution
target_host = input("Enter the domain or IP address you want to scan: ")
scan_ports(target_host)
