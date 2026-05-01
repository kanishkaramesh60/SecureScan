import socket
from scanner import scan_port
import services
import random
import time
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init

init()

# ⚠️ Ethical warning
print(Fore.YELLOW + "WARNING: Use only on authorized systems!" + Style.RESET_ALL)
confirm = input("Do you have permission? (yes/no): ")
if confirm.lower() != "yes":
    exit()

# Clear previous results
open("results.txt", "w").close()

# ⏱ Start time
start_time = time.time()

# 🎯 Input target
target = input("Enter target: ")
try:
    target_ip = socket.gethostbyname(target)
except:
    print(Fore.RED + "Invalid target!" + Style.RESET_ALL)
    exit()
start = 1
end = 1024 

# 📊 Counter
open_ports = 0

def run_scan(port):
    global open_ports
    try:
        time.sleep(random.uniform(0.05, 0.2))  # delay

        status, banner = scan_port(target_ip, port)

        if status == "OPEN":
            service = services.services.get(port, "Unknown")
            banner = banner if banner else "No banner"

            result = f"[+] Port {port:<5} | OPEN | {service:<10} | {banner}"

            # ✅ Colored output
            print(Fore.GREEN + result + Style.RESET_ALL)

            # Save to file
            with open("results.txt", "a") as f:
                f.write(result + "\n")

            open_ports += 1

    except:
        pass

# 🔀 Randomize ports
ports = list(range(start, end + 1))
random.shuffle(ports)

# ⚡ Multi-threading
with ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(run_scan, ports)

# ⏱ End time
end_time = time.time()

# 📊 Summary
print(Fore.CYAN + "\nScan completed!" + Style.RESET_ALL)
print(f"Total Open Ports: {open_ports}")
print(f"Time taken: {end_time - start_time:.2f} seconds")
print("Results saved in results.txt")