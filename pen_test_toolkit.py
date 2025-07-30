import socket
import re # For parsing port ranges

# --- Port Scanner Functions ---
def parse_port_range(port_string):
    """
    Parses a string like '1-1024' or '80,443' into a list of integers.
    Returns a sorted list of unique port numbers.
    """
    ports = set()
    parts = port_string.split(',')
    for part in parts:
        part = part.strip()
        if not part:
            continue
        if '-' in part:
            try:
                start, end = map(int, part.split('-'))
                if not (1 <= start <= 65535 and 1 <= end <= 65535 and start <= end):
                    raise ValueError("Port range out of valid range (1-65535) or invalid order.")
                ports.update(range(start, end + 1))
            except ValueError as e:
                print(f"Skipping invalid port range '{part}': {e}")
                continue
        else:
            try:
                port = int(part)
                if not (1 <= port <= 65535):
                    raise ValueError("Port number out of valid range (1-65535).")
                ports.add(port)
            except ValueError as e:
                print(f"Skipping invalid port '{part}': {e}")
                continue
    return sorted(list(ports))

def scan_single_port(target_ip, port_number, timeout=1):
    """
    Tries to connect to a specific port on a target IP.
    Returns True if the port is open, False otherwise.
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        result = s.connect_ex((target_ip, port_number))
        s.close()
        return result == 0  # 0 means connection successful (port open)
    except socket.gaierror:
        # This occurs if the hostname/IP cannot be resolved
        print(f"Error: Hostname '{target_ip}' could not be resolved.")
        return False
    except socket.error as e:
        # General socket errors (e.g., "No route to host", "Connection refused")
        print(f"Socket error for {target_ip}:{port_number}: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred during scan for {target_ip}:{port_number}: {e}")
        return False

def run_port_scanner():
    """
    Handles the user interaction and execution for the port scanner.
    """
    print("\n--- Running Port Scanner ---")
    while True:
        target = input("Enter the target IP address or hostname (e.g., 127.0.0.1, example.com): ").strip()
        if not target:
            print("Target cannot be empty. Please try again.")
            continue
        break

    while True:
        ports_input = input("Enter port(s) to check (e.g., 80, 443, 22-100, 1-1024): ").strip()
        if not ports_input:
            print("Port(s) cannot be empty. Please try again.")
            continue
        ports_to_scan = parse_port_range(ports_input)
        if not ports_to_scan:
            print("No valid ports found in your input. Please try again.")
            continue
        break

    print(f"\n[*] Starting scan on {target} for ports: {', '.join(map(str, ports_to_scan))}")
    open_ports = []
    
    # Try to resolve hostname once
    try:
        target_ip_resolved = socket.gethostbyname(target)
        print(f"[*] Resolved {target} to {target_ip_resolved}")
    except socket.gaierror:
        print(f"Error: Could not resolve hostname '{target}'. Exiting port scan.")
        return
    except Exception as e:
        print(f"An unexpected error occurred resolving hostname: {e}")
        return

    for port in ports_to_scan:
        if scan_single_port(target_ip_resolved, port):
            print(f"[+] Port {port} is OPEN")
            open_ports.append(port)
        # else:
        #     print(f"[-] Port {port} is CLOSED") # Uncomment for very verbose output

    if open_ports:
        print(f"\n[*] Scan complete. Open ports on {target}: {', '.join(map(str, open_ports))}")
    else:
        print(f"\n[*] Scan complete. No open ports found on {target} within the specified range.")
    print("--- Port Scan Finished ---")


# --- Simple Brute-Forcer tool (simulated) ---
def simple_brute_force(correct_password, wordlist_file):
    """
    This function simulates trying passwords from a wordlist.
    It does NOT connect to any real service.
    """
    print(f"\n--- Simple Brute-Forcer (Simulated) ---")
    print(f"Trying to guess the password (simulated) using wordlist: {wordlist_file}")

    try:
        with open(wordlist_file, 'r') as f: # Open the wordlist file for reading
            passwords = f.readlines() # Read all lines (passwords) into a list

        found = False
        for i, password in enumerate(passwords):
            password = password.strip() # Remove any extra spaces or newlines
            if not password: # Skip empty lines
                continue
            
            print(f"Attempt {i+1}: Trying password '{password}'...")

            if password == correct_password:
                print(f"SUCCESS! The simulated password is: '{password}'")
                found = True
                break # Stop trying once found

        if not found:
            print("FAILURE: Password not found in the provided wordlist.")

    except FileNotFoundError:
        print(f"Error: Wordlist file '{wordlist_file}' not found.")
        print(f"Please ensure '{wordlist_file}' is in the same directory as this script.")
    except Exception as e:
        print(f"An error occurred during brute-forcing: {e}")
    print("--- Brute-Force Simulation Finished ---")

def run_brute_forcer():
    """
    Handles the user interaction and execution for the simulated brute-forcer.
    """
    print("\n--- Running Simple Brute-Forcer (Simulated) ---")
    
    # For this simulation, let's set a "correct" password
    actual_password = "secretpassword" # You can change this for testing

    wordlist_name = "passwords.txt"

    # Instructions on how to create passwords.txt
    print(f"\n*** IMPORTANT: Create '{wordlist_name}' for Brute-Forcer ***")
    print(f"1. Create a text file named '{wordlist_name}' in the same folder as this script.")
    print(f"2. Inside '{wordlist_name}', put one password on each line.")
    print(f"   Example content for '{wordlist_name}':")
    print(f"     password123")
    print(f"     testpass")
    print(f"     {actual_password}  <-- Make sure this 'actual_password' is in your list to see a SUCCESS!")
    print(f"     123456")
    print(f"     admin")
    print(f"     ...")
    input("Press Enter once you have created 'passwords.txt' with some passwords (including the correct one for success).")

    simple_brute_force(actual_password, wordlist_name)

# --- Main Program Loop and Menu ---
def main_menu():
    """
    Displays the main menu and handles user choices.
    """
    print("\n" + "="*40)
    print("=== Simple Penetration Testing Toolkit ===")
    print("="*40)

    while True:
        print("\nChoose a tool to run:")
        print("1. Port Scanner (Scan for open ports)")
        print("2. Simple Brute-Forcer (Simulated password guessing)")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ").strip()

        if choice == '1':
            run_port_scanner()
        elif choice == '2':
            run_brute_forcer()
        elif choice == '3':
            print("Exiting Toolkit. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
        
        input("\nPress Enter to return to the main menu...") # Pause before showing menu again

if __name__ == "__main__":
    main_menu()