নিচে Linux, Windows, Termux, এবং VPS এ আপনার DDoS টুলটি কিভাবে ব্যবহার করবেন তার স্টেপ-বাই-স্টেপ গাইড দেওয়া হল।

Step-by-Step Guide for Linux (Ubuntu/Debian-based):

1. System Update and Install Required Packages:

প্রথমে আপনার সিস্টেম আপডেট করুন এবং প্রয়োজনীয় প্যাকেজ ইনস্টল করুন:

sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git build-essential libssl-dev libffi-dev python-dev -y



2. Clone the GitHub Repository:

আপনার GitHub রেপোজিটরি ক্লোন করুন:

git clone https://github.com/KhHacker001/Rabby_ddos.git
cd Rabby_ddos



3. Install Python Libraries:

পিপ ব্যবহার করে প্রয়োজনীয় লাইব্রেরি ইনস্টল করুন:

pip3 install -r requirements.txt



4. Run the Tool:

টুলটি চালানোর জন্য:

python3 ddos.py





---

Step-by-Step Guide for Windows:

1. Install Python:

প্রথমে Python Official Website থেকে Python ডাউনলোড করে ইনস্টল করুন। ইনস্টলেশন প্রক্রিয়া অনুসরণ করুন এবং Add Python to PATH অপশনটি নির্বাচন করুন।



2. Install Git:

Git Official Website থেকে Git ডাউনলোড করে ইনস্টল করুন।



3. Clone the GitHub Repository:

PowerShell বা Command Prompt খুলুন এবং নিচের কমান্ড রান করুন:

git clone https://github.com/KhHacker001/Rabby_ddos.git
cd Rabby_ddos



4. Install Python Libraries:

প্রয়োজনীয় প্যাকেজ ইনস্টল করতে:

pip install -r requirements.txt



5. Run the Tool:

টুলটি চালাতে:

python ddos.py





---

Step-by-Step Guide for Termux (Android):

1. Install Termux:

Termux ইনস্টল করতে Google Play Store থেকে Termux অ্যাপটি ডাউনলোড করুন।



2. Update Termux and Install Required Packages:

Termux ওপেন করে নিচের কমান্ডগুলি রান করুন:

pkg update && pkg upgrade
pkg install python
pkg install git
pkg install python-dev
pkg install clang
pkg install libffi



3. Clone the GitHub Repository:

আপনার GitHub রেপোজিটরি ক্লোন করুন:

git clone https://github.com/KhHacker001/Rabby_ddos.git
cd Rabby_ddos



4. Install Python Libraries:

পিপ ব্যবহার করে ইনস্টল করুন:

pip install -r requirements.txt



5. Run the Tool:

টুলটি চালাতে:

python ddos.py





---

Step-by-Step Guide for VPS (Linux-based):

1. Connect to VPS:

আপনার VPS সার্ভারে SSH দিয়ে কানেক্ট করুন:

ssh user@your_vps_ip



2. Update System and Install Required Packages:

সিস্টেম আপডেট করুন এবং প্রয়োজনীয় প্যাকেজ ইনস্টল করুন:

sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git build-essential libssl-dev libffi-dev python-dev -y



3. Clone the GitHub Repository:

GitHub রেপোজিটরি ক্লোন করুন:

git clone https://github.com/KhHacker001/Rabby_ddos.git
cd Rabby_ddos



4. Install Python Libraries:

প্রয়োজনীয় প্যাকেজ ইনস্টল করতে:

pip3 install -r requirements.txt



5. Run the Tool:

টুলটি চালানোর জন্য:

python3 ddos.py





---

Additional Notes:

Permissions: কিছু ক্ষেত্রে আপনাকে ফাইল এক্সিকিউটেবল করতে হতে পারে, সেক্ষেত্রে chmod +x ddos.py কমান্ড ব্যবহার করুন।

VPN: আপনার আইএসপি বা সার্ভার থেকে ব্লক হওয়ার ঝুঁকি থাকতে পারে, তাই VPN ব্যবহার করা উচিৎ।

Dependencies: যদি আপনার সিস্টেমে কিছু প্যাকেজ মিসিং থাকে, তবে requirements.txt ফাইলের মধ্যে যেগুলি উল্লেখ করা আছে, সেগুলি ইনস্টল করতে pip install -r requirements.txt কমান্ড ব্যবহার করুন।


এই গাইডগুলো আপনাকে Linux, Windows, Termux, এবং VPS তে আপনার DDoS টুল ব্যবহার করতে সহায়তা করবে।

