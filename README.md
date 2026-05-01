🔐 SecureScan

SecureScan is a multi-threaded TCP port scanner developed in Python for network reconnaissance and security analysis.
It is designed to identify open ports, detect services, and retrieve banners efficiently while maintaining a clean and user-friendly output.

🚀 Features
• ⚡ Multi-threaded scanning for faster performance
• 🎯 Automatic port scanning (common ports or defined range)
• 🔍 Service detection using port mapping
• 📡 Banner grabbing for additional information
• 🛡 Basic stealth techniques (randomized ports + delay)
• 📂 Result logging to file (results.txt)
• 🎨 Colored CLI output for better readability
• ⏱ Scan summary with time tracking

🧠 How It Works

SecureScan uses TCP connect scanning:
1. Resolves the target domain/IP
2. Attempts connection to each port using sockets
3. Identifies port status:
    • OPEN
    • CLOSED
    • FILTERED
4. Retrieves service name and banner (if available)
5. Displays and logs results

📁 Project Structure
SecureScan/
│
├── main.py        # Main execution file
├── scanner.py     # Core scanning logic
├── services.py    # Port-to-service mapping
├── results.txt    # Output file (generated after scan)
└── README.md      # Project documentation

▶️ How to Run
🔹 Requirements
    • Python 3.x
    • Install dependencies:
pip install colorama
🔹 Run the Scanner
python main.py
🔹 Example Input
Enter target: 127.0.0.1
🔹 Example Output
[+] Port 80    | OPEN | HTTP       | HTTP/1.1 200 OK
[+] Port 22    | OPEN | SSH        | SSH-2.0-OpenSSH_8.2

Scan completed!
Total Open Ports: 2
Time taken: 2.45 seconds
⚠️ Ethical Use

This tool is intended only for educational purposes.

Do NOT use SecureScan on:

• Unauthorized networks
• Systems without permission

Unauthorized scanning may be illegal.

⚙️ Technologies Used
• Python
• Socket Programming
• Threading (concurrent.futures)
📊 Limitations
• Uses TCP connect scan only
• Cannot bypass firewalls or IDS
• Banner grabbing may not always return results
🚀 Future Enhancements
• GUI interface (Tkinter)
• CLI argument support
• UDP scanning
• OS detection
• Vulnerability scanning

👨‍💻 Author
Developed as a cybersecurity project by Kanishka R

🏁 Conclusion
SecureScan demonstrates core concepts of network scanning, combining performance, usability, and basic stealth techniques into a simple yet effective tool.
