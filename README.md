
Step-by-Step Guide for Termux (Android):

1. Termux ইনস্টল করুন:

Termux ইনস্টল করতে Play Store থেকে Termux অ্যাপটি ডাউনলোড এবং ইনস্টল করুন।



2. Termux আপডেট এবং প্রয়োজনীয় প্যাকেজ ইনস্টল করুন:

Termux ওপেন করে নিম্নলিখিত কমান্ডগুলি রান করুন:

pkg update && pkg upgrade
pkg install python
pkg install git
pkg install python-dev
pkg install clang
pkg install libffi



3. GitHub রেপোজিটরি ক্লোন করুন:

আপনার GitHub রিপোজিটরি ক্লোন করতে নিম্নলিখিত কমান্ডটি রান করুন:

git clone https://github.com/KhHacker001/Rabby_ddos.git
cd Rabby_ddos



4. Python লাইব্রেরি ইনস্টল করুন:

সমস্ত নির্ভরতা ইনস্টল করার জন্য নিচের কমান্ডটি রান করুন:

pip install -r requirements.txt



5. অ্যাকসেস করার অনুমতি দিন:

আক্রমণ চালানোর জন্য ইনপুট এবং আউটপুট ফাইলগুলো লিখতে অনুমতি দেওয়া হতে পারে। নিচের কমান্ডটি রান করুন:

chmod +x ddos.py



6. টুল চালু করুন:

এরপর আপনি টুলটি চালাতে পারেন:

python ddos.py





---

Step-by-Step Guide for Linux (Ubuntu/Debian-based):

1. System Update and Required Packages:

প্রথমে আপনার সিস্টেম আপডেট করুন এবং প্রয়োজনীয় প্যাকেজ ইনস্টল করুন:

sudo apt update && sudo apt upgrade
sudo apt install python3 python3-pip git
sudo apt install build-essential libssl-dev libffi-dev python-dev



2. Clone the GitHub Repository:

এরপর আপনার GitHub রেপোজিটরি ক্লোন করুন:

git clone https://github.com/KhHacker001/Rabby_ddos.git
cd Rabby_ddos



3. Install Python Libraries:

ইনস্টল করতে পিপের মাধ্যমে লাইব্রেরি ইনস্টল করুন:

pip3 install -r requirements.txt



4. Run the Tool:

এখন আপনি টুলটি চালাতে পারেন:

python3 ddos.py





---

Step-by-Step Guide for Windows:

1. Install Python:

প্রথমে Python ইনস্টল করুন Python Official Website থেকে। ইনস্টলেশন প্রক্রিয়া অনুসরণ করুন এবং Add Python to PATH নির্বাচন করুন।



2. Install Git:

Git ইনস্টল করতে Git Official Website থেকে Git ডাউনলোড এবং ইনস্টল করুন।



3. Clone the GitHub Repository:

Windows কমান্ড প্রম্পট বা PowerShell খুলুন এবং নিচের কমান্ডটি রান করুন:

git clone https://github.com/KhHacker001/Rabby_ddos.git
cd Rabby_ddos



4. Install Python Libraries:

প্রয়োজনীয় প্যাকেজগুলি ইনস্টল করতে পিপ ব্যবহার করুন:

pip install -r requirements.txt



5. Run the Tool:

শেষমেষ টুলটি চালানোর জন্য কমান্ডটি ব্যবহার করুন:

python ddos.py





---

Additional Information:

Requirements.txt ফাইলটি আপনার প্রজেক্টের সমস্ত Python লাইব্রেরির তালিকা থাকবে, যা pip install -r requirements.txt কমান্ড দিয়ে ইনস্টল করা যাবে।

Python Version: নিশ্চিত করুন আপনার সিস্টেমে Python 3.x ভার্সন ইনস্টল করা আছে।

Permissions: যদি কোনো ফাইল এক্সিকিউটেবল না হয়, তাহলে chmod +x ddos.py কমান্ড রান করুন।

Firewall: আপনি যদি টুলটি ব্যবহার করে কোনো ওয়েবসাইট বা সার্ভারে আক্রমণ চালান, তাহলে আপনার আইএসপি বা ওয়েব হোস্টিং প্রদানকারী আপনার অ্যাক্সেস ব্লক করে দিতে পারে। এজন্য VPN ব্যবহার করার পরামর্শ দেওয়া হয়।



---

এই গাইডটি আপনার টুলটি Termux, Linux এবং Windows এ ব্যবহারের জন্য প্রয়োজনীয় প্রতিটি স্টেপ অন্তর্ভুক্ত করেছে। আপনি এখন GitHub থেকে টুলটি ক্লোন করে সহজেই আক্রমণ চালাতে পারবেন।

