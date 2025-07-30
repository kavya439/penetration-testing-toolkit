# penetration-testing-toolkit
COMPANY: CODTECH IT SOLUTIONS

NAME: P.KAVYANJALI

INTERN ID: CT06DZ757

DOMAIN: CYBER SECURITY & ETHICAL HACKING

DURATION: 6 WEEKS

MENTOR: NEELA SANTHOSH KUMAR

DESCRIPTION:

This Python script is a basic penetration testing toolkit featuring two main tools: a port scanner and a simulated brute-force password cracker. It helps users understand how security testers identify potential weaknesses in systems. The toolkit operates through a simple menu, letting users choose which tool to run, making it easy to explore fundamental security concepts.

The port scanner works by checking a range of ports on a target IP address or hostname to see which ones are open. Open ports indicate active services that could potentially be accessed over the network. Users input the target and specify ports or port ranges, and the scanner attempts connections to each specified port. It then reports which ports are open, helping users understand how network services are discovered during security assessments.How the port scanner works is fairly straightforward. The user is prompted to enter the target system’s IP address or hostname, such as 192.168.1.1 or example.com. Then, the user specifies which ports or port ranges to scan — for instance, a list like 22, 80, 443 or a range like 1-1024. The toolkit processes this input and attempts to connect to each port on the target using TCP connections. If a connection to a port is successful, that port is marked as open and reported back to the user. This process mimics how real-world security professionals gather information about active services on a network during a penetration test or vulnerability assessment. By identifying open ports, users can see which parts of a system might need closer inspection or additional protection.

The simulated brute-force password cracker models how password guessing attacks occur by checking a list of possible passwords against a preset correct password. Users provide a file with candidate passwords, and the tool tries each one in turn, reporting success if the correct password is found. This simulation demonstrates the importance of strong, unique passwords and how attackers attempt to breach systems by systematically guessing credentials.The tool reads this file and tries each password against a predefined “correct” password stored within the script. Each attempt is displayed, and if a match is found, the program notifies the user of success. If the password is not found in the list, it indicates failure. This helps users understand why it’s important to use strong, unique passwords that are not easily guessable or found in common password lists.The script also includes a user-friendly menu to choose between running the port scanner, the brute-force simulation, or exiting the program. It features input validation and error handling to guide users and prevent crashes.

It provides hands-on experience with common penetration testing tasks in a safe environment. By understanding how port scanning and password guessing work, users can better appreciate the importance of securing network services and choosing strong passwords, which are critical steps in protecting systems from potential attacks.
